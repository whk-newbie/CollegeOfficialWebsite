<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-aside width="20%">
        <el-col>
          <el-row>
            <el-button type="info" @click="$router.push('/research/research')">科研动态</el-button>
          </el-row>
          <el-row>
            <el-button type="info" @click="$router.push('/research/institutions')">科研机构</el-button>
          </el-row>
          <el-row>
            <el-button type="info" @click="$router.push('/research/achievement')">科研成果</el-button>
          </el-row>
        </el-col>
      </el-aside>
      <el-container>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
          <el-breadcrumb-item>科学研究</el-breadcrumb-item>
          <el-breadcrumb-item>{{ where }}</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>{{ where }}</p></el-header>
        <el-main>
          <list :url="url"/>
        </el-main>
      </el-container>
    </el-container>

  </div>
  <Footer/>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import list from "@/components/list"

export default {
  name: "research",
  components: {Header, Footer,list},
  data: function () {
    return {
      url: "/api/research/research",
      where: "科研动态",
    }
  },
  created() {
    this.change()
  },
  methods: {
    change() {
      const paths = this.$route.fullPath.split('/')[2]
      console.log(paths)
      if (paths ==="research") {
        // this.getList('/api/research/research')
        this.url = '/api/research/research'
      }
      if (paths ==="institutions") {
        // this.getList('/api/research/institutions')
        this.url = '/api/research/institutions'
        this.where = "科研机构"
      }
      if (paths === "achievement") {
        // this.getList( '/api/research/achievements')
        this.url = '/api/research/achievements'
        this.where = "科研成果"
      }
    }
  }
}
</script>

<style scoped>

@import "~@/styles/body.css";
</style>
