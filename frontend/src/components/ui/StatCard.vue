<template>
  <div class="stat-card">
    <div class="stat-card__icon" :style="{ background: iconBg }">
      <span class="stat-card__icon-text">{{ icon }}</span>
    </div>
    <div class="stat-card__content">
      <p class="stat-card__label">{{ label }}</p>
      <p class="stat-card__value">{{ value }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
withDefaults(defineProps<{
  icon: string;
  label: string;
  value: string | number;
  iconBg?: string;
}>(), {
  iconBg: 'linear-gradient(135deg, #0A7B3B, #10B860)',
});
</script>

<style scoped>
.stat-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: var(--wayfs-card);
  border: 1px solid var(--wayfs-border);
  border-radius: 1rem;
  padding: 1.25rem 1.5rem;
  backdrop-filter: blur(12px);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.stat-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 40px rgba(13, 150, 71, 0.12);
}

:global(.dark) .stat-card:hover {
  box-shadow: 0 12px 40px rgba(245, 184, 0, 0.15);
}

.stat-card__icon {
  width: 48px;
  height: 48px;
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.stat-card__icon-text {
  font-size: 1.4rem;
}

.stat-card__label {
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--wayfs-text-secondary);
  margin-bottom: 0.15rem;
}

.stat-card__value {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--wayfs-text);
}
</style>
