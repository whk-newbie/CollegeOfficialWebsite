<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-aside width="20%">
        <laboratory/>
      </el-aside>
      <el-container>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>当前位置: </el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/CollegeOverview'}">实验中心</el-breadcrumb-item>
          <el-breadcrumb-item>综合实验室</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>综合实验室</p></el-header>
        <el-main>
          <p>&nbsp;&nbsp;&nbsp;&nbsp;实验室使用面积700多平米，分为三个相对独立机房，拥有双核液晶台式电脑300多台，
            4核、6核服务器10余台，具有千兆光纤骨干连接，高速互联网出口。实验室还配置了多媒体视频教学系统、投影机、音响、机房管理系统、安防监
            控系统等。在此基础上学院已建设了结合服务器、桌面虚拟化的云计算中心，初步实现能够使同学们接触和运用最新的前沿计算机技术，更好的为
            本专业各方向的实验教学科研提供优质服务。</p>
          <p>&nbsp;&nbsp;&nbsp;&nbsp;本实验室开设的课程有：</p>
          <p>&nbsp;&nbsp;&nbsp;&nbsp;信息技术导论、高级语言程序设计、汇编语言、数据结构、操作系统、面向对象程序设计、
            数据库原理、编译原理及技术、C++程序设计、ACM程序设计选讲、C#程序设计、Linux操作系统、基于机器人平台的VC程序设计、数字图像处理、
            大型数据库技术、海量存储技术、 计算机辅助设计、空间数据库系统、普适计算、人工智能、软件测试、并行程序设计、多核程序设计、软件工程导论、
            算法设计与分析、数据库系统原理、JAVA语言程序设计合计27门课程。</p>
          <img src="https://jsjxy.jxnu.edu.cn/_upload/article/images/a2/4e/2b4b3ad7402a876ec0568f8a8237/8c89c2ef-1a74-46f9-a311-03f21b390b8b.jpg" alt="">
          <img src="https://jsjxy.jxnu.edu.cn/_upload/article/images/a2/4e/2b4b3ad7402a876ec0568f8a8237/a3e252d1-715a-480e-9ab4-35d563cb0d18.jpg" alt="">.
          <img src="https://jsjxy.jxnu.edu.cn/_upload/article/images/a2/4e/2b4b3ad7402a876ec0568f8a8237/4e90fa39-fe93-4578-91b2-125e9de18d4d.jpg" alt="">
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
name: "Gerneral",
  components: {Header,laboratory,Footer},
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
  margin-left:10px;
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
