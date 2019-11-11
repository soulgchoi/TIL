<template>
<!-- HTML 영역, div 태그 하나만 -->
    <div class="container">
        <!-- 3. template 에 보여주기 -->
        <SearchBar @inputChange="onInputChange"></SearchBar>
        <!-- v-on:자식 컴포넌트에서 emit 하는 이벤트 이름="" -->
        <div class="row">
            <VideoDetail :video="selectedVideo"></VideoDetail>

            <!-- props 0. bind 로 데이터를 넘긴다. -->
            <VideoList
                :videos="videos"
                @videoSelect="onVideoSelect"
            >
            </VideoList>
            <!-- v-bind: 줄여서 : | v-bind 가 붙은 후 더 이상 HTML 속성이 아니고 vue 에 속하는 것 -->
        </div>
    </div>
</template>

<script>
    // 누군가 이 파일을 import 하면 export 안의 내용을 받게 될 것이다.
    // new Vue({ 여기 부분 내용인거랑 같음 })
    // 1. import
    import SearchBar from './components/SearchBar'
    import VideoList from './components/VideoList'
    import VideoDetail from './components/VideoDetail'
    import axios from 'axios';

    const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;

    export default {
        // component 생성하면,
        // 0. 이름 적기
        name: 'App',
        // 2. 부모에게 자식 컴포넌트 등록하기
        components: {
            SearchBar,
            VideoList,
            VideoDetail,
        },
        data () {
            return {
                videos: [],
                // 시작할 때, 값이 없으면 없는대로 빈 [] 만들어야 한다.
                // 명시되어있지 않으면 vue 가 읽지 않는다.
                // 여기서는 일단 [] 만들고, 아래 method 에서 input 이 들어오면서 array 에 object 가 들어온다.
                selectedVideo: null,
            }
        },
        methods: {
            onInputChange (inputValue) {  // inputValue = SearchBar 에서 e.target.value
                // console.log(inputValue);
                axios.get('https://www.googleapis.com/youtube/v3/search', {
                    params: {
                        key: API_KEY,
                        type: 'video',
                        part: 'snippet',
                        q: inputValue,
                    }
                })
                // this. 해야 위에 있는 videos 접근 가능
                .then(res => this.videos = res.data.items)
            },
            onVideoSelect (video) {
                this.selectedVideo = video;
            }
        },
    }
</script>

<style>
</style>