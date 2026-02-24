<template>
  <div class="api-test-widget card">
    <h3>Test Your Agent API</h3>
    <p class="text-sm text-secondary mb-4 mt-1">Paste your Agent API Key below to fetch the accessible tasks.</p>
    
    <div class="form-group flex gap-2">
      <input 
        v-model="apiKey" 
        type="password" 
        placeholder="Enter your Agent API Key" 
        class="form-input flex-1"
      />
      <button @click="testApi" :disabled="loading || !apiKey" class="btn btn--primary whitespace-nowrap">
        {{ loading ? 'Testing...' : 'Send Request' }}
      </button>
    </div>

    <div v-if="response" class="response-box mt-4 bg-gray-900 rounded p-4 text-green-400 font-mono text-sm overflow-x-auto">
      <pre>{{ JSON.stringify(response, null, 2) }}</pre>
    </div>
    <div v-if="error" class="response-box error mt-4 bg-red-900/20 border border-red-500 rounded p-4 text-red-500 font-mono text-sm">
      {{ error }}
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { API_BASE_URL } from '../../api';

const apiKey = ref('');
const response = ref<any>(null);
const error = ref('');
const loading = ref(false);

const testApi = async () => {
    loading.value = true;
    error.value = '';
    response.value = null;

    try {
        // Ensure proper format
        const fullKey = apiKey.value.startsWith('Api-Key ') ? apiKey.value : `Api-Key ${apiKey.value}`;
        
        const res = await fetch(`${API_BASE_URL}/api/v1/agents/tasks/`, {
            method: 'GET',
            headers: {
                'Authorization': fullKey,
                'Content-Type': 'application/json'
            }
        });

        const data = await res.json();

        if (!res.ok) {
            throw new Error(`HTTP ${res.status}: ${data.detail || res.statusText}`);
        }

        response.value = data;
    } catch (err: any) {
        error.value = err.message || 'Connection failed';
    } finally {
        loading.value = false;
    }
}
</script>

<style scoped>
.api-test-widget {
  border: 1px solid var(--wayfs-border);
  padding: 1.5rem;
  border-radius: 0.5rem;
  margin: 1.5rem 0;
  background: var(--wayfs-surface);
}

:global(.dark) .api-test-widget {
  background: var(--color-dark-surface);
}
</style>
