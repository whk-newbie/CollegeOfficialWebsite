<template>
  <Header/>
  <div v-if="news!==null">
    <div class="grid-container" v-loading="loading">
      <h1 id="title">{{ pages.title }}</h1>
      <p id="subtitle">
        发布时间: {{ formatted_time(pages.created) }}
      </p>
      <div v-html="pages.content_html" class="news-body"></div>
    </div>
  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import axios from "axios";

export default {
  name: "TmoralityDetail",
  components: {Header, Footer},
  data: function () {
    return {
      loading: false,
      pages: '',
    }
  },
  mounted() {
    this.loading = true;
    this.getData()
  },
  methods: {
    getData() {
      axios
          .get('/api/Tmorality/' + this.$route.params.id)
          .then(response => (this.pages = response.data))
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
  padding: 20px;
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
