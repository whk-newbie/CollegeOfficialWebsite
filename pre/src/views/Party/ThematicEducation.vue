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
        <div class="options">
          <h3>不忘初心、牢记使命”主题教育意见征集信箱</h3>

          <h4>
            书记信箱：liululinxinqiao@sina.com
          </h4>
          <h4>
            院长信箱：mwwang@jxnu.edu.cn
          </h4>
        </div>
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
      url2: "/api/education/infor",
      url3: "/api/education/filelearn"
    }
  }
}
</script>

<style scoped>
@import "~@/styles/body.css";
.options {
  margin-left: 20%;
  height: 500px;
}
</style>
