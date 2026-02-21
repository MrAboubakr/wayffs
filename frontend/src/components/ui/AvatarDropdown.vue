<template>
  <div class="avatar-dropdown" ref="dropdownRef">
    <button @click="toggle" class="avatar-dropdown__trigger" :aria-expanded="isOpen">
      <div class="avatar-dropdown__avatar">
        {{ initials }}
      </div>
      <span class="avatar-dropdown__name">{{ username }}</span>
      <svg class="avatar-dropdown__chevron" :class="{ 'avatar-dropdown__chevron--open': isOpen }" width="16" height="16" viewBox="0 0 16 16" fill="none">
        <path d="M4 6L8 10L12 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>

    <Transition name="dropdown">
      <div v-if="isOpen" class="avatar-dropdown__menu">
        <div class="avatar-dropdown__header">
          <div class="avatar-dropdown__avatar avatar-dropdown__avatar--lg">
            {{ initials }}
          </div>
          <div>
            <p class="avatar-dropdown__menu-name">{{ username }}</p>
            <span class="avatar-dropdown__role-badge">{{ role }}</span>
          </div>
        </div>
        <div class="avatar-dropdown__divider"></div>
        <router-link to="/profile" class="avatar-dropdown__item" @click="close">
          <span>👤</span> Profile
        </router-link>
        <router-link to="/settings" class="avatar-dropdown__item" @click="close">
          <span>⚙️</span> Settings
        </router-link>
        <div class="avatar-dropdown__divider"></div>
        <button @click="handleLogout" class="avatar-dropdown__item avatar-dropdown__item--danger">
          <span>🚪</span> Logout
        </button>
      </div>
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount } from 'vue';
import { useAuthStore } from '../../stores/auth';

const authStore = useAuthStore();

const isOpen = ref(false);
const dropdownRef = ref<HTMLElement | null>(null);

const username = computed(() => authStore.user?.username || 'User');
const role = computed(() => authStore.user?.role || 'Member');
const initials = computed(() => {
  const name = username.value;
  return name.slice(0, 2).toUpperCase();
});

const toggle = () => { isOpen.value = !isOpen.value; };
const close = () => { isOpen.value = false; };

const handleLogout = () => {
  close();
  authStore.logout();
};

const handleClickOutside = (e: MouseEvent) => {
  if (dropdownRef.value && !dropdownRef.value.contains(e.target as Node)) {
    close();
  }
};

const handleKeydown = (e: KeyboardEvent) => {
  if (e.key === 'Escape') close();
};

onMounted(() => {
  document.addEventListener('click', handleClickOutside);
  document.addEventListener('keydown', handleKeydown);
});

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside);
  document.removeEventListener('keydown', handleKeydown);
});
</script>

<style scoped>
.avatar-dropdown {
  position: relative;
}

.avatar-dropdown__trigger {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.35rem 0.75rem;
  border-radius: 9999px;
  border: 1px solid rgba(255, 255, 255, 0.15);
  background: rgba(255, 255, 255, 0.08);
  color: #fff;
  cursor: pointer;
  transition: all 0.2s ease;
}

.avatar-dropdown__trigger:hover {
  background: rgba(255, 255, 255, 0.15);
  border-color: rgba(255, 255, 255, 0.3);
}

.avatar-dropdown__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #0D9647, #10B860);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 700;
  color: #fff;
  flex-shrink: 0;
}

.avatar-dropdown__avatar--lg {
  width: 40px;
  height: 40px;
  font-size: 0.85rem;
}

.avatar-dropdown__name {
  font-size: 0.85rem;
  font-weight: 600;
}

.avatar-dropdown__chevron {
  transition: transform 0.2s ease;
  opacity: 0.7;
}

.avatar-dropdown__chevron--open {
  transform: rotate(180deg);
}

.avatar-dropdown__menu {
  position: absolute;
  top: calc(100% + 0.5rem);
  right: 0;
  min-width: 220px;
  background: var(--wayfs-surface);
  border: 1px solid var(--wayfs-border);
  border-radius: 0.75rem;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
  padding: 0.5rem;
  z-index: 200;
}

.avatar-dropdown__header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
}

.avatar-dropdown__menu-name {
  font-weight: 700;
  font-size: 0.9rem;
  color: var(--wayfs-text);
}

.avatar-dropdown__role-badge {
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  padding: 0.1rem 0.5rem;
  border-radius: 9999px;
  background: linear-gradient(135deg, #0A7B3B, #10B860);
  color: #fff;
}

.avatar-dropdown__divider {
  height: 1px;
  background: var(--wayfs-border);
  margin: 0.25rem 0;
}

.avatar-dropdown__item {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.6rem 0.75rem;
  border-radius: 0.5rem;
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--wayfs-text);
  text-decoration: none;
  cursor: pointer;
  transition: background 0.15s ease;
  border: none;
  background: none;
  width: 100%;
  text-align: left;
}

.avatar-dropdown__item:hover {
  background: rgba(245, 184, 0, 0.1);
}

.avatar-dropdown__item--danger:hover {
  background: rgba(146, 43, 43, 0.1);
  color: #E04B1A;
}

/* Dropdown transition */
.dropdown-enter-active,
.dropdown-leave-active {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  transform-origin: top right;
}

.dropdown-enter-from,
.dropdown-leave-to {
  opacity: 0;
  transform: scale(0.95) translateY(-4px);
}
</style>
