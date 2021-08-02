import { createRouter, createWebHistory } from 'vue-router'
// import Search from '../components/mainBody/search.vue'
// import Nav from '../components/nav/navigation.vue'
import Response from '../components/mainBody/response.vue'


const routes = [
  {
    name : 'search',
    path : '/search/:Ecode',
    component : Response
  },


]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
