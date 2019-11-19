import Vue from 'vue'
import App from './App.vue'
import router from './router'  // = from './router/index.js'
// router 에 담겨있는 것 = VueRouter ( 왜냐면 export router 했는데, router 는 VueRouter )
// npm i vue-session 
// 발급받은 토큰을 SessionStorage 에 저장하는걸 쉽게 해주는 플러그인(미들웨어)
import VueSession from 'vue-session'

Vue.config.productionTip = false
Vue.use(VueSession);  // Vue 에게 VueSession 이라는 Middleware 등록

new Vue({
  router,  // = router: router
  // index.js 에서 악수하고, 본격적으로 일을 시작
  render: h => h(App)
}).$mount('#app')
