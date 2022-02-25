<template>
  <Header/>
  <div class="body">
    <el-row class="tac">
      <el-col :span="6">
        <el-menu
            router
            default-active="undergraduate"
            class="el-menu-vertical-demo"
            :collapse="isCollapse"
            @open="handleOpen"
            @close="handleClose"
        >
          <el-sub-menu index="1">
            <template #title>
              <span>本科生教育</span>
            </template>
            <el-menu-item index="graduate">专业介绍</el-menu-item>
            <el-menu-item index="1-2">培养方案</el-menu-item>
            <el-menu-item index="1-3">教学成果</el-menu-item>
            <el-menu-item index="'1-4">精品课程</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="2">
            <template #title>
              <span>研究生教育</span>
            </template>
            <el-menu-item index="undergraduate">学位点介绍</el-menu-item>
            <el-menu-item index="2-2">培养方案</el-menu-item>
            <el-menu-item index="2-3">信息公告</el-menu-item>
          </el-sub-menu>
        </el-menu>
      </el-col>
      <el-col :span="24" stryle="width:100%">
      </el-col>
    </el-row>
  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";

export default {
  name: "Undergraduate",
  components: {Header, Footer},
  data() {
    return {
      activeIndex: this.$route.path,
      isCollapse: false
    }
  }
}
</script>

<style scoped>
.body {
  margin: 2% 2% 2% 10%;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}
</style>
