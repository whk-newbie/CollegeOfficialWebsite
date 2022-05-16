<template>
  <Header/>
  <div v-if="pages!==null">
    <div class="grid-container">
      <h1 id="title">{{ pages.title }}</h1>
      <p id="subtitle">
        发布时间: {{ DetailTime(pages.create_time) }}
      </p>
      <div v-html="pages.description_html" class="news-body"></div>
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
  name: "majorDetail",
  components: {Header, Footer},
  setup() {
    const pages = ref('')
    const route = useRoute();
    getPages('/api/student/major/', pages, route)
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
.grid-container {
  margin: 1% 2% 2% 10%;
  height: 800px;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}

</style>
