<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-aside width="20%">
        <laboratory/>
      </el-aside>
      <el-container>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/CollegeOverview'}">实验中心</el-breadcrumb-item>
          <el-breadcrumb-item>嵌入式实验室</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>嵌入式实验室</p></el-header>
        <el-main>
          <p>&nbsp;&nbsp;&nbsp;&nbsp;学院嵌入式实验室，能够为学生提供基于ARM9、ARM10、Cortex-A8，WINCE6、
            安卓2.3、安卓4.0等多平台的嵌入式实验，还拥有30套可提供主流手机应用开发平台的3G实验箱，能够满足嵌入式
            课程实验、学生课外创新，部分嵌入式产品设计研发的实验要求。</p>
          <img
              src="https://jsjxy.jxnu.edu.cn/_upload/article/images/8f/6f/35ea30e240b5aa793eedb6d12424/a2a8aca7-0b98-4ba7-b6cb-5472873691b2.jpg"
              alt="">
        </el-main>
      </el-container>
    </el-container>
  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import laboratory from "@/components/laboratory"

export default {
  name: "Embedded",
  components: {Header, laboratory, Footer},
}
</script>

<style scoped>
.container {
  margin: 2% 2% 2% 10%;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}

.el-main > p {
  font-size: 22px;
  font-family: 仿宋_GB2312;
  margin-left: 5%;
  margin-right: 5%;
  margin-top: 5px;
}

.el-main > img {
  margin-left: 5%;
  margin-right: 5%;
  width: 90%;
  height: 500px;
}

.el-breadcrumb {
  margin-top: 10px;
  margin-left: 10px;
  font-family: 华文仿宋;
}

.el-aside {
  background-color: #92f6ce;
}

.el-header {
  text-align: -webkit-left;
  font-size: 24px;
  font-style: normal;
  font-family: 微软雅黑;
}

.el-header > p {
  margin-top: 15px;
  margin-left: 45%;
  color: gray;
}
</style>
