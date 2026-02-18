<template>
  <div class="app-root">
    <!-- Animated background blobs (dark mode) -->
    <div v-if="isDark" class="dark-bg-animated">
      <div class="dark-bg-blob3"></div>
    </div>

    <!-- Navbar -->
    <Navbar />

    <!-- Main layout -->
    <div class="app-body">
      <!-- Sidebar (authenticated only) -->
      <Sidebar v-if="authStore.isAuthenticated" ref="sidebarRef" />

      <!-- Page content -->
      <main class="app-content">
        <router-view v-slot="{ Component }">
          <Transition name="page" mode="out-in">
            <component :is="Component" />
          </Transition>
        </router-view>
      </main>
    </div>

    <!-- Footer (shown on public pages or always) -->
    <Footer v-if="!authStore.isAuthenticated" />
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from './stores/auth';
import { useTheme } from './composables/useTheme';
import Navbar from './components/layout/Navbar.vue';
import Sidebar from './components/layout/Sidebar.vue';
import Footer from './components/layout/Footer.vue';

const authStore = useAuthStore();
const { isDark } = useTheme();
</script>

<style>
/* Page route transition */
.page-enter-active,
.page-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.page-enter-from {
  opacity: 0;
  transform: translateY(8px);
}

.page-leave-to {
  opacity: 0;
  transform: translateY(-8px);
}
</style>

<style scoped>
.app-root {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-body {
  display: flex;
  flex: 1;
  min-height: 0;
}

.app-content {
  flex: 1;
  overflow-y: auto;
  min-height: calc(100vh - 57px);
}
</style>
