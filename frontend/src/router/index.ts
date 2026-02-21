import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import('../views/HomeView.vue'),
            beforeEnter: (_to, _from, next) => {
                const authStore = useAuthStore()
                if (authStore.isAuthenticated) {
                    next({ name: 'dashboard' })
                } else {
                    next()
                }
            }
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: () => import('../views/DashboardView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/projects/:id',
            name: 'project-detail',
            component: () => import('../views/ProjectDetailView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/tasks',
            name: 'tasks',
            component: () => import('../views/TasksView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/analytics',
            name: 'analytics',
            component: () => import('../views/AnalyticsView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/activity',
            name: 'activity',
            component: () => import('../views/ActivityView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/profile',
            name: 'profile',
            component: () => import('../views/ProfileView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/settings',
            name: 'settings',
            component: () => import('../views/SettingsView.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/LoginView.vue')
        },
        {
            path: '/register',
            name: 'register',
            component: () => import('../views/RegisterView.vue')
        }
    ],
    scrollBehavior(_to, _from, savedPosition) {
        if (savedPosition) return savedPosition
        return { top: 0 }
    }
})

router.beforeEach((to, _from, next) => {
    const authStore = useAuthStore()
    if (to.meta.requiresAuth && !authStore.isAuthenticated) {
        next('/login')
    } else {
        next()
    }
})

export default router
