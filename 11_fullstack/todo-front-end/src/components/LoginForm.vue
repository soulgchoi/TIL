<template>
    <div class="login-form">
        <div v-if="isLoading" class="spinner-border" role="status">
            <span class="sr-only">Loading</span>
        </div>
        <!-- submit 의 기본동작 말고 login 을 하겠다는 의미 -->
        <form v-else class="login-input" @submit.prevent="login">
            <div v-if="errors.length" class="error-list alert alert-danger">
                <h4>아래의 오류를 해결해주세요.</h4>
                <ul>
                    <li v-for="(error, idx) in errors" :key="idx">
                        {{ error }}
                    </li>
                </ul>
            </div>
            <div class="form-group">
                <label for="username">ID</label>
                <input v-model="credentials.username" type="text" class="form-control" id="username"
                    placeholder="아이디를 입력해주세요">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input v-model="credentials.password" type="password" class="form-control" id="password"
                    placeholder="비밀번호를 입력해주세요">
            </div>
            <button class="btn btn-primary">로그인</button>
        </form>
    </div>
</template>

<script>
    import router from '../router'  // '../router/index.js'
    const axios = require('axios');
    export default {
        name: 'LoginForm',
        data() {
            return {
                credentials: {  // 1. id/password 에 해당하는 data
                    username: '',
                    password: '',
                }, 
                isAuthenticated: false, // 인증 여부
                isLoading: false,
                errors: [],
            }
        },
        methods: {
            login() {
                this.isLoading = true;
                if (this.checkUserInput()) {
                    // console.log('django 서버로 데이터를 보냅니다.')
                    // axios.get('http://localhost:8000', this.credentials)
                    // 아래부터 장고에서 jwt rest framework 와 연결
                    axios.post('http://localhost:8000/api-token-auth/', this.credentials)
                        // .then(res => console.log(res))
                        .then(res => {
                            this.isLoading = false;
                            // console.log(res.data.token)  // token 만 뽑아서 받아옴 > 이걸로 django 에 보낼 것
                            // window.sessionStorage.setItem() 은 귀찮으니까 vue-session 을 쓰는 것
                            this.$session.start();  // sessionStorage.session-id: sess: + Date.now()
                            this.$session.set('jwt', res.data.token);
                            // dispatch => action 실행하는 메서드
                            // 어떤 컴포넌트에 있어도 token 에 접근할 수 있도록
                            this.$store.dispatch('login', res.data.token);
                            router.push('/')  // vue 에서의 redirect (실제 새로고침은 일어나지 않음)
                        })
                        .catch(err => {
                            if (!err.response) {  // no response
                                this.errors.push('Network Error...');
                            } else if (err.response.status === 400) {
                                this.errors.push('Invalid username or password');
                            } else if (err.response.status === 500) {
                                this.errors.push('Internal Server error. Please try again');
                            } else {
                                this.errors.push('Some error occured');
                            }
                            this.isLoading = false;
                        })
                } else {
                    // console.log('검증실패. 다시 작성하세요')
                    this.isLoading = false;
                }
                
            },
            checkUserInput () {
                this.errors = [];
                if (!this.credentials.username) this.errors.push("username 을 입력하세요.");
                if (this.credentials.password.length < 8) this.errors.push("password 는 8 자 이상이어야 합니다.");
                if (!this.errors.length) return true;
            }
        }
    }
</script>

<style>

</style>