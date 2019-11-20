// component 들의 영향을 받지 않는다.
// 인증과 관련된 모든 State 를 작성한다. 
// State 에 접근/변경하는 모든 로직은 여기로 온다.

const state = {
    token: null, // 초기 로그인 하지 않은 상태
};


const getters = {
    // Vuex 에서는 arrow function
    // 첫번째 인자는 무조건 state(객체 상태)
    isLoggedIn: state => !!state.token,  // 특정 값을 T/F 로 바꾸는 구문
};


const mutations = {
    setToken: (state, token) => state.token = token,
};

const actions = {
    // logout: (options) => {
        // mutations.setToken(state, null)  // 이렇게 하지 말 것
        // options.commit('setToken', null)  // GREAT
    // }   
    logout: ({ commit }) => {  // options 에서 commit 을 바로 꺼내서 쓴다.
        commit('setToken', null)
    },
    
    login: ({ commit }, token ) => {
        commit('setToken', token)
    }
};

export default {
    state, getters, mutations, actions
}

