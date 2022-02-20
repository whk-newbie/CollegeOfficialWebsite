<template>
  <Header/>
  <div class="body">
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
        <el-main>

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
  name: "Enrollful",
  components: {Header, Footer, PTTE}
}
</script>

<style scoped>
.body {
  margin: 2% 2% 2% 10%;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}

.el-main > h3 {
  font-size: 22px;
  font-family: 微软雅黑;
  margin-left: 5%;
}

.el-breadcrumb {
  margin-top: 10px;
  margin-left: 10px;
  font-family: 微软雅黑;
}

.el-aside {
  background-color: #92f6ce;
}


.el-header {
  text-align: -webkit-left;
  font-size: 24px;
  font-style: normal;
  font-family: 仿宋_GB2312;
}

.el-header > p {
  margin-top: 15px;
  margin-left: 5px;
  color: gray;
}
</style>
