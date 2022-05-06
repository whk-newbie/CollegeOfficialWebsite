<template>
  <Header/>
  <div class="container">
    <el-tabs
        v-model="activeName"
        type="card"
        class="demo-tabs"
        @tab-click="handleClick"
    >
      <el-tab-pane label="党史学习教育文件" name="first">
        <list :url="url1"></list>
      </el-tab-pane>
      <el-tab-pane label="党史学习教育动态" name="second">
        <list :url="url2"></list>
      </el-tab-pane>
      <el-tab-pane label="党史学习教育活动意见征集" name="third">
          意见
      </el-tab-pane>
    </el-tabs>
  </div>
  <Footer/>

</template>

<script>
import Header from "@/components/Header"
import Footer from "@/components/Footer"
import list from '@/components/list'

export default {
  name: "PartyLearning",
  components: {Header, Footer,list},
  data() {
    return {
      activeName: "first",
      url1: "/api/party/fileandtrends?category=教育文件",
      url2: '/api/party/fileandtrends?category=学习动态"'
    }
  },
  methods: {
    handleClick(tab) {
      console.log(tab.props.name)
      // if (names === "second"){
      //   Pass
      // }
    }
  }
}
</script>

<style scoped>
@import "~@/styles/body.css";
</style>
