import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 5173,
    watch: {
      usePolling: true
    }
  },
  // Explicitly define the entry point
  resolve: {
    alias: {
      '@': '/src'
    }
  },
  // Specify the entry point
  build: {
    rollupOptions: {
      input: {
        main: './index.html'  // Adjust this path if your index.html is in a different location
      }
    }
  }
})
