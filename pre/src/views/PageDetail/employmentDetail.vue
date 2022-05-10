<template>
  <Header/>
  <div v-if="pages!==null">
    <div class="grid-container">
      <h1 id="title">{{ pages.title }}</h1>
      <p id="subtitle">
        发布时间: {{ DetailTime(pages.create_time) }}
      </p>
      <div v-html="pages.description_html" class="news-body"></div>
      <div v-if="pages.file !==''" class="file-container">
        <p @click="tofile(pages.file)">{{ getName(pages.file) }}</p>
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
import {getName , tofile } from '@/composables/viewhelp'
export default {
name: "employmentDetail",
  components: {Header, Footer},
  setup() {
    const pages = ref('')
    const route = useRoute();
    getPages('/api/student/employment/', pages, route)
    return {
      pages,
      DetailTime,
      getName,
      tofile
    }
  },
}
</script>

<style scoped>
@import '~@/styles/DetailBody.css';
.file-container{
  margin-left: 10%;
  margin-right: 10%;
  padding-bottom: 5px;
  text-decoration: underline;
}
</style>

<style>
@import '~@/styles/content.css';
</style>
