<template>
  <Header/>
  <div v-if="pages!==null">
    <div class="grid-container" v-loading="loading">
      <h1 id="title">{{ pages.title }}</h1>
      <p id="subtitle">
        发布时间: {{ DetailTime(pages.create_time) }}
      </p>
      <div v-if="pages.file" class="pdf-content">
        <iframe :src="pages.file" width="100%" height="800px" autocapitalize="true"></iframe>
      </div>
      <div v-else>
        <div v-html="pages.description_html" class="news-body"></div>
      </div>
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
  name: "teachingDetail",
  components: {Header, Footer},
  setup() {
    const pages = ref('')
    const route = useRoute();
    getPages('/api/student/teaching/', pages, route)
    return {
      pages,
      DetailTime,
    }
  },
}
</script>

<style scoped>

@import '~@/styles/DetailBody.css';

</style>

<style>
@import '~@/styles/content.css';
</style>


