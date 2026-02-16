<template>
  <div class="flex min-h-[calc(100vh-72px)] items-center justify-center p-4">
    <div class="card-wayfs w-full max-w-md animate-fade-in">
      <h2 class="text-2xl font-bold mb-6 text-center text-gradient-brand">Register</h2>
      <form @submit.prevent="handleRegister">
        <div class="mb-4">
          <label class="label-wayfs">Username</label>
          <input
            v-model="username"
            type="text"
            class="input-wayfs"
            placeholder="Your username"
            required
          />
        </div>
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
          class="btn-wayfs btn-secondary w-full"
        >
          Register
        </button>
      </form>
      <p class="mt-4 text-center text-sm" style="color: var(--wayfs-text-secondary);">
        Already have an account?
        <router-link to="/login" class="text-gradient-brand font-semibold hover:underline">Login</router-link>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth';

const username = ref('');
const email = ref('');
const password = ref('');
const authStore = useAuthStore();

const handleRegister = async () => {
  try {
    await authStore.register({
      username: username.value,
      email: email.value,
      password: password.value,
    });
  } catch (error) {
    alert('Registration failed');
  }
};
</script>
