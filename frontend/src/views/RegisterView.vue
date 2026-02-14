<template>
  <div class="flex min-h-screen items-center justify-center bg-gray-100">
    <div class="w-full max-w-md bg-white p-8 rounded-lg shadow-md">
      <h2 class="text-2xl font-bold mb-6 text-center">Register</h2>
      <form @submit.prevent="handleRegister">
        <div class="mb-4">
          <label class="block text-gray-700">Username</label>
          <input
            v-model="username"
            type="text"
            class="w-full mt-2 p-2 border rounded-md"
            required
          />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700">Email</label>
          <input
            v-model="email"
            type="email"
            class="w-full mt-2 p-2 border rounded-md"
            required
          />
        </div>
        <div class="mb-6">
          <label class="block text-gray-700">Password</label>
          <input
            v-model="password"
            type="password"
            class="w-full mt-2 p-2 border rounded-md"
            required
          />
        </div>
        <button
          type="submit"
          class="w-full bg-green-500 text-white p-2 rounded-md hover:bg-green-600"
        >
          Register
        </button>
      </form>
      <p class="mt-4 text-center">
        Already have an account? <router-link to="/login" class="text-blue-500">Login</router-link>
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
