<template>
  <div class="page-container" v-if="project">
    <div class="mb-6 animate-fade-in">
      <router-link to="/" class="text-gradient-brand font-semibold hover:underline inline-flex items-center gap-1">
        &larr; Back to Dashboard
      </router-link>
      <h1 class="text-3xl font-bold mt-3 text-gradient-brand">{{ project.title }}</h1>
      <p style="color: var(--wayfs-text-secondary);" class="mt-1">{{ project.description }}</p>
      <div class="mt-3 text-sm" style="color: var(--wayfs-text-secondary);">
        Track ID: <span class="track-id">{{ project.track_id }}</span>
      </div>
    </div>

    <!-- Add Task (Owner Only) -->
    <div v-if="project.is_owner" class="card-wayfs mb-8 animate-fade-in-delay-1">
      <h2 class="text-xl font-semibold mb-4 text-gradient-lime">Add Task</h2>
      <form @submit.prevent="createTask" class="flex gap-4">
        <input v-model="newTaskTitle" placeholder="Task Title" class="input-wayfs flex-grow" required />
        <button type="submit" class="btn-wayfs btn-primary">Add</button>
      </form>
    </div>

    <!-- Task List -->
    <div class="space-y-4">
      <div
        v-for="(task, index) in project.tasks"
        :key="task.id"
        class="card-wayfs"
        :class="Number(index) < 1 ? 'animate-fade-in-delay-1' : Number(index) < 2 ? 'animate-fade-in-delay-2' : 'animate-fade-in-delay-3'"
      >
        <div class="flex justify-between items-start">
          <div>
            <h3 class="font-bold text-lg" style="color: var(--wayfs-text);">{{ task.title }}</h3>
            <span :class="statusBadge(task.status)" class="badge mt-2">
              {{ statusLabel(task.status) }}
            </span>
          </div>
          <!-- Owner Actions -->
          <div v-if="project.is_owner" class="flex items-center gap-3">
             <select v-model="task.status" @change="updateTaskStatus(task)" class="input-wayfs text-sm !p-1.5 !rounded-lg" style="width: auto;">
                <option value="TODO">To Do</option>
                <option value="IN_PROGRESS">In Progress</option>
                <option value="DONE">Done</option>
             </select>
             <button @click="deleteTask(task.id)" class="text-gradient-danger font-semibold text-sm hover:underline cursor-pointer">Delete</button>
          </div>
        </div>

        <!-- Comments Section -->
        <div class="mt-4 border-t pt-3" style="border-color: var(--wayfs-border);">
           <h4 class="font-semibold text-sm mb-2" style="color: var(--wayfs-text-secondary);">Comments</h4>
           <div
             v-for="comment in task.comments"
             :key="comment.id"
             class="text-sm p-2 rounded-lg mb-2"
             style="background: var(--wayfs-surface); color: var(--wayfs-text);"
           >
              <span class="font-bold text-gradient-brand">{{ comment.author.username }}:</span> {{ comment.content }}
           </div>

           <form @submit.prevent="addComment(task.id)" class="mt-2 flex gap-2">
             <input v-model="newComments[task.id]" placeholder="Add a comment..." class="input-wayfs text-sm flex-grow" />
             <button type="submit" class="btn-wayfs btn-outline text-sm !px-3 !py-1.5">Post</button>
           </form>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="page-container text-center py-20">
    <p class="text-gradient-brand text-xl font-semibold">Loading...</p>
  </div>
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

const statusBadge = (status: string) => {
    switch(status) {
        case 'TODO': return 'badge-todo';
        case 'IN_PROGRESS': return 'badge-progress';
        case 'DONE': return 'badge-done';
        default: return 'badge-todo';
    }
}

const statusLabel = (status: string) => {
    switch(status) {
        case 'TODO': return 'To Do';
        case 'IN_PROGRESS': return 'In Progress';
        case 'DONE': return 'Done';
        default: return status;
    }
}

onMounted(() => {
  fetchProject();
});
</script>
