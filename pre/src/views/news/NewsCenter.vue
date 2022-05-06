<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-aside width="20%">
        <el-col>
          <el-row>
            <el-button type="info" @click="$router.push('/newsAndinfos/overview')">学院新闻</el-button>
          </el-row>
          <el-row>
            <el-button type="info" @click="$router.push('/newsAndinfos/inforsCenter')">通知公告</el-button>
          </el-row>
        </el-col>
      </el-aside>
      <el-container>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/news'}">新闻中心</el-breadcrumb-item>
          <el-breadcrumb-item>学院新闻</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>学院新闻</p></el-header>
        <el-main>
          <list :url="url"/>
        </el-main>
      </el-container>
    </el-container>

  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import list from "@/components/list"

export default {
  name: "NewsCenter",
  components: {Header, Footer,list},

  data: function () {
    return {
      url: "/api/news/"
    }
  },
}
</script>

<style scoped>

@import "~@/styles/body.css";
</style>
