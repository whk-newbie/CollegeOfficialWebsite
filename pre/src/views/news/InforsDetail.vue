<template>
  <Header/>
  <div class="grid-container" v-loading="loading">
    <div v-if="news!==null">
      <h1 id="title">{{ news.title }}</h1>
      <p id="subtitle">
        发布时间: {{ formatted_time(news.pub_time) }}
      </p>
      <div class="content_body">
        <div v-if="news.content_html">
          <div v-html="news.content_html" class="news-body"></div>
        </div>
        <div v-else-if="news.file">
          <div>文件展示</div>
<!--          <div v-if="judge">-->
<!--            <div class="pdf" v-show="fileType === 'pdf'">-->
<!--              <pdf :src="news.file"></pdf>-->
<!--            </div>-->
<!--          </div>-->
<!--          <div v-else>-->
<!--            <el-button @click="openfile">点此查看文件</el-button>-->
<!--          </div>-->
          <el-button @click="openfile">点此查看文件</el-button>
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
import axios from "axios";
// import pdf from 'vue-pdf'

export default {
  name: "InfosDetail",
  components: {Header, Footer},
  data: function () {
    return {
      loading: false,
      news: null,
      pdfstring: 'pdf'
    }
  },
  mounted() {
    this.loading = true;
    this.getData()
  },
  methods: {
    getData() {
      axios
          .get('/api/infos/' + this.$route.params.id)
          .then(response => (this.news = response.data))
      this.loading = false;
    },
    formatted_time: function (time) {
      const date = new Date(time);
      // return date.toLocaleDateString()
      return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate() + ' ' + date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds()
    },
    openfile() {
      var path = this.news.file
      window.open(path)
      // window.open("https://view.officeapps.live.com/op/view.aspx?src=" + path)
    },
    judge() {
      if (this.news.file.substring(this.news.file.length - 3) === 'pdf') {
        return true
      }
      else{
        return false
      }
    }
  }
}
</script>

<style scoped>

.grid-container {
  margin: 1% 2% 2% 10%;
  height: auto;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}


#title {
  margin-top: 5%;
  text-align: center;
  font-size: x-large;
}

#subtitle {
  text-align: center;
  color: gray;
  font-size: small;
}

.news-body {
  margin-left: 10%;
  margin-right: 10%;
}

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
.news-body p img {

  max-width: 100%;
  border-radius: 50px;
  box-shadow: gray 0 0 20px;
}

.toc ul {
  list-style-type: none;
}

.toc a {
  color: gray;
}
</style>
