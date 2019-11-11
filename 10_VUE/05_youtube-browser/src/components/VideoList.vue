<template>
    <ul class="col-lg-4 list-group">
        <VideoListItem
            v-for="video in videos"
            :key="video.etag"
            :video="video"
            @videoSelect="onVideoSelect"
        >  <!-- for 문 으로 나온 video 를 props -->
        </VideoListItem>
    </ul>
    
    <!-- <li v-for="video in videos" :key="video.etag">
        etag 가 유일무이한 값인것 같으니 etag 로 접근
        {{ video.snippet.title }}</li>
        이걸 이제 VideoListItem 에서 할거임 -->
</template>

<script>
import VideoListItem from './VideoListItem';

export default {
    name: 'VideoList',
    // props 1. props 가 넘어온다고 명시한다.
    // 여러 개가 넘어올 수 있으므로 [] 로 썼다.
    // props 는 data 와 똑같이 쓸 수 있다. > props = 물려받은 data > 그냥 바로 쓴다. (data 파트 필요 X)
    // props: ['videos'], 배열로 써도 되지만,
    props: {  // 객체를 매우 권장
        videos: Array,  // Validations, videos 가 Array 이냐 먼저 확인
    },
    // data() { return { videos: this.videos }}  쓰면 안됨
    components: {
        VideoListItem,
    },
    methods: {
        // videoSelect 가 오면 실행할 함수
        onVideoSelect (video) {
            this.$emit('videoSelect', video)
        }
    },
}
</script>

<style>
    
</style>