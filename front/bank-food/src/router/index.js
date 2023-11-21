import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MapView from '../views/MapView.vue'
import MyPage from '../views/MyPage.vue'
import Compare from '../views/Compare.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/mypage',
      name: 'mypage',
      component : MyPage,
    },
    {
      path: '/compare',
      name: 'compare',
      component : Compare,
    }
    
  ]
})

export default router
