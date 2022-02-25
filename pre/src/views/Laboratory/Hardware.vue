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
          <el-breadcrumb-item>硬件实验室</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>硬件实验室</p></el-header>
        <el-main>
          <p>&nbsp;&nbsp;&nbsp;&nbsp;创建于上世纪80年代的硬件实验室于2012年、2013年分两期更新了全部硬件实验设备
            ，拥有微机组成原理实验箱、数字电路实验箱、32位单片机实验箱各60台套及相关配套仪器仪表，2015年实验室又购买电
            子电路实验箱15套，目前硬件实验室能够为硬件相关课程如汇编语言、微机原理、系统结构、单片机、数字电路，电子电路
            等提供多方面的实验支撑。为方便老师教学及学生学习，实验室新安装了投影仪和60台计算机配合教学。在新教学环境支持
            下，实验室正抓紧筹备虚拟教学系统，拟购进多种虚拟实验软件，更大限度的满足教师和学生的教学与学习需求。</p>
          <img src="https://jsjxy.jxnu.edu.cn/_upload/article/images/45/a0/3f091cc948ccb1e4f01b47145119/4ee59b70-ff89-4755-bd23-5cefbf9e2031.jpg" alt="">
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
  name: "Hardware",
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
