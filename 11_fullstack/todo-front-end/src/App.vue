<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> <!-- a 태그 대용 -->
      <span v-if="!isLoggedIn">
        <router-link to="/login">Login</router-link>
      </span>
      <span v-else>
        <a @click.prevent="logout" href="#">Logout</a>
      </span>
    </div>
    <div class="container col-6">
    <router-view/> <!-- 다른 컴포넌트를 여기에 보여주세요 -->
    </div>
  </div>
  
</template>

<script>
// vuex 의 모든 actions, getters 가져오기
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'App',
  methods: {
    ...mapGetters(['isLoggedIn']),
    ...mapActions(['logout']),
  },
}
</script>

<style>
/*
  앞으로 생길 문제 두 가지
  1. 컴포넌트마다 비슷한/같은 함수들을 정의해야함, 정리 안됨
  2. 사용자 auth 정보와 todos 목록을 컴포넌트끼리 공유하지 못함

  > Vuex(State Management System)
*/
</style>

