<template>
  <div v-if="news!==null">
    <Header/>
    <div class="grid-container">
      <h1 id="title">{{ news.title }}</h1>
      <p id="subtitle">
        发布时间: {{ DetailTime(news.create_time) }}
      </p>
      <div v-html="news.body_html" class="news-body"></div>
    </div>
  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import DetailTime from "@/composables/DetailTime";
import getPages from "@/composables/GetPageData";
import {ref} from 'vue'
import {useRoute} from 'vue-router'


export default {
  name: "NewsDetail",
  components: {Header, Footer},
  setup() {
    const news = ref('')
    const route = useRoute();
    getPages('/api/news/', news, route)
    return {
      news,
      DetailTime
    }
  }
}
</script>

<style scoped>

@import '~@/styles/DetailBody.css';
</style>

<style>
@import '~@/styles/content.css';
</style>
