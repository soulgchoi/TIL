import Vue from 'vue'
import VueRouter from 'vue-router'  // 앞에 ./ 없으면 설치된 모듈
import Home from '../views/Home.vue'  // 있으면 어느 폴더에서 가져오는 것
import Login from '../views/Login'

Vue.use(VueRouter)  // 우리 같이 일해보자. 악수. 의 개념
// import 된 Vue 와 VueRouter 가 악수함

// const routes = [
//   {
//     path: '/',
//     name: 'home',
//     component: Home
//   },
//   {
//     path: '/about',
//     name: 'about',
//     // route level code-splitting
//     // this generates a separate chunk (about.[hash].js) for this route
//     // which is lazy-loaded when the route is visited.
//     component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
//   }
// ]

const router = new VueRouter({
  mode: 'history',  // 원래의 브라우저 라우팅 방식 ( # 뒤에 있는 url 은 다 무시하기 때문에, # 없앰 )
  routes: [
      {
        path: '/',
        name: 'home',
        component: Home   // component 에 있는 vue > router 에서 보여줄 것만
      },
      {
        path: '/login',
        name: 'login',
        component: Login
      },
    ],
})

export default router
