<template>
  <nav class="navbar" :class="{ 'navbar--scrolled': isScrolled }">
    <div class="navbar__inner">
      <!-- Left section -->
      <div class="navbar__left">
        <router-link :to="authStore.isAuthenticated ? '/dashboard' : '/'" class="navbar__brand">
          <img src="/images/wayffs.jpg" alt="Wayffs" class="navbar__logo" />
          <span class="navbar__brand-text">Wayffs</span>
        </router-link>

        <div class="navbar__links" :class="{ 'navbar__links--open': isMobileMenuOpen }">
          <router-link to="/" class="navbar__link" active-class="navbar__link--active" @click="closeMobile">
            Home
          </router-link>
          <template v-if="authStore.isAuthenticated">
            <router-link to="/dashboard" class="navbar__link" active-class="navbar__link--active" @click="closeMobile">
              Dashboard
            </router-link>
            <router-link to="/tasks" class="navbar__link" active-class="navbar__link--active" @click="closeMobile">
              Tasks
            </router-link>
            <router-link to="/analytics" class="navbar__link" active-class="navbar__link--active" @click="closeMobile">
              Analytics
            </router-link>
            <router-link to="/activity" class="navbar__link" active-class="navbar__link--active" @click="closeMobile">
              Activity
            </router-link>
          </template>
          <template v-if="!authStore.isAuthenticated">
            <a href="#features" class="navbar__link" @click="closeMobile">Discover</a>
            <a href="#about" class="navbar__link" @click="closeMobile">About</a>
          </template>
        </div>
      </div>

      <!-- Right section -->
      <div class="navbar__right">
        <template v-if="authStore.isAuthenticated">
          <button @click="toggleTheme" class="navbar__icon-btn" :title="isDark ? 'Light mode' : 'Dark mode'">
            {{ isDark ? '☀️' : '🌙' }}
          </button>
          <button class="navbar__icon-btn navbar__notification-btn" title="Notifications">
            🔔
            <span class="navbar__notification-dot"></span>
          </button>
          <AvatarDropdown />
        </template>
        <template v-else>
          <button @click="toggleTheme" class="navbar__icon-btn" :title="isDark ? 'Light mode' : 'Dark mode'">
            {{ isDark ? '☀️' : '🌙' }}
          </button>
          <router-link to="/login" class="navbar__auth-link">Login</router-link>
          <router-link to="/register" class="navbar__auth-btn">Register</router-link>
        </template>

        <!-- Mobile hamburger -->
        <button class="navbar__hamburger" @click="toggleMobile" :class="{ 'navbar__hamburger--open': isMobileMenuOpen }">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useAuthStore } from '../../stores/auth';
import { useTheme } from '../../composables/useTheme';
import AvatarDropdown from '../ui/AvatarDropdown.vue';

const authStore = useAuthStore();
const { isDark, toggleTheme } = useTheme();

const isScrolled = ref(false);
const isMobileMenuOpen = ref(false);

const toggleMobile = () => { isMobileMenuOpen.value = !isMobileMenuOpen.value; };
const closeMobile = () => { isMobileMenuOpen.value = false; };

const handleScroll = () => {
  isScrolled.value = window.scrollY > 10;
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true });
});

onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.75);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(13, 150, 71, 0.08);
  transition: all 0.3s ease;
}

:global(.dark) .navbar {
  background: rgba(10, 26, 15, 0.8);
  border-bottom-color: rgba(245, 184, 0, 0.1);
}

.navbar--scrolled {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

:global(.dark) .navbar--scrolled {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.navbar__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0.75rem 1.5rem;
}

.navbar__left {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.navbar__brand {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
}

.navbar__logo {
  width: 36px;
  height: 36px;
  border-radius: 0.5rem;
  object-fit: contain;
}

.navbar__brand-text {
  font-weight: 900;
  font-size: 1.35rem;
  letter-spacing: 0.04em;
  background: linear-gradient(135deg, #F5B800, #A8D400, #10B860);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.navbar__links {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.navbar__link {
  text-decoration: none;
  padding: 0.5rem 0.85rem;
  border-radius: 0.5rem;
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--wayfs-text-secondary);
  transition: all 0.2s ease;
}

.navbar__link:hover {
  color: var(--wayfs-text);
  background: rgba(13, 150, 71, 0.06);
}

:global(.dark) .navbar__link:hover {
  background: rgba(245, 184, 0, 0.08);
}

.navbar__link--active {
  color: #0D9647;
  background: rgba(13, 150, 71, 0.1);
  font-weight: 600;
}

:global(.dark) .navbar__link--active {
  color: #10B860;
  background: rgba(245, 184, 0, 0.12);
}

.navbar__right {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.navbar__icon-btn {
  width: 38px;
  height: 38px;
  border-radius: 0.5rem;
  border: 1px solid var(--wayfs-border);
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 1.1rem;
  transition: all 0.2s ease;
}

.navbar__icon-btn:hover {
  background: rgba(13, 150, 71, 0.06);
  transform: scale(1.05);
}

:global(.dark) .navbar__icon-btn:hover {
  background: rgba(245, 184, 0, 0.08);
}

.navbar__notification-btn {
  position: relative;
}

.navbar__notification-dot {
  position: absolute;
  top: 6px;
  right: 6px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #F5B800;
  border: 2px solid var(--wayfs-surface);
}

.navbar__auth-link {
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--wayfs-text);
  transition: all 0.2s ease;
}

.navbar__auth-link:hover {
  background: rgba(13, 150, 71, 0.06);
}

.navbar__auth-btn {
  text-decoration: none;
  padding: 0.5rem 1.25rem;
  border-radius: 0.5rem;
  font-size: 0.9rem;
  font-weight: 600;
  color: #fff;
  background: linear-gradient(135deg, #0D9647, #10B860);
  transition: all 0.2s ease;
  box-shadow: 0 2px 10px rgba(13, 150, 71, 0.3);
}

.navbar__auth-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 16px rgba(13, 150, 71, 0.4);
}

/* Hamburger */
.navbar__hamburger {
  display: none;
  flex-direction: column;
  gap: 4px;
  padding: 0.5rem;
  background: none;
  border: none;
  cursor: pointer;
}

.navbar__hamburger span {
  width: 20px;
  height: 2px;
  background: var(--wayfs-text);
  border-radius: 1px;
  transition: all 0.3s ease;
}

.navbar__hamburger--open span:nth-child(1) {
  transform: rotate(45deg) translate(4px, 4px);
}

.navbar__hamburger--open span:nth-child(2) {
  opacity: 0;
}

.navbar__hamburger--open span:nth-child(3) {
  transform: rotate(-45deg) translate(4px, -4px);
}

/* Mobile */
@media (max-width: 768px) {
  .navbar__links {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    flex-direction: column;
    background: var(--wayfs-surface);
    border-bottom: 1px solid var(--wayfs-border);
    padding: 1rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  }

  .navbar__links--open {
    display: flex;
  }

  .navbar__hamburger {
    display: flex;
  }

  .navbar__auth-link,
  .navbar__auth-btn {
    display: none;
  }
}
</style>
