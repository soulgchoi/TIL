<template>
  <div class="home">
    <h1>This is Home</h1>
    <TodoList/>
  </div>
</template>

<script>
  import router from '../router';
  import TodoList from '../components/TodoList';

  export default {
    name: 'home',
    components: {
      TodoList,
    },
    methods: {
      isLoggedIn() {
        this.$session.start();
        if (!this.$session.has('jwt')) {  // jwt 가 없으면 = Login 안했으면
          router.push('/login');
        }
      }
    },
    // lifesycle 관련
    created () {  // logout 이후에 어떻게 되나 확인하기
      this.isLoggedIn()
    }
  }
</script>