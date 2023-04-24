import { createRouter, createWebHistory } from 'vue-router'
import downloadPage from "../components/downloadPage.vue";
import fileDownload from "../components/fileDownload.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: downloadPage
    },
    {
      path: '/fileDownload',
      name: 'downloadFile',
      component: fileDownload
    },
  ]
})

export default router
