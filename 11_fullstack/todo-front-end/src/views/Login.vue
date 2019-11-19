<template>
  <div class="login">
      <h1>로그인 페이지 입니다.</h1>
      <LoginForm />  <!-- self-closing 으로 써도 똑같이 동작한다 -->
  </div>
</template>

<script>
import LoginForm from '../components/LoginForm';

export default {
    name: 'Login',
    components: {
      LoginForm,
    }
}
</script>

<style>

</style>