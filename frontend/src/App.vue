<template>
  <div :class="['min-h-screen transition-colors duration-400', isDark ? 'dark' : '']">
    <!-- Animated background blobs (dark mode) -->
    <div v-if="isDark" class="dark-bg-animated">
      <div class="dark-bg-blob3"></div>
    </div>

    <!-- Navigation -->
    <nav class="nav-wayfs">
      <router-link to="/" class="nav-brand">Wayfs</router-link>
      <div class="flex items-center gap-2">
        <template v-if="authStore.isAuthenticated">
          <router-link to="/" class="nav-link">Dashboard</router-link>
          <button @click="authStore.logout()" class="nav-link" style="cursor:pointer;">Logout</button>
        </template>
        <template v-else>
          <router-link to="/login" class="nav-link">Login</router-link>
          <router-link to="/register" class="nav-link">Register</router-link>
        </template>
        <button @click="toggleTheme" class="theme-toggle" :title="isDark ? 'Switch to light mode' : 'Switch to dark mode'">
          {{ isDark ? '☀️' : '🌙' }}
        </button>
      </div>
    </nav>

    <!-- Page content -->
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuthStore } from './stores/auth';

const authStore = useAuthStore();

const isDark = ref(false);

onMounted(() => {
  const saved = localStorage.getItem('wayfs-theme');
  if (saved === 'dark') {
    isDark.value = true;
  } else if (!saved) {
    isDark.value = window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
});

const toggleTheme = () => {
  isDark.value = !isDark.value;
  localStorage.setItem('wayfs-theme', isDark.value ? 'dark' : 'light');
};
</script>
