<template>
  <Header/>
  <div class="container">
    <el-tabs
        v-model="activeName"
        type="card"
    >
      <el-tab-pane label="活动报道" name="first">
        <list :url="url1"></list>
      </el-tab-pane>
      <el-tab-pane label="通知公告" name="second">
        <list :url="url2"></list>
      </el-tab-pane>
      <el-tab-pane label="文件学习" name="third">
        <list :url="url3"></list>
      </el-tab-pane>
      <el-tab-pane label="意见征集" name="forth">
        意见
      </el-tab-pane>
    </el-tabs>
  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header"
import Footer from "@/components/Footer"
import list from "@/components/list"

export default {
  name: "ThematicEducation",
  components: {Header, list, Footer},
  data() {
    return {
      activeName: "first",
      url1: "/api/education/report",
      url2: "/api/education/infos",
      url3: "/api/education/filelearn"
    }
  }
}
</script>

<style scoped>
@import "~@/styles/body.css";
</style>
