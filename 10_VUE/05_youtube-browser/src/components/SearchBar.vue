<template>
    <div>
        <!-- method 는 내가 인자를 추가로 넘긴다면 () 붙이고, -->
        <!-- 그게 아니라면 () 없음 -->
        <!-- 함수를 실행하는게 아니라, 함수를 넘긴다 > 알아서 일어남 -->
        <!-- <input v-on:input="onInput" type="text"> -->
        <!-- <input @input="onInput" type="text"> -->
        <input @keypress.enter="onInput" type="text">
    </div>
</template>

<script>
export default {
    name: 'SearchBar',
    methods: {
        onInput (e) {
            // console.log(e.target.value);
            // console.log(e.data);  > 추가되는 데이터만 보여준다.
            // this.$emit('Event 이름', 전송할 값)  > 자식 컴포넌트에서 부모 컴포넌트에게 데이터를 올려보낼 때 사용한다.
            // 데이터 = 값, 정보
            this.$emit('inputChange', e.target.value);
        }
    },
}
</script>

<style scoped>
/* scoped: 해당 컴포넌트의 태그들만 영향을 받는다. */
    input {
        width: 75%;
    }

    div {
        text-align: center;
        margin: 20px;
    }
</style>