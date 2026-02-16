<template>
  <div :class="['base-card', accentClass, { 'base-card--hoverable': hoverable }]">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';

const props = withDefaults(defineProps<{
  accent?: 'brand' | 'cyan' | 'magenta' | 'green' | 'lime' | 'none';
  hoverable?: boolean;
}>(), {
  accent: 'none',
  hoverable: true,
});

const accentClass = computed(() => {
  if (props.accent === 'none') return '';
  return `base-card--accent-${props.accent}`;
});
</script>

<style scoped>
.base-card {
  background: var(--wayfs-card);
  border: 1px solid var(--wayfs-border);
  border-radius: 1rem;
  padding: 1.5rem;
  backdrop-filter: blur(12px);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.base-card--hoverable:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 40px rgba(86, 52, 186, 0.12);
  border-color: rgba(86, 52, 186, 0.3);
}

:global(.dark) .base-card--hoverable:hover {
  box-shadow: 0 12px 40px rgba(72, 198, 203, 0.15);
  border-color: rgba(72, 198, 203, 0.3);
}

.base-card--accent-brand { border-left: 4px solid #5634BA; }
.base-card--accent-cyan { border-left: 4px solid #48C6CB; }
.base-card--accent-magenta { border-left: 4px solid #C914C7; }
.base-card--accent-green { border-left: 4px solid #16FF4B; }
.base-card--accent-lime { border-left: 4px solid #96A80D; }
</style>
