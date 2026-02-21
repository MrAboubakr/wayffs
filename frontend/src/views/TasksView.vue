<template>
  <div class="page-container">
    <div class="page-header animate-fade-in">
      <h1 class="section-title">✅ Tasks</h1>
      <p class="section-subtitle">Manage and track your tasks across all projects</p>
    </div>

    <!-- Task filters -->
    <div class="task-filters animate-fade-in-delay-1">
      <button class="task-filter task-filter--active">All</button>
      <button class="task-filter">To Do</button>
      <button class="task-filter">In Progress</button>
      <button class="task-filter">Done</button>
    </div>

    <!-- Task list -->
    <div class="task-list">
      <div v-for="(task, i) in tasks" :key="i" class="task-item card-wayfs animate-fade-in-delay-2">
        <div class="task-item__check" :class="{ 'task-item__check--done': task.done }">
          <span v-if="task.done">✓</span>
        </div>
        <div class="task-item__content">
          <h3 class="task-item__title" :class="{ 'task-item__title--done': task.done }">{{ task.title }}</h3>
          <p class="task-item__meta">
            <span class="badge" :class="task.badgeClass">{{ task.status }}</span>
            <span class="task-item__project">{{ task.project }}</span>
          </p>
        </div>
        <span class="task-item__date">{{ task.date }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const tasks = [
  { title: 'Design homepage wireframe', status: 'Done', badgeClass: 'badge-done', done: true, project: 'Website Redesign', date: 'Feb 18' },
  { title: 'Set up CI/CD pipeline', status: 'In Progress', badgeClass: 'badge-progress', done: false, project: 'Backend API', date: 'Feb 19' },
  { title: 'Write API documentation', status: 'To Do', badgeClass: 'badge-todo', done: false, project: 'Backend API', date: 'Feb 20' },
  { title: 'Create user onboarding flow', status: 'In Progress', badgeClass: 'badge-progress', done: false, project: 'Mobile App', date: 'Feb 20' },
  { title: 'Deploy staging environment', status: 'To Do', badgeClass: 'badge-todo', done: false, project: 'DevOps', date: 'Feb 21' },
];
</script>

<style scoped>
.page-header {
  margin-bottom: 2rem;
}

.task-filters {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

.task-filter {
  padding: 0.45rem 1.1rem;
  border-radius: 9999px;
  border: 1px solid var(--wayfs-border);
  background: transparent;
  color: var(--wayfs-text-secondary);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.task-filter:hover {
  color: var(--wayfs-text);
  border-color: #10B860;
}

.task-filter--active {
  background: linear-gradient(135deg, #0D9647, #10B860);
  color: #fff;
  border-color: transparent;
}

.task-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.task-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.25rem;
}

.task-item__check {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 2px solid var(--wayfs-border);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  font-size: 0.85rem;
  font-weight: 700;
  color: transparent;
  transition: all 0.3s ease;
  cursor: pointer;
}

.task-item__check:hover {
  border-color: #10B860;
}

.task-item__check--done {
  background: linear-gradient(135deg, #0D9647, #22C55E);
  border-color: transparent;
  color: #fff;
}

.task-item__content {
  flex: 1;
  min-width: 0;
}

.task-item__title {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--wayfs-text);
  margin-bottom: 0.3rem;
}

.task-item__title--done {
  text-decoration: line-through;
  opacity: 0.5;
}

.task-item__meta {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.8rem;
}

.task-item__project {
  color: var(--wayfs-text-secondary);
}

.task-item__date {
  font-size: 0.8rem;
  color: var(--wayfs-text-secondary);
  white-space: nowrap;
}
</style>
