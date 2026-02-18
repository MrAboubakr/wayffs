<template>
  <div class="project-detail" v-if="project">
    <!-- Header -->
    <header class="project-detail__header animate-fade-in">
      <router-link to="/dashboard" class="project-detail__back">
        &larr; Back to Dashboard
      </router-link>
      <div class="project-detail__title-row">
        <h1 class="project-detail__title text-gradient-brand">{{ project.title }}</h1>
        <div class="project-detail__id">
          Track ID: <span class="track-id">{{ project.track_id }}</span>
        </div>
      </div>
      <p class="project-detail__desc">{{ project.description }}</p>
    </header>

    <div class="project-detail__content">
      <!-- Left: Task Management -->
      <div class="project-detail__tasks">
        <!-- Add Task (Owner Only) -->
        <BaseCard v-if="project.is_owner" accent="lime" :hoverable="false" class="mb-6 animate-fade-in-delay-1">
          <h2 class="project-detail__section-title">
            <span>➕</span> Add New Task
          </h2>
          <form @submit.prevent="createTask" class="project-detail__form">
            <input v-model="newTaskTitle" placeholder="What needs to be done?" class="input-wayfs" required />
            <button type="submit" class="btn-wayfs btn-primary">Add Task</button>
          </form>
        </BaseCard>

        <!-- Task List -->
        <div class="project-detail__task-list">
          <BaseCard
            v-for="(task, index) in project.tasks"
            :key="task.id"
            :accent="getTaskAccent(task.status)"
            class="project-detail__task-card"
            :class="`animate-fade-in-delay-${Math.min(Number(index) + 1, 3)}`"
          >
            <div class="project-detail__task-header">
              <div class="project-detail__task-info">
                <h3 class="project-detail__task-name">{{ task.title }}</h3>
                <span :class="['badge', statusBadge(task.status)]" class="mt-2">
                  {{ statusLabel(task.status) }}
                </span>
              </div>

              <!-- Owner Actions -->
              <div v-if="project.is_owner" class="project-detail__task-actions">
                <select v-model="task.status" @change="updateTaskStatus(task)" class="input-wayfs text-xs !p-1.5 !rounded-lg" style="width: auto;">
                  <option value="TODO">To Do</option>
                  <option value="IN_PROGRESS">In Progress</option>
                  <option value="DONE">Done</option>
                </select>
                <button @click="deleteTask(task.id)" class="text-gradient-danger font-semibold text-xs hover:underline cursor-pointer">
                  Delete
                </button>
              </div>
            </div>

            <!-- Comments Section -->
            <div class="project-detail__comments">
              <h4 class="project-detail__comments-title">
                Comments <span>({{ task.comments?.length || 0 }})</span>
              </h4>
              <div class="project-detail__comment-list">
                <div
                  v-for="comment in task.comments"
                  :key="comment.id"
                  class="project-detail__comment"
                >
                  <span class="project-detail__comment-author">{{ comment.author.username }}</span>
                  <span class="project-detail__comment-content">{{ comment.content }}</span>
                </div>
              </div>

              <form @submit.prevent="addComment(task.id)" class="project-detail__comment-form">
                <input v-model="newComments[task.id]" placeholder="Add a comment..." class="input-wayfs text-sm flex-grow" />
                <button type="submit" class="btn-wayfs btn-outline text-xs !px-3 !py-1.5">Post</button>
              </form>
            </div>
          </BaseCard>
        </div>
      </div>

      <!-- Right: Sidebar Info (Optional) -->
      <div class="project-detail__info animate-fade-in-delay-2">
        <BaseCard :hoverable="false">
          <h3 class="font-bold mb-3 border-b pb-2" style="border-color: var(--wayfs-border);">Project Info</h3>
          <div class="space-y-4 text-sm">
            <div>
              <p class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Owner</p>
              <p class="font-semibold">{{ project.owner?.username }}</p>
            </div>
            <div>
              <p class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Status</p>
              <span class="badge badge-progress">Active</span>
            </div>
            <div>
              <p class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">Members</p>
              <p>{{ (project.tasks?.length || 0) > 0 ? 'Managed actively' : 'Awaiting tasks' }}</p>
            </div>
          </div>
        </BaseCard>
      </div>
    </div>
  </div>

  <div v-else class="project-detail__loading">
    <div class="project-detail__spinner"></div>
    <p>Loading project details...</p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import api from '../api';
import BaseCard from '../components/ui/BaseCard.vue';

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

const getTaskAccent = (status: string) => {
  switch(status) {
    case 'TODO': return 'brand';
    case 'IN_PROGRESS': return 'cyan';
    case 'DONE': return 'green';
    default: return 'none';
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

<style scoped>
.project-detail {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

.project-detail__header {
  margin-bottom: 2.5rem;
}

.project-detail__back {
  font-size: 0.9rem;
  font-weight: 600;
  color: #5634BA;
  text-decoration: none;
  transition: all 0.2s ease;
  display: inline-block;
  margin-bottom: 1rem;
}

:global(.dark) .project-detail__back {
  color: #48C6CB;
}

.project-detail__back:hover {
  transform: translateX(-4px);
  text-decoration: underline;
}

.project-detail__title-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}

.project-detail__title {
  font-size: 2.25rem;
  font-weight: 900;
  margin: 0;
}

.project-detail__id {
  font-size: 0.85rem;
  color: var(--wayfs-text-secondary);
}

.project-detail__desc {
  font-size: 1.1rem;
  color: var(--wayfs-text-secondary);
  margin-top: 0.5rem;
  max-width: 600px;
}

.project-detail__content {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 2rem;
}

.project-detail__section-title {
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 1.25rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.project-detail__form {
  display: flex;
  gap: 0.75rem;
}

.project-detail__task-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.project-detail__task-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.5rem;
}

.project-detail__task-name {
  font-size: 1.15rem;
  font-weight: 700;
  margin: 0;
}

.project-detail__task-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.project-detail__comments {
  margin-top: 1.5rem;
  padding-top: 1rem;
  border-top: 1px solid var(--wayfs-border);
}

.project-detail__comments-title {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--wayfs-text-secondary);
  margin-bottom: 0.75rem;
}

.project-detail__comments-title span {
  font-weight: 500;
  opacity: 0.6;
}

.project-detail__comment-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.project-detail__comment {
  font-size: 0.85rem;
  padding: 0.5rem 0.75rem;
  background: rgba(86, 52, 186, 0.04);
  border-radius: 0.5rem;
  line-height: 1.4;
}

:global(.dark) .project-detail__comment {
  background: rgba(255, 255, 255, 0.04);
}

.project-detail__comment-author {
  font-weight: 700;
  color: #5634BA;
  margin-right: 0.5rem;
}

:global(.dark) .project-detail__comment-author {
  color: #48C6CB;
}

.project-detail__comment-form {
  display: flex;
  gap: 0.5rem;
}

/* Loading */
.project-detail__loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 5rem 0;
  color: #5634BA;
}

.project-detail__spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(86, 52, 186, 0.1);
  border-left-color: #5634BA;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Mobile */
@media (max-width: 768px) {
  .project-detail__content {
    grid-template-columns: 1fr;
  }

  .project-detail__title {
    font-size: 1.75rem;
  }

  .project-detail__form {
    flex-direction: column;
  }

  .project-detail__task-header {
    flex-direction: column;
    gap: 1rem;
  }
}
</style>
