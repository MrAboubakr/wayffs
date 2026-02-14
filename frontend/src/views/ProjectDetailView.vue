<template>
  <div class="p-6" v-if="project">
    <div class="mb-6">
      <router-link to="/" class="text-blue-500 hover:underline">&larr; Back to Dashboard</router-link>
      <h1 class="text-3xl font-bold mt-2">{{ project.title }}</h1>
      <p class="text-gray-600">{{ project.description }}</p>
      <div class="mt-2 text-sm text-gray-500">
        Track ID: <span class="font-mono bg-gray-100 p-1 select-all">{{ project.track_id }}</span>
      </div>
    </div>

    <!-- Add Task (Owner Only) -->
    <div v-if="project.is_owner" class="mb-8 p-4 bg-white rounded shadow">
      <h2 class="text-xl font-semibold mb-4">Add Task</h2>
      <form @submit.prevent="createTask" class="flex gap-4">
        <input v-model="newTaskTitle" placeholder="Task Title" class="border p-2 rounded flex-grow" required />
        <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Add</button>
      </form>
    </div>

    <!-- Task List -->
    <div class="space-y-4">
      <div v-for="task in project.tasks" :key="task.id" class="bg-white p-4 rounded shadow">
        <div class="flex justify-between items-start">
          <div>
            <h3 class="font-bold text-lg">{{ task.title }}</h3>
            <span :class="statusClass(task.status)" class="text-xs px-2 py-1 rounded text-white inline-block mt-1">
              {{ task.status }}
            </span>
          </div>
          <!-- Owner Actions -->
          <div v-if="project.is_owner" class="flex gap-2">
             <select v-model="task.status" @change="updateTaskStatus(task)" class="border rounded p-1 text-sm">
                <option value="TODO">To Do</option>
                <option value="IN_PROGRESS">In Progress</option>
                <option value="DONE">Done</option>
             </select>
             <button @click="deleteTask(task.id)" class="text-red-500 text-sm hover:underline">Delete</button>
          </div>
        </div>
        
        <!-- Comments Section -->
        <div class="mt-4 border-t pt-2">
           <h4 class="font-semibold text-sm mb-2">Comments</h4>
           <div v-for="comment in task.comments" :key="comment.id" class="text-sm bg-gray-50 p-2 rounded mb-2">
              <span class="font-bold">{{ comment.author.username }}:</span> {{ comment.content }}
           </div>
           
           <form @submit.prevent="addComment(task.id)" class="mt-2 flex gap-2">
             <input v-model="newComments[task.id]" placeholder="Add a comment..." class="border p-1 rounded flex-grow text-sm" />
             <button type="submit" class="bg-gray-200 px-2 py-1 rounded text-sm hover:bg-gray-300">Post</button>
           </form>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="p-6 text-center">Loading...</div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import api from '../api';

const route = useRoute();
const project = ref<any>(null);
const newTaskTitle = ref('');
const newComments = ref<Record<number, string>>({});

const fetchProject = async () => {
  try {
    const response = await api.get(`projects/${route.params.id}/`);
    project.value = response.data;
  } catch (error) {
    console.error('Failed to fetch project', error);
  }
};

const createTask = async () => {
  try {
    await api.post('tasks/', { 
        title: newTaskTitle.value,
        project: project.value.id
    });
    newTaskTitle.value = '';
    await fetchProject();
  } catch (error) {
    alert('Failed to create task');
  }
};

const updateTaskStatus = async (task: any) => {
    try {
        await api.patch(`tasks/${task.id}/`, { status: task.status });
    } catch (error) {
        alert('Failed to update status');
    }
}

const deleteTask = async (taskId: number) => {
    if(!confirm("Are you sure?")) return;
    try {
        await api.delete(`tasks/${taskId}/`);
        await fetchProject();
    } catch (error) {
        alert('Failed to delete task');
    }
}

const addComment = async (taskId: number) => {
    const content = newComments.value[taskId];
    if(!content) return;
    try {
        await api.post('comments/', { task: taskId, content });
        newComments.value[taskId] = '';
        await fetchProject();
    } catch (error) {
        alert('Failed to post comment');
    }
}

const statusClass = (status: string) => {
    switch(status) {
        case 'TODO': return 'bg-gray-500';
        case 'IN_PROGRESS': return 'bg-blue-500';
        case 'DONE': return 'bg-green-500';
        default: return 'bg-gray-500';
    }
}

onMounted(() => {
  fetchProject();
});
</script>
