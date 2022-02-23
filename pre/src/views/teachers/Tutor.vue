<template>
  <Header/>
  <div class="body">
    <el-container>
      <el-aside width="20%">
        <PTTE/>
      </el-aside>
      <el-container>
        <el-header>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/CollegeOverview'}">学院概况</el-breadcrumb-item>
          <el-breadcrumb-item>师资队伍</el-breadcrumb-item>
          <el-breadcrumb-item>研究生导师</el-breadcrumb-item>
        </el-breadcrumb>
        </el-header>
        <el-main>
          <div class="news-list">
            <el-row :gutter="2">
              <el-col :span="4">导师名称</el-col>
              <el-col :span="4">职称</el-col>
              <el-col :span="4">时间</el-col>
            </el-row>
            <el-row :gutter="2" width="100%" v-for="item in teachers_info.results" :key="item.title" class="listitem">
              <el-col :span="4">{{ item.name }}</el-col>
              <el-col :span="4">{{ item.job_title}}</el-col>
              <el-col :span="4">{{ item.updated }}</el-col>
            </el-row>
          </div>
          <div class="paginationbox">
            <el-pagination
                v-model:currentPage="currentPage"
                :page-sizes="[14, 28, 42, 56]"
                :page-size="14"
                layout="total, sizes, prev, pager, next, jumper"
                :total="400"
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
            >
            </el-pagination>
          </div>
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
import axios from 'axios'
export default {
  name: "Tutor",
  components: {Header, Footer,PTTE},
  mounted()     {
    axios
        .get('api/teachers')
        .then(response =>(this.teachers_info = response.data))
  },
  data() {
    return {
      teachers_info: ''
    }
  },
  methods: {
    formatted_time: function (row, column) {
      const date = new Date(row[column.property]);
      // return date.toLocaleDateString()
      return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate() + ' ' + date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds()
    },
  }
}
</script>

<style scoped>
.body {
  margin: 2% 2% 2% 10%;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}
.el-breadcrumb {
  margin-top: 10px;
  margin-left:10px;
  height: 50px;
  font-family: 微软雅黑;
}
.el-aside {
  background-color: #92f6ce;
}
.news-list{
  width: 80%;
  height: 500px;
  padding: 0;
  margin-left: 20%;
  margin-right: 20%;
}
.paginationbox{
  margin-left: 20%;
  margin-right: 20%;
}

.paginationbox {
  position: relative;
  left: auto;
}
</style>
