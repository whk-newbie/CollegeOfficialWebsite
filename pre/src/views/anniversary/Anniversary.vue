<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
        <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
        <el-breadcrumb-item>80周年校庆</el-breadcrumb-item>
      </el-breadcrumb>
      <el-header><p>校庆动态</p></el-header>
      <el-main>
        <list :url="url"></list>
      </el-main>
    </el-container>
  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header"
import Footer from "@/components/Footer"
import list from "@/components/list"

export default {
  name: "Anniversary",
  components: {Header, Footer,list},
  data() {
    return {
      url: '/api/anniversary'
    }
  }
}
</script>

<style scoped>

@import "~@/styles/body.css";

</style>
