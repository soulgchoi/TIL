import Vuex from 'vuex';
import Vue from 'vue';
import auth from './modules/auth';

Vue.use(Vuex);  // Vue 에 Vuex 라는 middleware 등록 (settings.py 등록하듯이)

const store = new Vuex.Store({
    modules: {
        auth,
    }
}) 
export default store;