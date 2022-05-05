<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-aside width="20%">
        <PTTE/>
      </el-aside>
      <el-container>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/CollegeOverview'}">学院概况</el-breadcrumb-item>
          <el-breadcrumb-item>师资队伍</el-breadcrumb-item>
          <el-breadcrumb-item>研究生导师</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header>
          <p>研究生导师</p>
        </el-header>
        <el-main>
          <div class="news-list">
            <el-table :data="teachersList.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%"
                      @cell-click="changetodetail">
              <el-table-column prop="name" label="名字" width="200px"/>
              <el-table-column prop="job_title" label="职称" width="200px"/>
              <el-table-column prop="degree" label="学历" width="200px"/>
            </el-table>
          </div>
          <div class="paginationbox">
            <el-pagination
                v-model:currentPage="currentPage"
                :page-sizes="[10, 20, 30, 40]"
                :page-size="pageSize"
                layout="total, prev, pager, next, jumper"
                :total="totalPages"
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
  mounted() {
    this.getList()
  },
  data() {
    return {
      teachersList: '',
      totalPages: 0,
      pageSize: 10,
      currentPage: 1,
    }
  },
  methods: {
    getList() {
      axios
          .get('/api//teachers/teacher')
          .then(response => {
            this.totalPages = response.data.count,
                (this.teachersList = response.data.results)
            if (response.data.next !== null) {
              this.getData(response.data.next.charAt(response.data.next.length - 1))
            }
          })

    },
    getData(number) {
      axios.get('api/teachers/teacher', {params: {page: number}})
          .then(
              response => {
                this.teachersList= this.teachersList.concat(response.data.results)
                if (response.data.next !== null) {
                  this.getData(response.data.next.charAt(response.data.next.length - 1))
                }
              }
          )
    },
    handleSizeChange(val) {
      // console.log(`每页 ${val} 条`);
      this.pageSize = val;
    },
    handleCurrentChange(val) {
      // console.log(`当前页: ${val}`);
      this.currentPage = val;
    },
    formatted_time: function (row, column) {
      const date = new Date(row[column.property]);
      // return date.toLocaleDateString()
      return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate() + ' ' + date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds()
    },
    changetodetail(row) {
      this.$router.push({name: 'TeacherDetail', params: {id: row.id}})
    },
  }
}
</script>

<style scoped>
@import "~@/styles/body.css";
</style>
