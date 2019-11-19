<template>
    <div class="todo-list">
        <div v-for="todo in todos" :key="todo.id" class="card">
            <div class="card-body d-flex justify-content-between">
                <span>{{ todo.title }}</span>
            </div>
        </div>
    </div>
</template>

<script>
const axios = require('axios');
/*
    1. REQ 보내기
        1) GET
        2) http://localhost:8000/api/v1/users/my_todos/
        3) REQ.Header > Authorizaion: JWT <your token here>
        4) (POST, PATCH) Body 에 내용 추가
*/
export default {
    name: 'TodoList',
    data () {
        return {
            todos: [],
        }
    },
    methods: {
        // isLoggedIn () {},
        getTodos () {
            this.$session.start()
            const token = this.$session.get('jwt');
            const options = {
                headers: {
                    Authorization: `JWT ${token}`,
                }
            }
            axios.get('http://localhost:8000/api/v1/users/my_todos/', options)
                .then(res => this.todos = res.data.todo_set)
                .catch(err => {
                    console.log(err.response)
                })
        }
    },
    created () {
        this.getTodos()
    }
}
</script>

<style>

</style>