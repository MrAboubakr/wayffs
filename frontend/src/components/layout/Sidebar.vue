<template>
  <aside
    class="sidebar"
    :class="{
      'sidebar--collapsed': isCollapsed,
      'sidebar--mobile-open': isMobileOpen,
    }"
  >
    <!-- Collapse toggle -->
    <button class="sidebar__toggle" @click="toggleCollapse" :title="isCollapsed ? 'Expand' : 'Collapse'">
      <svg :class="{ 'rotate-180': isCollapsed }" width="18" height="18" viewBox="0 0 18 18" fill="none">
        <path d="M11 4L6 9L11 14" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>

    <!-- Navigation items -->
    <nav class="sidebar__nav">
      <router-link
        v-for="item in menuItems"
        :key="item.to"
        :to="item.to"
        class="sidebar__item"
        active-class="sidebar__item--active"
        :title="isCollapsed ? item.label : undefined"
        @click="closeMobile"
      >
        <span class="sidebar__icon">{{ item.icon }}</span>
        <Transition name="fade-slide">
          <span v-if="!isCollapsed" class="sidebar__label">{{ item.label }}</span>
        </Transition>
      </router-link>
    </nav>

    <!-- Bottom section -->
    <div class="sidebar__bottom">
      <router-link to="/settings" class="sidebar__item" active-class="sidebar__item--active" @click="closeMobile">
        <span class="sidebar__icon">⚙️</span>
        <Transition name="fade-slide">
          <span v-if="!isCollapsed" class="sidebar__label">Settings</span>
        </Transition>
      </router-link>
    </div>
  </aside>

  <!-- Mobile overlay -->
  <Transition name="fade">
    <div v-if="isMobileOpen" class="sidebar__overlay" @click="closeMobile"></div>
  </Transition>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const isCollapsed = ref(false);
const isMobileOpen = ref(false);

const menuItems = [
  { icon: '📊', label: 'Dashboard', to: '/dashboard' },
  { icon: '📁', label: 'Projects', to: '/projects' },
  { icon: '✅', label: 'Tasks', to: '/tasks' },
  { icon: '📈', label: 'Analytics', to: '/analytics' },
  { icon: '🕐', label: 'Activity', to: '/activity' },
];

const toggleCollapse = () => { isCollapsed.value = !isCollapsed.value; };
const closeMobile = () => { isMobileOpen.value = false; };

const toggleMobile = () => { isMobileOpen.value = !isMobileOpen.value; };

defineExpose({ toggleMobile });
</script>

<style scoped>
.sidebar {
  width: 240px;
  min-height: calc(100vh - 57px);
  background: var(--wayfs-surface);
  border-right: 1px solid var(--wayfs-border);
  display: flex;
  flex-direction: column;
  padding: 1rem 0.75rem;
  transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  overflow-y: auto;
  overflow-x: hidden;
  flex-shrink: 0;
  position: relative;
}

:global(.dark) .sidebar {
  background: var(--color-dark-surface);
}

.sidebar--collapsed {
  width: 68px;
}

.sidebar__toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 0.375rem;
  border: 1px solid var(--wayfs-border);
  background: var(--wayfs-card);
  color: var(--wayfs-text-secondary);
  cursor: pointer;
  position: absolute;
  top: 1rem;
  right: -14px;
  z-index: 10;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.sidebar__toggle:hover {
  color: var(--wayfs-text);
  border-color: #10B860;
}

.sidebar__toggle svg {
  transition: transform 0.3s ease;
}

.sidebar__nav {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  margin-top: 2rem;
  flex: 1;
}

.sidebar__item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.65rem 0.75rem;
  border-radius: 0.5rem;
  text-decoration: none;
  color: var(--wayfs-text-secondary);
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.sidebar__item:hover {
  color: var(--wayfs-text);
  background: rgba(13, 150, 71, 0.06);
}

:global(.dark) .sidebar__item:hover {
  background: rgba(245, 184, 0, 0.08);
}

.sidebar__item--active {
  color: #0D9647;
  background: rgba(13, 150, 71, 0.1);
  font-weight: 600;
}

:global(.dark) .sidebar__item--active {
  color: #10B860;
  background: rgba(245, 184, 0, 0.12);
}

.sidebar__icon {
  font-size: 1.15rem;
  flex-shrink: 0;
  width: 28px;
  text-align: center;
}

.sidebar__label {
  overflow: hidden;
}

.sidebar__bottom {
  padding-top: 0.5rem;
  border-top: 1px solid var(--wayfs-border);
  margin-top: 0.5rem;
}

/* Transitions */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.2s ease;
}

.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateX(-8px);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Mobile overlay */
.sidebar__overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 40;
}

/* Mobile sidebar */
@media (max-width: 768px) {
  .sidebar {
    position: fixed;
    top: 57px;
    left: 0;
    bottom: 0;
    z-index: 50;
    transform: translateX(-100%);
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 4px 0 24px rgba(0, 0, 0, 0.15);
  }

  .sidebar--mobile-open {
    transform: translateX(0);
  }

  .sidebar__toggle {
    display: none;
  }

  .sidebar--collapsed {
    width: 240px;
  }
}
</style>
