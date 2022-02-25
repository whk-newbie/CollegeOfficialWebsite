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
          <el-breadcrumb-item>中心概况</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>中心概况</p></el-header>
        <el-main>
          <p>&nbsp;&nbsp;&nbsp;&nbsp;1985年5月学校成立计算机科学系，同时创建了计
            算机实验室， 当时建设了软件实验室和硬件实验室。此后对软件实验室和硬件实验室进行了多次更新和扩充。
            2003年成立计算机信息工程学院 （含大学信息技术教学部），组建了计算机实验教学中心，新建了网络工程
            及信息安全实验室和学生创新实验室，扩建了软件实验室和硬件实验室。 2007年获批江西高校实验教学示范
            中心。2010年新建了嵌入式实验室。2013年新建了物联网实验室。</p>
          <p>&nbsp;&nbsp;&nbsp;&nbsp;实验教学中心依托计算机信息工程学院，面向全校，
            辐射社会，开展实验教学、实训和技术服务。实验教学中心现有软件综合实验室、硬件实验室、网络工程及信息
            安全实验室、学生创新实验室、嵌入式实验室、物联网实验室。承担了计算机科学与技术、网络工程、物联网工
            程三个本科专业1200余名学生的48门专业课程的实验教学任务，以及全校计算机相关专业学院学生选修相关计
            算机专业课程的实验教学任务。同时，积极面向省内各高校和社会单位提供技术培训和咨询服务。</p>
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
  name: "LaboratoryOverView",
  components: {Header, laboratory, Footer},
}
</script>

<style scoped>
.container {
  margin: 2% 2% 2% 10%;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}
.el-main {
  height: 600px;
}
.el-main > p {
  font-size: 22px;
  font-family: 仿宋_GB2312;
  margin-left: 5%;
  margin-right: 5%;
  margin-top: 5px;
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
