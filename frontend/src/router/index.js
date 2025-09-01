import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import FireballDashboard from '@/views/FireballDashboard.vue'
import CADDashboard from '@/views/CADDashboard.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/fireballs',
    name: 'fireballs',
    component: FireballDashboard
  },
  {
    path: '/CAD',
    name: 'CAD',
    component: CADDashboard
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('@/views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
