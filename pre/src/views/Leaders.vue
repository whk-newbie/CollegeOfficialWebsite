<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-aside width="20%">
        <CLO/>
      </el-aside>
      <el-container>
        <el-header><p>学院领导</p></el-header>
        <el-main>
          <h3>院长：王明文</h3>
          <h3>院党委书记：胡弢</h3>
          <h3>副院长：李云清</h3>
          <h3>副院长：杨庆红</h3>
          <h3>副院长：马勇</h3>
          <h3>院党委副书记：黄清明</h3>
          <h3>副院长：江爱文</h3>
          <h3>大学信息技术教学部主任：王明文</h3>
        </el-main>
      </el-container>
    </el-container>

  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import CLO from "@/components/CLO"

export default {
  name: "Leaders",
  components: {Header, Footer, CLO}
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
</style>
