import { createRouter, createWebHistory } from 'vue-router'
import downloadPage from "../components/downloadPage.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: downloadPage
    },
  ]
})

export default router
