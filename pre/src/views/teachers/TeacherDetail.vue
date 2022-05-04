<template>
  <Header/>
  <div v-if="news!==null">
    <div class="grid-container" v-loading="loading">
      <h1 id="title">{{ pages.name }}({{ pages.job_title }}{{ pages.position }})</h1>
      <p id="subtitle">
        发布时间: {{ formatted_time(pages.updated) }}
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
import axios from "axios";

export default {
  name: "TeacherDetail",
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
          .get('/api/teachers/teacher/' + this.$route.params.id)
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
  height: 600px;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}


#title {
  margin-top: 5%;
  text-align: center;
  font-size: x-large;
  padding-top: 20px;
}
h3 {
  margin-top: 5%;
  text-align: center;
  font-size: large;
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

