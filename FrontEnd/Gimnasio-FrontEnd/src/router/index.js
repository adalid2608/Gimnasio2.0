import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/components/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    }
  ]
})

export default router
