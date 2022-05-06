<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-aside width="20%">
        <el-col>
          <el-row>
            <el-button type="info" @click="$router.push('/downloadCenter/materials')">学习资料</el-button>
          </el-row>
          <el-row>
            <el-button type="info" @click="$router.push('/downloadCenter/application')">软件下载</el-button>
          </el-row>
        </el-col>
      </el-aside>
      <el-container>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
          <el-breadcrumb-item>下载中心</el-breadcrumb-item>
          <el-breadcrumb-item>{{ where }}</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>{{ where }}</p></el-header>
        <el-main>
          <list :url="url"/>
        </el-main>
      </el-container>
    </el-container>
  </div>
  <Footer/>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import list from "@/components/list"

export default {
  name: "downloadCenter",
  components: {Header, Footer,list},
  data: function () {
    return {
      url: "/api/student/Learning?category=学习资料",
      where: "学习资料",
    }
  },
  created() {
    this.change()
  },
  methods: {
    change() {
      const paths = this.$route.fullPath.split('/')[2]
      // console.log(paths)
      if (paths === "materials") {
        this.url = '/api/student/Learning?category=学习资料'
      }
      if (paths === "application") {
        this.url = '/api/student/Learning?category=软件'
        this.where = "软件下载"
      }
    }
  }
}
</script>

<style scoped>

@import "~@/styles/body.css";
</style>
