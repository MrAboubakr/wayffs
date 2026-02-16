import { ref, watch, onMounted } from 'vue';

const isDark = ref(false);

export function useTheme() {
    const init = () => {
        const saved = localStorage.getItem('wayfs-theme');
        if (saved === 'dark') {
            isDark.value = true;
        } else if (saved === 'light') {
            isDark.value = false;
        } else {
            isDark.value = window.matchMedia('(prefers-color-scheme: dark)').matches;
        }
        applyTheme();
    };

    const applyTheme = () => {
        const root = document.documentElement;
        if (isDark.value) {
            root.classList.add('dark');
        } else {
            root.classList.remove('dark');
        }
    };

    const toggleTheme = () => {
        isDark.value = !isDark.value;
        localStorage.setItem('wayfs-theme', isDark.value ? 'dark' : 'light');
        applyTheme();
    };

    watch(isDark, applyTheme);

    onMounted(init);

    return {
        isDark,
        toggleTheme,
    };
}
