<template>
  <Header/>
  <div v-if="pages!==null">
    <div class="grid-container">
      <h1 id="title">{{ pages.title }}</h1>
      <p id="subtitle">
        发布时间: {{ DetailTime(pages.create_time) }}
      </p>
      <div v-html="pages.desc_html" class="news-body"></div>
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
  name: "groupDetail",
  components: {Header, Footer},
  setup() {
    const pages = ref('')
    const route = useRoute();
    getPages('/api/group/group/', pages, route)
    return {
      pages,
      DetailTime,
    }
  },
}
</script>

<style scoped>
@import '~@/styles/DetailBody.css';
@import '~@/styles/content.css';
</style>
