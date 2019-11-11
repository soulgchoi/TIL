<template>
    <li @click="onVideoClick" class="list-group-item">
        <img :src="thubmnailUrl" class="mr-3" :alt="video.snippet.title">
        <div class="media-body">
            <span v-html="video.snippet.title"></span>
        </div>
    </li>
</template>

<script>
export default {
    name: 'VideoListItem',
    props: {
        video: Object,
    },
    methods: {
        onVideoClick () {
            this.$emit('videoSelect', this.video)
            // video 객체를 부모 컴포넌트인 VideoList 에 올려보낸다.
        }
    },
    computed: {
        thubmnailUrl () {
            return this.video.snippet.thumbnails.default.url
        }
    },
}
</script>

<style scoped>
    li {
        display: flex;
        cursor: pointer;
    }

    li:hover {
        background-color: #eee;
    }
</style>