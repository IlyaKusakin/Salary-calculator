import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Main from '../views/Main.vue'
import MainPage from '../components/MainPage.vue'
import About from '../components/About.vue'
import Contacts from '../components/Contacts.vue'


Vue.use(VueRouter)

  const routes = [
    {
      path:'/login',
      name: 'Login',
      component: Login
  },
  {
      path:'/register',
      name: 'Register',
      component: Register
  },
  {
      path:'/',
      name: 'Main',
      component: Main,
      children:[
        {
            path:'',
            component: MainPage
        },
        {
            path:'about',
            component: About,  
        },
        {
          path:'contacts',
          component: Contacts,  
      },
      ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
