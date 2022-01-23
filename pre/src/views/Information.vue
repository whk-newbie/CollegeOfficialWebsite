<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-aside width="20%">
        <el-col>
          <el-row>
            <el-button type="info" @click="$router.push('/News')">学院新闻</el-button>
          </el-row>
          <el-row>
            <el-button type="info" @click="$router.push('/ImageNews')">图片新闻</el-button>
          </el-row>
          <el-row>
            <el-button type="info" @click="$router.push('/Information')">通知公告</el-button>
          </el-row>
        </el-col>
      </el-aside>
      <el-container>

      </el-container>
    </el-container>

  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
export default {
name: "Information",
  components: {Header, Footer}
}
</script>

<style scoped>

.container {
  margin: 2% 2% 2% 10%;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}
.el-main>h3{
  font-size: 22px;
  font-family: 微软雅黑;
  margin-left: 5%;
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
  margin-top: 10px;
  margin-left: 5px;
  color: gray;
}
.el-row {
  margin-top: 10%;
  margin-left: 50%;
}

.el-button {
  margin-top: 10px;
  height: 40px;
  width: 120px;
}
</style>
