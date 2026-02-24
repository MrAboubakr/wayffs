import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import mdx from '@mdx-js/rollup'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    mdx({ jsxImportSource: 'vue', providerImportSource: '@mdx-js/vue' }),
    vueJsx(),
    tailwindcss(),
  ],
})

