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
          <el-breadcrumb-item>网络实验室</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>网络实验室</p></el-header>
        <el-main>
          <p>&nbsp;&nbsp;&nbsp;&nbsp;计算机信息工程学院计算机网络及信息安全实验室与2005年下半年正式投入使用，实验室占地面积240平米,
            主体设备是业界领先的思科路由交换设备、专业网管软件，并拥有同类院校很少能配置的福禄克网络协议分析仪、福禄克专业线缆认证测试设备
            等。实验课程引进吸收了在国际上具有广泛影响的思科网络学院课程体系和教学资源。进几年来，学院持续投入扩充了网络及信息安全设备，更
            新了一批国产主流路由交换设备等，能够满足60名同学同时开展基础实验、综合设计实验教学。</p>
          <img
              src="https://jsjxy.jxnu.edu.cn/_upload/article/images/7c/75/a633394d44d6b68db05bfbc1aefd/eb832d17-ca01-4530-b9e2-d1d381f4a001.jpg"
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
  name: "Network",
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
