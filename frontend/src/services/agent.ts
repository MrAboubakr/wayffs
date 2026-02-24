import api from '../api';

export interface Agent {
    id?: number;
    name: string;
    description?: string;
    created_at?: string;
    updated_at?: string;
    keys?: AgentAPIKey[];
    recent_actions?: AgentAction[];
}

export interface AgentAPIKey {
    id?: number;
    agent?: number;
    key?: string; // Only shown on creation / partial
    scope: string;
    expires_at: string;
    last_used?: string;
    total_actions?: number;
    is_active?: boolean;
    created_at?: string;
}

export interface AgentAction {
    id: number;
    action_type: string;
    description: string;
    timestamp: string;
}

export const AgentService = {
    // Agents
    async getAgents() {
        const response = await api.get<Agent[]>('/users/manage/agents/');
        return response.data;
    },

    async createAgent(data: { name: string; description?: string }) {
        const response = await api.post<Agent>('/users/manage/agents/', data);
        return response.data;
    },

    async updateAgent(id: number, data: Partial<Agent>) {
        const response = await api.patch<Agent>(`/users/manage/agents/${id}/`, data);
        return response.data;
    },

    async deleteAgent(id: number) {
        await api.delete(`/users/manage/agents/${id}/`);
    },

    // API Keys
    async createApiKey(data: { agent: number; scope: string; expires_at: string }) {
        const response = await api.post<AgentAPIKey>('/users/manage/keys/', data);
        return response.data;
    },

    async deleteApiKey(id: number) {
        await api.delete(`/users/manage/keys/${id}/`);
    }
};
