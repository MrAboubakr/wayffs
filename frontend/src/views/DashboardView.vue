<template>
  <div class="page-container">
    <div class="flex justify-between items-center mb-8 animate-fade-in">
      <h1 class="section-title text-gradient-brand">Dashboard</h1>
    </div>

    <!-- Create Project Section -->
    <div class="card-wayfs mb-6 animate-fade-in-delay-1">
      <h2 class="text-xl font-semibold mb-4 text-gradient-lime">Create New Project</h2>
      <form @submit.prevent="createProject" class="flex gap-4">
        <input v-model="newProjectTitle" placeholder="Project Title" class="input-wayfs flex-grow" required />
        <button type="submit" class="btn-wayfs btn-primary">Create</button>
      </form>
    </div>

    <!-- Track Project Section -->
    <div class="card-wayfs mb-8 animate-fade-in-delay-2">
      <h2 class="text-xl font-semibold mb-4 text-gradient-danger">Track a Project</h2>
      <form @submit.prevent="trackProject" class="flex gap-4">
        <input v-model="trackIdInput" placeholder="Enter Track ID" class="input-wayfs flex-grow" required />
        <button type="submit" class="btn-wayfs btn-success">Track</button>
      </form>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <!-- My Projects -->
      <div class="animate-fade-in-delay-3">
        <h2 class="text-2xl font-semibold mb-4 text-gradient-brand">My Projects</h2>
        <div v-if="myProjects.length === 0" style="color: var(--wayfs-text-secondary);">No projects created yet.</div>
        <div v-else class="space-y-4">
          <router-link
            v-for="project in myProjects"
            :key="project.id"
            :to="`/projects/${project.id}`"
            class="block card-wayfs accent-brand"
          >
            <h3 class="font-bold text-lg" style="color: var(--wayfs-text);">{{ project.title }}</h3>
            <p class="text-sm mt-1" style="color: var(--wayfs-text-secondary);">
              Track ID: <span class="track-id">{{ project.track_id }}</span>
            </p>
            <p class="text-sm mt-2" style="color: var(--wayfs-text-secondary);">{{ project.tasks.length }} Tasks</p>
          </router-link>
        </div>
      </div>

      <!-- Following Projects -->
      <div class="animate-fade-in-delay-3">
        <h2 class="text-2xl font-semibold mb-4 text-gradient-lime">Following</h2>
        <div v-if="followingProjects.length === 0" style="color: var(--wayfs-text-secondary);">Not following any projects.</div>
        <div v-else class="space-y-4">
          <router-link
            v-for="project in followingProjects"
            :key="project.id"
            :to="`/projects/${project.id}`"
            class="block card-wayfs accent-cyan"
          >
            <h3 class="font-bold text-lg" style="color: var(--wayfs-text);">{{ project.title }}</h3>
            <p class="text-sm mt-1" style="color: var(--wayfs-text-secondary);">Owner: {{ project.owner.username }}</p>
            <p class="text-sm mt-2" style="color: var(--wayfs-text-secondary);">{{ project.tasks.length }} Tasks</p>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import api from '../api';

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
    return projects.value.filter(p => p.is_owner);
});

const followingProjects = computed(() => {
    return projects.value.filter(p => !p.is_owner);
});

onMounted(() => {
  fetchProjects();
});
</script>
