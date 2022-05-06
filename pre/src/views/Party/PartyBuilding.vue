<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
        <el-breadcrumb-item>党建工作</el-breadcrumb-item>
      </el-breadcrumb>
      <el-header><p>党建工作</p></el-header>
      <el-main>
        <list :url="url"></list>
      </el-main>
    </el-container>
  </div>
  <Footer/>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import list from "@/components/list.vue"
export default {
  name: "PartyBuilding",
  components: {Header, Footer, list},
  data() {
    return {
      url: "/api/party/building",
    }
  },
}
</script>

<style scoped>
@import "~@/styles/body.css";
</style>
