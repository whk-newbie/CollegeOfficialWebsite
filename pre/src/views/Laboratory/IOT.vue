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
          <el-breadcrumb-item>物联网实验室</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>物联网实验室</p></el-header>
        <el-main>
          <p>&nbsp;&nbsp;&nbsp;&nbsp;创建于2013年的物联网实验室一期已购置17套实验箱及3G频谱分析仪等设备，
            能够满足30人的物联网卓越人才班的相关课程实验，学院已经投入100余万元经费用于完善物联网实验设备，主要
            提供传感器网络、RFID、zigbee协议、智能家居、大数据处理等方面的实验课程，并与大唐电信、中科院云计算
            中心、中科曙光等高层次企业及科研单位开展多方面合作，力争将此实验室建成国内领先水平，为学院新设专业创
            造一个优良的实验教学环境。</p>
          <img src="https://jsjxy.jxnu.edu.cn/_upload/article/images/eb/a7/e4ae55e2414d899107907088b9c7/8b56b94b-d320-42a5-ba2f-545419b80ffe.jpg" alt="">
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
  name: "IOT",
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
