import { fileURLToPath, URL } from 'node:url'

import {
  defineConfig,
  loadEnv
} from 'vite'
import vue from '@vitejs/plugin-vue'
export default defineConfig(({
  mode
}) => {
  process.env = {
    // Fallback API URL parameter
    BASE_URL: 'https://lot37.artw.dev/',

    ...process.env,
    ...loadEnv(mode, process.cwd(), ''),
  };

  return {
    plugins: [
      vue(),
    ],
      resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    },
    server: {
      proxy: {
        '/api/': {
          target: process.env.BASE_URL,
          changeOrigin: true,
          secure: false,
        },
      }
    },
  }
})
