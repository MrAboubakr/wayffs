<template>
  <div class="dashboard">
    <!-- Welcome header -->
    <div class="dashboard__header animate-fade-in">
      <div>
        <h1 class="dashboard__title">Welcome back<span v-if="authStore.user">, {{ authStore.user.username }}</span> 👋</h1>
        <p class="dashboard__subtitle">Here's what's happening with your projects</p>
      </div>
    </div>

    <!-- Stats row -->
    <div class="dashboard__stats animate-fade-in-delay-1">
      <StatCard icon="📁" label="Total Projects" :value="projects.length" />
      <StatCard
        icon="✅"
        label="Total Tasks"
        :value="totalTasks"
        icon-bg="linear-gradient(135deg, #96A80D, #16FF4B)"
      />
      <StatCard
        icon="👥"
        label="Following"
        :value="followingProjects.length"
        icon-bg="linear-gradient(135deg, #5634BA, #560DDE)"
      />
      <StatCard
        icon="📊"
        label="My Projects"
        :value="myProjects.length"
        icon-bg="linear-gradient(135deg, #C914C7, #560DDE)"
      />
    </div>

    <!-- Quick actions -->
    <div class="dashboard__actions animate-fade-in-delay-2">
      <!-- Create Project -->
      <BaseCard accent="brand" :hoverable="false">
        <h2 class="dashboard__card-title">
          <span>📝</span> Create New Project
        </h2>
        <form @submit.prevent="createProject" class="dashboard__form">
          <input v-model="newProjectTitle" placeholder="Project Title" class="input-wayfs" required />
          <button type="submit" class="btn-wayfs btn-primary">Create</button>
        </form>
      </BaseCard>

      <!-- Track Project -->
      <BaseCard accent="cyan" :hoverable="false">
        <h2 class="dashboard__card-title">
          <span>🔗</span> Track a Project
        </h2>
        <form @submit.prevent="trackProject" class="dashboard__form">
          <input v-model="trackIdInput" placeholder="Enter Track ID" class="input-wayfs" required />
          <button type="submit" class="btn-wayfs btn-success">Track</button>
        </form>
      </BaseCard>
    </div>

    <!-- Projects grid -->
    <div class="dashboard__grid animate-fade-in-delay-3">
      <!-- My Projects -->
      <div class="dashboard__section">
        <h2 class="dashboard__section-title text-gradient-brand">My Projects</h2>
        <div v-if="myProjects.length === 0" class="dashboard__empty">
          <span class="dashboard__empty-icon">📁</span>
          <p>No projects created yet</p>
          <p class="dashboard__empty-hint">Create your first project above to get started!</p>
        </div>
        <div v-else class="dashboard__project-list">
          <router-link
            v-for="project in myProjects"
            :key="project.id"
            :to="`/projects/${project.id}`"
            class="dashboard__project-card"
          >
            <div class="dashboard__project-header">
              <h3 class="dashboard__project-name">{{ project.title }}</h3>
              <span class="badge badge-progress">Owner</span>
            </div>
            <p class="dashboard__project-meta">
              Track ID: <span class="track-id">{{ project.track_id }}</span>
            </p>
            <div class="dashboard__project-footer">
              <span>{{ project.tasks.length }} Tasks</span>
            </div>
          </router-link>
        </div>
      </div>

      <!-- Following Projects -->
      <div class="dashboard__section">
        <h2 class="dashboard__section-title text-gradient-lime">Following</h2>
        <div v-if="followingProjects.length === 0" class="dashboard__empty">
          <span class="dashboard__empty-icon">👀</span>
          <p>Not following any projects</p>
          <p class="dashboard__empty-hint">Use a Track ID to follow a project!</p>
        </div>
        <div v-else class="dashboard__project-list">
          <router-link
            v-for="project in followingProjects"
            :key="project.id"
            :to="`/projects/${project.id}`"
            class="dashboard__project-card"
          >
            <div class="dashboard__project-header">
              <h3 class="dashboard__project-name">{{ project.title }}</h3>
              <span class="badge badge-todo">Following</span>
            </div>
            <p class="dashboard__project-meta">
              Owner: {{ project.owner.username }}
            </p>
            <div class="dashboard__project-footer">
              <span>{{ project.tasks.length }} Tasks</span>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import api from '../api';
import { useAuthStore } from '../stores/auth';
import StatCard from '../components/ui/StatCard.vue';
import BaseCard from '../components/ui/BaseCard.vue';

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

const myProjects = computed(() => projects.value.filter(p => p.is_owner));
const followingProjects = computed(() => projects.value.filter(p => !p.is_owner));
const totalTasks = computed(() => projects.value.reduce((sum, p) => sum + (p.tasks?.length || 0), 0));

onMounted(() => {
  authStore.fetchUser();
  fetchProjects();
});
</script>

<style scoped>
.dashboard {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

.dashboard__header {
  margin-bottom: 2rem;
}

.dashboard__title {
  font-size: 1.75rem;
  font-weight: 800;
  color: var(--wayfs-text);
  margin-bottom: 0.25rem;
}

.dashboard__subtitle {
  font-size: 0.95rem;
  color: var(--wayfs-text-secondary);
}

/* Stats */
.dashboard__stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  margin-bottom: 2rem;
}

/* Quick actions */
.dashboard__actions {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-bottom: 2rem;
}

.dashboard__card-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--wayfs-text);
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.dashboard__form {
  display: flex;
  gap: 0.75rem;
}

.dashboard__form .input-wayfs {
  flex: 1;
}

/* Projects grid */
.dashboard__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.dashboard__section-title {
  font-size: 1.25rem;
  font-weight: 800;
  margin-bottom: 1rem;
}

.dashboard__empty {
  text-align: center;
  padding: 2.5rem 1rem;
  background: var(--wayfs-card);
  border: 1px dashed var(--wayfs-border);
  border-radius: 1rem;
  color: var(--wayfs-text-secondary);
}

.dashboard__empty-icon {
  font-size: 2.5rem;
  display: block;
  margin-bottom: 0.75rem;
}

.dashboard__empty-hint {
  font-size: 0.8rem;
  margin-top: 0.25rem;
  opacity: 0.7;
}

.dashboard__project-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.dashboard__project-card {
  display: block;
  text-decoration: none;
  background: var(--wayfs-card);
  border: 1px solid var(--wayfs-border);
  border-radius: 0.75rem;
  padding: 1.25rem;
  backdrop-filter: blur(12px);
  transition: all 0.2s ease;
}

.dashboard__project-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(86, 52, 186, 0.1);
  border-color: rgba(86, 52, 186, 0.25);
}

:global(.dark) .dashboard__project-card:hover {
  box-shadow: 0 8px 24px rgba(72, 198, 203, 0.1);
  border-color: rgba(72, 198, 203, 0.25);
}

.dashboard__project-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.dashboard__project-name {
  font-weight: 700;
  font-size: 1rem;
  color: var(--wayfs-text);
}

.dashboard__project-meta {
  font-size: 0.8rem;
  color: var(--wayfs-text-secondary);
  margin-bottom: 0.75rem;
}

.dashboard__project-footer {
  font-size: 0.8rem;
  color: var(--wayfs-text-secondary);
  display: flex;
  align-items: center;
  gap: 1rem;
}

/* Responsive */
@media (max-width: 1024px) {
  .dashboard__stats {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .dashboard__stats {
    grid-template-columns: 1fr;
  }

  .dashboard__actions {
    grid-template-columns: 1fr;
  }

  .dashboard__grid {
    grid-template-columns: 1fr;
  }

  .dashboard__form {
    flex-direction: column;
  }
}
</style>
