<template>
  <Header/>
  <div class="grid-container" v-loading="loading">
    <div v-if="news!==null">
      <h1 id="title">{{ news.title }}</h1>
      <p id="subtitle">
        发布时间: {{ DetailTime(news.create_time) }}
      </p>
      <div class="content_body">
        <div v-if="news.content_html !== ''">
          <div v-html="news.content_html" class="news-body"></div>
        </div>
        <div v-else-if="news.file !=='' ">
          <iframe :src="news.file" width="100%" height="600px" autocapitalize="true"></iframe>
        </div>
        <div v-else>
          <el-empty description="加载失败！请联系网站管理员，点击下方按钮，返回上一页"/>
          <el-button class="back-btn" type="primary" @click="$router.go(-1)">Primary</el-button>
        </div>
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
  name: "InfosDetail",
  components: {Header, Footer},
  setup() {
    const news = ref('')
    const route = useRoute();
    getPages('/api/infos/', news, route)
    return {
      news,
      DetailTime
    }
  },
  data: function () {
    return {
      pdfstring: 'pdf',

    }
  },
}
</script>

<style scoped>

@import '~@/styles/DetailBody.css';

.content_body {
  margin-right: 5%;
  margin-left: 5%;
}

.back-btn {
  margin-right: 10%;
  margin-left: 45%;
  margin-bottom: 2%;
}
</style>

<style>
@import '~@/styles/content.css';
</style>
