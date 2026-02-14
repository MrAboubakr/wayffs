<template>
  <div class="p-6">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold">Dashboard</h1>
      <button @click="authStore.logout()" class="text-red-500 hover:text-red-700">Logout</button>
    </div>

    <!-- Create Project Section -->
    <div class="mb-8 p-4 bg-white rounded shadow">
      <h2 class="text-xl font-semibold mb-4">Create New Project</h2>
      <form @submit.prevent="createProject" class="flex gap-4">
        <input v-model="newProjectTitle" placeholder="Project Title" class="border p-2 rounded flex-grow" required />
        <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Create</button>
      </form>
    </div>

    <!-- Track Project Section -->
    <div class="mb-8 p-4 bg-white rounded shadow">
      <h2 class="text-xl font-semibold mb-4">Track a Project</h2>
      <form @submit.prevent="trackProject" class="flex gap-4">
        <input v-model="trackIdInput" placeholder="Enter Track ID" class="border p-2 rounded flex-grow" required />
        <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">Track</button>
      </form>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <!-- My Projects -->
      <div>
        <h2 class="text-2xl font-semibold mb-4">My Projects</h2>
        <div v-if="myProjects.length === 0" class="text-gray-500">No projects created yet.</div>
        <div v-else class="space-y-4">
          <div v-for="project in myProjects" :key="project.id" class="bg-white p-4 rounded shadow border-l-4 border-blue-500">
            <h3 class="font-bold text-lg">{{ project.title }}</h3>
            <p class="text-sm text-gray-600">Track ID: <span class="font-mono bg-gray-100 p-1">{{ project.track_id }}</span></p>
            <p class="text-sm text-gray-500 mt-2">{{ project.tasks.length }} Tasks</p>
          </div>
        </div>
      </div>

      <!-- Following Projects -->
      <div>
        <h2 class="text-2xl font-semibold mb-4">Following</h2>
        <div v-if="followingProjects.length === 0" class="text-gray-500">Not following any projects.</div>
        <div v-else class="space-y-4">
          <div v-for="project in followingProjects" :key="project.id" class="bg-white p-4 rounded shadow border-l-4 border-green-500">
            <h3 class="font-bold text-lg">{{ project.title }}</h3>
            <p class="text-sm text-gray-600">Owner: {{ project.owner.username }}</p>
            <p class="text-sm text-gray-500 mt-2">{{ project.tasks.length }} Tasks</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useAuthStore } from '../stores/auth';
import api from '../api';

const authStore = useAuthStore();
const projects = ref<any[]>([]);
const newProjectTitle = ref('');
const trackIdInput = ref('');

const fetchProjects = async () => {
  try {
    const response = await api.get('projects/');
    projects.value = response.data;
  } catch (error) {
    console.error('Failed to fetch projects', error);
  }
};

const createProject = async () => {
  try {
    await api.post('projects/', { title: newProjectTitle.value });
    newProjectTitle.value = '';
    await fetchProjects();
  } catch (error) {
    alert('Failed to create project');
  }
};

const trackProject = async () => {
  try {
    await api.post('projects/track/', { track_id: trackIdInput.value });
    trackIdInput.value = '';
    await fetchProjects();
  } catch (error: any) {
    alert(error.response?.data?.error || 'Failed to track project');
  }
};

const myProjects = computed(() => {
    // Ideally backend flags ownership or we compare ID
    // Since serializer has is_owner field now
    return projects.value.filter(p => p.is_owner);
});

const followingProjects = computed(() => {
    return projects.value.filter(p => !p.is_owner);
});

onMounted(() => {
  fetchProjects();
});
</script>
