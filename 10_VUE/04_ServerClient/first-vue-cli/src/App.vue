<template>
    <!-- template 안에는 반드시 단 한 개의 최상단 태그(노드) -->
    <div>
        <input type="text" v-model="input">
        <p>{{ filteredInput }}</p>
    </div>
</template>

<script>
export default {
    name: 'App',
    data: function () {
        return {
            input: 'Type something',
        }
    },
    methods: {},
    computed: {
        filteredInput: function () {
            // let string = this.input;
            // string = string.replace(/바보/g,"**")  // g > global 하게 찾는 의미, i > 대소문자 구분 X
            // return `Filtered ${string}`;
            return this.input.replace(/바보|멍청이/g, "##")
        }
    },
}
</script>

<style></style>
        
    
