<template>
  <div class="page-container">
    <div class="page-header animate-fade-in">
      <h1 class="section-title">🕐 Activity Feed</h1>
      <p class="section-subtitle">Keep track of everything happening in your workspace</p>
    </div>

    <div class="activity-timeline">
      <div v-for="(item, i) in activities" :key="i" class="activity-item animate-fade-in" :style="{ animationDelay: (i * 0.1) + 's' }">
        <div class="activity-dot shadow-glow"></div>
        <div class="activity-card card-wayfs">
          <div class="activity-header">
            <span class="activity-user">{{ item.user }}</span>
            <span class="activity-time">{{ item.time }}</span>
          </div>
          <div class="activity-body">
            {{ item.action }} <span class="activity-context">{{ item.context }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const activities = [
  { user: 'Aboubakr', action: 'completed task', context: 'Design homepage wireframe', time: '2 hours ago' },
  { user: 'Sarah', action: 'added project', context: 'Marketing Campaign Q3', time: '5 hours ago' },
  { user: 'John', action: 'updated status of', context: 'API Integration', time: 'Yesterday' },
  { user: 'Aboubakr', action: 'invited', context: 'Sarah to Team Alpha', time: '2 days ago' },
];
</script>

<style scoped>
.activity-timeline {
  display: flex;
  flex-direction: column;
  gap: 0;
  padding-left: 1.5rem;
  border-left: 2px solid var(--wayfs-border);
  margin-top: 2rem;
}

.activity-item {
  position: relative;
  padding-bottom: 2rem;
}

.activity-item:last-child {
  padding-bottom: 0;
}

.activity-dot {
  position: absolute;
  left: -24px;
  top: 1rem;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: #10B860;
  border: 3px solid var(--wayfs-bg);
  box-shadow: 0 0 10px rgba(16, 184, 96, 0.4);
}

.activity-card {
  padding: 1.25rem;
}

.activity-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.activity-user {
  font-weight: 700;
  color: var(--wayfs-text);
  font-size: 0.95rem;
}

.activity-time {
  font-size: 0.8rem;
  color: var(--wayfs-text-secondary);
}

.activity-body {
  font-size: 0.9rem;
  color: var(--wayfs-text-secondary);
}

.activity-context {
  color: #10B860;
  font-weight: 600;
}
</style>
