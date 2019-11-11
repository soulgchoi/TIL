// 이름은 되도록 main.js 유지하는 게 좋다 (바꿀 수는 있지만, 설정 변경해야 함)
import Vue from 'vue';
import App from './App';  // App.vue 가 아닌 이유 > 알아서 확장자 떼고 읽음  // export default 안의 내용 import 한 것

// const app = new Vue({
/*new Vue ({
    el: '#app',  // HTML 에 id app 마운트 할 것 (public/index.html 에서 id="app" 이 대상)
    // render 는 root component 에서 한번만 쓰기
    render: function (createElement) {
        return createElement(App);
    }   // 이 코드를 아래처럼 쓴다 (create vue 하면 나오는 기본값)
    render: h => h(App), // 유일하게 method 인데 arrow function
})  아래와 같이 쓴다 */
new Vue ({
    render: h => h(App),
}).$mount('#app')