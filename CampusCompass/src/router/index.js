import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/homepage.vue')
    },
    {
      path: '/indivschool',
      name: 'indivschool',
      component: () => import('../views/indivschview.vue')
    },
    {
      path: '/recommended',
      name: 'recommended',
      component: () => import('../views/Recommended.vue')
    }
  ]
})

export default router
