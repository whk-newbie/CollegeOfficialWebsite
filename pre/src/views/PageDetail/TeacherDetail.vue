<template>
  <Header/>
  <div v-if="pages!==null">
    <div class="grid-container">
      <h1 id="title">{{ pages.name }}({{ pages.job_title }}{{ pages.position }})</h1>
      <p id="subtitle">
        发布时间: {{ DetailTime(pages.updated) }}
      </p>
      <h3>个人简介</h3>
      <div v-if="pages.photo"><img :src="pages.photo" alt=""></div>
      <div v-html="pages.personal_profile_html" class="news-body"></div>
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
  name: "TeacherDetail",
  components: {Header, Footer},
  setup() {
    const pages = ref('')
    const route = useRoute();
    getPages('/api/teachers/teacher/', pages, route)
    return {
      pages,
      DetailTime
    }
  },
}
</script>
<style scoped>

@import '~@/styles/DetailBody.css';
@import '~@/styles/content.css';
h3 {
  margin-top: 5%;
  text-align: center;
  font-size: large;
}
</style>


