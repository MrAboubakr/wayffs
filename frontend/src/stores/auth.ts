import { defineStore } from 'pinia';
import api from '../api';
import router from '../router';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: null as any | null,
        isAuthenticated: !!localStorage.getItem('access_token'),
    }),
    actions: {
        async login(credentials: { email: string; password: string }) {
            try {
                const response = await api.post('users/token/', credentials);
                const { access, refresh } = response.data;
                localStorage.setItem('access_token', access);
                localStorage.setItem('refresh_token', refresh);
                this.isAuthenticated = true;
                await this.fetchUser();
                router.push('/');
            } catch (error) {
                console.error('Login failed', error);
                throw error;
            }
        },
        async register(userData: { username: string; email: string; password: string }) {
            try {
                await api.post('users/register/', userData);
                // Auto-login after successful registration
                await this.login({ email: userData.email, password: userData.password });
            } catch (error) {
                console.error('Registration failed', error);
                throw error;
            }
        },
        async fetchUser() {
            try {
                const response = await api.get('users/me/');
                this.user = response.data;
            } catch (error) {
                console.error('Fetch user failed', error);
            }
        },
        logout() {
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            this.user = null;
            this.isAuthenticated = false;
            router.push('/login');
        },
    },
});
