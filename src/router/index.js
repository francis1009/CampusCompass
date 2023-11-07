import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/index.html' // Redirect the root path to '/index.html'
    },
    {
      path: '/index.html',
      name: 'recommended',
      component: () => import('../views/Recommended.vue'),
      props: (route) => ({ schoolsList: route.query.schoolsList ? JSON.parse(route.query.schoolsList) : [] })
    },
    {
      path: '/indivschool/:searchID',
      name: 'indivschool',
      component: () => import('../views/indivschview.vue'),
      props: true 
    },
    {
      path: '/search',
      name: 'search',
      component: () => import('../views/SearchView.vue'),
      props: (route) => ({ schoolsList: route.query.schoolsList ? JSON.parse(route.query.schoolsList) : [] })
    },
    {
      path: '/compare',
      name: 'compare',
      component: () => import('../views/ComparisonView.vue')
    },
    {
      path: '/viewschools',
      name: 'viewSchools',
      component: () => import('../views/ViewAllSchools.vue')
    }
  ]
})

export default router
