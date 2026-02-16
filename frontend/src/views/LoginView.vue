<template>
  <div class="flex min-h-[calc(100vh-72px)] items-center justify-center p-4">
    <div class="card-wayfs w-full max-w-md animate-fade-in">
      <h2 class="text-2xl font-bold mb-6 text-center text-gradient-brand">Login</h2>
      <form @submit.prevent="handleLogin">
        <div class="mb-4">
          <label class="label-wayfs">Email</label>
          <input
            v-model="email"
            type="email"
            class="input-wayfs"
            placeholder="you@example.com"
            required
          />
        </div>
        <div class="mb-6">
          <label class="label-wayfs">Password</label>
          <input
            v-model="password"
            type="password"
            class="input-wayfs"
            placeholder="••••••••"
            required
          />
        </div>
        <button
          type="submit"
          class="btn-wayfs btn-primary w-full"
        >
          Login
        </button>
      </form>
      <p class="mt-4 text-center text-sm" style="color: var(--wayfs-text-secondary);">
        Don't have an account?
        <router-link to="/register" class="text-gradient-brand font-semibold hover:underline">Register</router-link>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth';

const email = ref('');
const password = ref('');
const authStore = useAuthStore();

const handleLogin = async () => {
  try {
    await authStore.login({ email: email.value, password: password.value });
  } catch (error) {
    alert('Invalid credentials');
  }
};
</script>
