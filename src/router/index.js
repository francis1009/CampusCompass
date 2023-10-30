import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/test',
      name: 'test',
      component: () => import('../views/TestView.vue')
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
    },
    {
      path: '/compare',
      name: 'compare',
      component: () => import('../views/ComparisonView.vue')
    }
  ]
})

export default router
