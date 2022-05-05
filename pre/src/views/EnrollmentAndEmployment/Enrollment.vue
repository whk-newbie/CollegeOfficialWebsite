<template>
  <Header/>
  <div class="body">
    <el-container>
      <el-aside width="20%">
        <el-menu
            default-active="activeMenu"
            class="el-menu-vertical-demo"
            @select="handleSelect"
            :default-openeds="defaultopen"
            background-color="#92f6ce"
            unique-opened=true
        >
          <el-sub-menu index="1">
            <template #title>
              <span>本科生</span>
            </template>
            <el-menu-item index="1-1">招生</el-menu-item>
            <el-menu-item index="1-2">就业</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="2">
            <template #title>
              <span>研究生</span>
            </template>
            <el-menu-item index="2-1">招生</el-menu-item>
            <el-menu-item index="2-2">就业</el-menu-item>
          </el-sub-menu>
        </el-menu>
      </el-aside>
      <el-container>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/home' }">主页</el-breadcrumb-item>
          <el-breadcrumb-item>{{ category }}</el-breadcrumb-item>
          <el-breadcurmb-item>{{ where }}</el-breadcurmb-item>
        </el-breadcrumb>
        <el-header><p>{{ where }}</p></el-header>
        <el-main>
          <div class="news-list">
            <el-table :data="inforsList.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%"
                      @cell-click="changetodetail">
              <el-table-column prop="title" label="标题" width="600px"/>
              <el-table-column prop="create_time" label="时间" width="300px" :formatter="formatted_time"/>
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

import Header from "@/components/Header";
import Footer from "@/components/Footer";
import axios from 'axios'
import formatted_time from '@/composables/formatted_time';

export default {
  name: "Enrollment",
  components: {Header, Footer},
  created() {
    this.judge()
  },
  data() {
    return {
      inforsList: [],
      totalPages: 0,
      pageSize: 10,
      currentPage: 1,
      detail: 'majorDetail',
      category: "本科生",
      activeMenu: "1-1",
      defaultopen: ['1',],
      where: '招生',
      formatted_time
    }
  },
  methods: {
    getList(url) {
      axios
          .get(url)
          .then(response => {
            (this.totalPages = response.data.count),
                (this.inforsList = response.data.results)
            // console.log(this.newsList)
            if (response.data.next !== null) {
              this.getData(response.data.next.charAt(response.data.next.length - 1), url)
            }
          })
      this.loading = false;
    },
    getData(number, url) {
      axios.get(url, {params: {page: number}})
          .then(response => {
                this.inforsList = this.inforsList.concat(response.data.results)
                // console.log(this.newsList)
                if (response.data.next !== null) {
                  this.getData(response.data.next.charAt(response.data.next.length - 1), url)
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
    changetodetail(row) {
      this.$router.push({name: this.detail, params: {id: row.id}})
    },
    handleSelect(key) {
      if (key === '1-1') {
        this.$router.push('/graduate/enrollment')
        this.judge()
        // console.log("change sucessful")
      }
      if (key === '1-2') {
        this.$router.push('/graduate/employment')
        this.judge()
      }
      if (key === '2-1') {
        this.$router.push('/undergraduate/enrollment')
        this.judge()
      }
      if (key === '2-2') {
        this.$router.push('/undergraduate/employment')
        this.judge()
      }
    },
    judge() {
      // console.log(this.$route.fullPath)
      const paths = this.$route.fullPath.split('/')
      // console.log(paths)
      if (paths[1] === "graduate") {
        if (paths[2] === 'enrollment') {

          this.detail = "majorDetail"
          this.where = "招生"
          this.category = "本科生"
          this.activeMenu = '1-1'
          this.defaultopen = ['1',]
          this.getList('/api/student/enrollment?category=本科生')
        } else {

          this.detail = "majorDetail"
          this.where = "就业"
          this.category = "本科生"
          this.activeMenu = '1-2'
          this.defaultopen = ['1',]
          this.getList('/api/student/employment?category=本科生')
        }

      }
      if (paths[1] === "undergraduate") {

        if (paths[2] === 'enrollment') {

          this.detail = "majorDetail"
          this.where = "招生"
          this.category = "研究生"
          this.activeMenu = '2-1'
          this.defaultopen = ['2',]
          this.getList('/api/student/enrollment?category=研究生')
        } else {

          this.detail = "majorDetail"
          this.where = "就业"
          this.category = "研究生"
          this.activeMenu = '2-2'
          this.defaultopen = ['2',]
          this.getList('/api/student/employment?category=研究生')
        }
      }
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

.container {
  margin: 2% 2% 2% 10%;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}

.el-aside {
  background-color: #92f6ce;
}


.el-header {
  text-align: -webkit-left;
  font-size: 24px;
  font-style: normal;
  font-family: 仿宋_GB2312 serif;
}

.el-header > p {
  margin-top: 15px;
  margin-left: 5px;
  color: gray;
}

.el-row {
  margin-top: 10%;
  margin-left: 50%;
}

.el-button {
  margin-top: 10px;
  height: 40px;
  width: 120px;
}

.news-list {
  /*width: 100%;*/
  height: 500px;
  position: relative;
  margin-left: 5%;
  margin-right: 5%;
  padding: 0;
}

.el-breadcrumb {
  margin-top: 10px;
  margin-left: 10px;
  font-family: 华文仿宋, serif;
}

#el-table-column {
  margin-left: 20px;
  margin-right: 20px;
  width: 50%;
}

.paginationbox {
  position: relative;
  margin-left: 35%;
  margin-right: 20%;
}
</style>
