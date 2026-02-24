<template>
  <div class="agent-settings">
    <div class="page-header">
      <h1 class="page-title">AI Agents</h1>
      <p class="page-subtitle">Manage AI agents and their API keys for your workspace.</p>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="loading-state">
      Loading agents...
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="error-state">
      {{ error }}
      <button @click="fetchAgents" class="btn btn--secondary mt-2">Retry</button>
    </div>

    <!-- Content -->
    <div v-else class="content-grid">
      
      <!-- Agents List / Management -->
      <section class="card panel-agents">
        <div class="panel-header">
          <h2>Your Agents</h2>
          <button @click="showCreateAgentModal = true" class="btn btn--primary btn--sm">
            + New Agent
          </button>
        </div>

        <div v-if="agents.length === 0" class="empty-state">
          <p>You haven't created any AI Agents yet.</p>
        </div>

        <div v-else class="agents-list">
          <div 
            v-for="agent in agents" 
            :key="agent.id" 
            class="agent-item"
            :class="{ 'agent-item--active': selectedAgent?.id === agent.id }"
            @click="selectAgent(agent)"
          >
            <div class="agent-info">
              <span class="agent-icon">🤖</span>
              <div>
                <h3>{{ agent.name }}</h3>
                <p class="text-sm text-secondary">{{ agent.description || 'No description' }}</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Selected Agent Details & Keys -->
      <section v-if="selectedAgent" class="card panel-details">
        <div class="panel-header">
          <h2>{{ selectedAgent.name }} Details</h2>
          <button @click="deleteAgent(selectedAgent.id!)" class="btn btn--danger btn--sm">
            Delete Agent
          </button>
        </div>

        <!-- API Keys -->
        <div class="keys-section mt-4">
          <div class="flex justify-between items-center mb-3">
            <h3 class="text-lg font-semibold">API Keys</h3>
            <button @click="showCreateKeyModal = true" class="btn btn--secondary btn--sm">
              Generate Key
            </button>
          </div>

          <!-- New Key Display -->
          <div v-if="newlyGeneratedKey" class="new-key-alert">
            <p class="font-bold text-red-600 mb-1">Copy your new API key now. You won't be able to see it again!</p>
            <div class="flex gap-2">
              <input type="text" readonly :value="newlyGeneratedKey" class="form-input flex-1" />
              <button @click="copyToClipboard(newlyGeneratedKey)" class="btn btn--primary">Copy</button>
            </div>
          </div>

          <!-- Existing Keys -->
          <table v-if="selectedAgent.keys?.length" class="table w-full mt-3">
            <thead>
              <tr>
                <th>Key (Hidden)</th>
                <th>Scope</th>
                <th>Expires</th>
                <th>Actions</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="keyInfo in selectedAgent.keys" :key="keyInfo.id">
                <td class="font-mono text-sm">{{ keyInfo.key }}</td>
                <td>
                  <span class="badge" :class="getScopeBadgeClass(keyInfo.scope)">
                    {{ getScopeLabel(keyInfo.scope) }}
                  </span>
                </td>
                <td>{{ formatDate(keyInfo.expires_at) }}</td>
                <td>{{ keyInfo.total_actions || 0 }} actions</td>
                <td class="text-right">
                  <button @click="revokeKey(keyInfo.id!)" class="text-red-500 hover:text-red-700 text-sm">
                    Revoke
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
          <p v-else class="text-sm text-secondary italic mt-3">No active API keys found for this agent.</p>
        </div>

        <hr class="my-6 border-gray-200 dark:border-gray-800" />

        <!-- Recent Activity -->
        <div class="activity-section">
          <h3 class="text-lg font-semibold mb-3">Recent Activity</h3>
          <div v-if="selectedAgent.recent_actions?.length" class="activity-timeline">
            <div v-for="action in selectedAgent.recent_actions" :key="action.id" class="activity-item">
              <div class="activity-dot"></div>
              <div class="activity-content">
                <p class="activity-desc">{{ action.description }}</p>
                <span class="activity-time">{{ formatTimeAgo(action.timestamp) }}</span>
              </div>
            </div>
          </div>
          <p v-else class="text-sm text-secondary italic">No recent activity.</p>
        </div>
      </section>
      
      <section v-else class="card panel-details flex items-center justify-center text-secondary">
        Select an agent to view details and manage API keys.
      </section>

    </div>

    <!-- Create Agent Modal -->
    <div v-if="showCreateAgentModal" class="modal-overlay">
      <div class="modal">
        <h2>Create New Agent</h2>
        <form @submit.prevent="handleCreateAgent">
          <div class="form-group">
            <label>Agent Name</label>
            <input v-model="agentForm.name" type="text" class="form-input" required placeholder="e.g. GitHub Integration Engine" />
          </div>
          <div class="form-group mt-3">
            <label>Description (Optional)</label>
            <textarea v-model="agentForm.description" class="form-input" rows="3" placeholder="What does this agent do?"></textarea>
          </div>
          <div class="modal-actions mt-5">
            <button type="button" @click="showCreateAgentModal = false" class="btn btn--secondary">Cancel</button>
            <button type="submit" class="btn btn--primary" :disabled="isSubmitting">Create Agent</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Create API Key Modal -->
    <div v-if="showCreateKeyModal" class="modal-overlay">
      <div class="modal">
        <h2>Generate API Key</h2>
        <form @submit.prevent="handleGenerateKey">
          <div class="form-group">
            <label>Permission Scope</label>
            <select v-model="keyForm.scope" class="form-select" required>
              <option value="all">Read / Write (No Delete)</option>
              <option value="read_only">Read Only</option>
              <option value="comment_only">Comment Only</option>
            </select>
            <p class="help-text">Agents cannot delete Tasks or Projects regardless of scope.</p>
          </div>
          
          <div class="form-group mt-3">
            <label>Expiration</label>
            <select v-model="keyForm.expirationDays" class="form-select" required>
              <option value="10">10 Days</option>
              <option value="30">30 Days</option>
              <option value="90">90 Days</option>
            </select>
          </div>

          <div class="modal-actions mt-5">
            <button type="button" @click="showCreateKeyModal = false" class="btn btn--secondary">Cancel</button>
            <button type="submit" class="btn btn--primary" :disabled="isSubmitting">Generate Key</button>
          </div>
        </form>
      </div>
    </div>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { AgentService } from '../services/agent';
