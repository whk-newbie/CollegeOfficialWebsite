<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-aside width="20%">
        <el-col>
          <el-row>
            <el-button type="info" @click="$router.push('/group/news')">团学工作</el-button>
          </el-row>
          <el-row>
            <el-button type="info" @click="$router.push('/group/qnzs')">青年之声</el-button>
          </el-row>
          <el-row>
            <el-button type="info" @click="$router.push('/group/group')">团学组织</el-button>
          </el-row>
          <el-row>
            <el-button type="info" @click="$router.push('/group/service')">党员服务</el-button>
          </el-row>
          <el-row>
            <el-button type="info" @click="$router.push('/group/management')">管理制度</el-button>
          </el-row>
          <el-row>
            <el-button type="info" @click="$router.push('/group/honor')">荣誉室</el-button>
          </el-row>
        </el-col>
      </el-aside>
      <el-container>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
          <el-breadcrumb-item>团学工作</el-breadcrumb-item>
          <el-breadcrumb-item>{{ where }}</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>{{ where }}</p></el-header>
        <el-main>

          <list :url="url"></list>
        </el-main>
      </el-container>
    </el-container>

  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header"
import Footer from "@/components/Footer"
import list from "@/components/list"

export default {
  name: "GroupNews",
  components: {Header, Footer, list},
  data: function () {
    return {
      url: "/api/group/groupnews",
    }
  },
  created() {
    this.change()
  },
  methods: {
    change() {
      const paths = this.$route.fullPath.split('/')[2]
      // console.log(paths)
      if (paths === "news") {
        this.url = "/api/group/groupnews"
      }
      if (paths === "group") {
        this.url = '/api/group/group'
        this.where = "团学组织"
      }
      if (paths === "service") {
        this.url = '/api/group/party'
        this.where = "党员服务"
      }
      if (paths === "management") {
        this.url = '/api/group/manage'
        this.where = "管理制度"
      }
      if (paths === "honor") {
        this.url = '/api/group/honor'
        this.where = "荣誉室"
      }
    }
  }
}
</script>

<style scoped>
@import "~@/styles/body.css";
</style>
