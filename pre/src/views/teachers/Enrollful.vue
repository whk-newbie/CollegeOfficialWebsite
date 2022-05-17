<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-aside width="20%">
        <PTTE/>
      </el-aside>
      <el-container>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/CollegeOverview'}">学院概况</el-breadcrumb-item>
          <el-breadcrumb-item>师资队伍</el-breadcrumb-item>
          <el-breadcrumb-item>招贤纳士</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header>
          <p>招贤纳士</p>
        </el-header>
        <el-main>
          <list :url="url"/>
        </el-main>
      </el-container>
    </el-container>
  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header"
import Footer from "@/components/Footer"
import PTTE from "@/components/PTTE"
import list from "@/components/list"

export default {
  name: "Enrollful",
  components: {Header, Footer, PTTE,list},
  data() {
    return {
      url: "/api/teachers/recruiting",
    }
  }
}
</script>

<style scoped>
@import "~@/styles/body.css";
</style>
