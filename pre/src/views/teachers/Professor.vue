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
          <el-breadcrumb-item>教授队伍</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>教授队伍</p></el-header>
        <el-main>
          <h3>王明文,李云清,谢旭升,杨印根,杨庆红,周琪云,</h3>
          <h3>刘超,叶继华,万剑怡,程艳,石海鹤,揭安全,</h3>
          <h3>王昌晶,曾雪强,马勇,钟茂生,李茂西,江爱文</h3>
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

export default {
  name: "Professor",
  components: {Header, Footer, PTTE}
}
</script>

<style scoped>
@import "~@/styles/body.css";
</style>
