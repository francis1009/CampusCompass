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
      path: '/indivschool/:searchID',
      name: 'indivschool',
      component: () => import('../views/indivschview.vue'),
      props: true 
    },
    {
      path: '/recommended',
      name: 'recommended',
      component: () => import('../views/Recommended.vue')
    },
    {
      path: '/search',
      name: 'search',
      component: () => import('../views/SearchView.vue')
    }
  ]
})

export default router
