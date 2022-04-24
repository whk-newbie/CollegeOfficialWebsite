<template>
  <Header/>
  <div class="grid-container" v-loading="loading">
    <div v-if="news!==null">
      <h1 id="title">{{ news.title }}</h1>
      <p id="subtitle">
        发布时间: {{ formatted_time(news.create_time) }}
      </p>
      <div v-html="news.body_html" class="news-body"></div>
    </div>
  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import axios from "axios";

export default {
  name: "NewsDetail",
  components: {Header, Footer},
  data: function () {
    return {
      loading: false,
      news: null,
    }
  },
  mounted() {
    this.loading = true;
    this.getData()
  },
  methods: {
    getData() {
      axios
          .get('/api/news/' + this.$route.params.id)
          .then(response => (this.news = response.data))
        this.loading = false;
    },
    formatted_time: function (time) {
      const date = new Date(time);
      // return date.toLocaleDateString()
      return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate() + ' ' + date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds()
    },
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