import type { Agent } from '../services/agent';

// State
const agents = ref<Agent[]>([]);
const selectedAgent = ref<Agent | null>(null);
const loading = ref(true);
const error = ref('');
const isSubmitting = ref(false);

// Modals
const showCreateAgentModal = ref(false);
const showCreateKeyModal = ref(false);

const newlyGeneratedKey = ref('');

// Forms
const agentForm = ref({ name: '', description: '' });
const keyForm = ref({ scope: 'all', expirationDays: '30' });

// Fetch Data
const fetchAgents = async () => {
  loading.value = true;
  error.value = '';
  try {
    agents.value = await AgentService.getAgents();
    if (selectedAgent.value) {
      // Update selected agent if it exists
      selectedAgent.value = agents.value.find((a: Agent) => a.id === selectedAgent.value?.id) || null;
    }
  } catch (err: any) {
    error.value = err.response?.data?.detail || 'Failed to load agents';
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchAgents();
});

// Actions
const selectAgent = (agent: Agent) => {
  selectedAgent.value = agent;
  newlyGeneratedKey.value = ''; // Clear new key alert when switching
};

const handleCreateAgent = async () => {
  isSubmitting.value = true;
  try {
    const newAgent = await AgentService.createAgent(agentForm.value);
    await fetchAgents();
    selectAgent(newAgent);
    showCreateAgentModal.value = false;
    agentForm.value = { name: '', description: '' };
  } catch (err) {
    alert('Failed to create agent');
  } finally {
    isSubmitting.value = false;
  }
};

const deleteAgent = async (id: number) => {
  if (!confirm('Are you sure you want to delete this agent? All keys and history will be lost.')) return;
  try {
    await AgentService.deleteAgent(id);
    selectedAgent.value = null;
    await fetchAgents();
  } catch (err) {
    alert('Failed to delete agent');
  }
};

const handleGenerateKey = async () => {
  if (!selectedAgent.value?.id) return;
  isSubmitting.value = true;
  newlyGeneratedKey.value = '';
  
  try {
    // Calculate expiration date
    const expiresAt = new Date();
    expiresAt.setDate(expiresAt.getDate() + parseInt(keyForm.value.expirationDays));
    
    const res = await AgentService.createApiKey({
      agent: selectedAgent.value.id,
      scope: keyForm.value.scope,
      expires_at: expiresAt.toISOString(),
    });
    
    newlyGeneratedKey.value = res.key || '';
    showCreateKeyModal.value = false;
    await fetchAgents(); // Refresh tables
  } catch (err) {
    alert('Failed to generate key');
  } finally {
    isSubmitting.value = false;
  }
};

const revokeKey = async (id: number) => {
  if (!confirm('Revoke this API Key immediately? Systems using it will fail.')) return;
  try {
    await AgentService.deleteApiKey(id);
    await fetchAgents();
  } catch (err) {
    alert('Failed to revoke key');
  }
};

const copyToClipboard = (text: string) => {
  navigator.clipboard.writeText(text);
  alert('Key copied to clipboard!');
};

// Utils
const formatDate = (ds: string) => new Date(ds).toLocaleDateString();
const formatTimeAgo = (ds: string) => {
  const diffHours = (new Date().getTime() - new Date(ds).getTime()) / 1000 / 60 / 60;
  if (diffHours < 1) return 'Just now';
  if (diffHours < 24) return `${Math.floor(diffHours)} hours ago`;
  return `${Math.floor(diffHours/24)} days ago`;
};

const getScopeLabel = (scope: string) => {
  const map: Record<string, string> = {
    'all': 'Read / Write',
    'read_only': 'Read Only',
    'comment_only': 'Comment Only'
  };
  return map[scope] || scope;
};

const getScopeBadgeClass = (scope: string) => {
  return scope === 'read_only' ? 'badge--blue' : 'badge--green';
};

</script>

<style scoped>
.agent-settings {
  max-width: 1200px;
  margin: 0 auto;
}

.content-grid {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 1.5rem;
  align-items: start;
}

.card {
  background: var(--wayfs-surface);
  border-radius: 0.75rem;
  border: 1px solid var(--wayfs-border);
  padding: 1.5rem;
}

:global(.dark) .card {
  background: var(--color-dark-surface);
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.panel-header h2 {
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0;
}

.agents-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.agent-item {
  padding: 1rem;
  border: 1px solid var(--wayfs-border);
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s;
}

.agent-item:hover {
  border-color: #10B860;
}

.agent-item--active {
  border-color: #10B860;
  background: rgba(16, 184, 96, 0.05);
}

.agent-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.agent-icon {
  font-size: 1.5rem;
}

.agent-info h3 {
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
}

.new-key-alert {
  background: rgba(255, 0, 0, 0.05);
  border: 1px solid rgba(255, 0, 0, 0.2);
  padding: 1rem;
  border-radius: 0.5rem;
  margin-bottom: 1.5rem;
}

.table th {
  text-align: left;
  padding: 0.5rem;
  border-bottom: 2px solid var(--wayfs-border);
  color: var(--wayfs-text-secondary);
  font-weight: 600;
}

.table td {
  padding: 0.75rem 0.5rem;
  border-bottom: 1px solid var(--wayfs-border);
}

.badge {
  padding: 0.2rem 0.5rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 600;
}

.badge--green { background: rgba(16, 184, 96, 0.1); color: #10B860; }
.badge--blue { background: rgba(59, 130, 246, 0.1); color: #3B82F6; }

/* Timeline Setup */
.activity-timeline {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 1rem;
  padding-left: 0.5rem;
  border-left: 2px solid var(--wayfs-border);
}

.activity-item {
  position: relative;
  padding-left: 1.5rem;
}

.activity-dot {
  position: absolute;
  left: -20px;
  top: 4px;
  width: 10px;
  height: 10px;
  background: #10B860;
  border-radius: 50%;
  border: 2px solid var(--wayfs-surface);
}

.activity-desc {
  margin: 0;
  font-size: 0.95rem;
}

.activity-time {
  font-size: 0.8rem;
  color: var(--wayfs-text-secondary);
}

/* Modal Simple Styles */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100;
}

.modal {
  background: var(--wayfs-surface);
  padding: 2rem;
  border-radius: 0.75rem;
  width: 100%;
  max-width: 400px;
}

:global(.dark) .modal {
  background: var(--color-dark-surface);
  border: 1px solid var(--wayfs-border);
}

.modal h2 {
  margin-top: 0;
  margin-bottom: 1.5rem;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 0.75rem;
}

.help-text {
  font-size: 0.75rem;
  color: var(--wayfs-text-secondary);
  margin-top: 0.25rem;
}
</style>
