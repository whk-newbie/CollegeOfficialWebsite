<template>
  <Header/>
  <div class="body">
    <el-container>
      <el-aside width="20%">
        <el-menu
            default-active="activeMenu"
            class="el-menu-vertical-demo"
            @open="1"
            @select="handleSelect"
            background-color="#92f6ce"
        >
          <el-sub-menu index="1">
            <template #title>
              <span>本科生教育</span>
            </template>
            <el-menu-item index="1-1">专业介绍</el-menu-item>
            <el-menu-item index="1-2">培养方案</el-menu-item>
            <el-menu-item index="1-3">教学成果</el-menu-item>
            <el-menu-item index="'1-4">精品课程</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="2">
            <template #title>
              <span>研究生教育</span>
            </template>
            <el-menu-item index="2-1">学位点介绍</el-menu-item>
            <el-menu-item index="2-2">培养方案</el-menu-item>
            <el-menu-item index="2-3">信息公告</el-menu-item>
          </el-sub-menu>
        </el-menu>
      </el-aside>
      <el-container>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/home' }">主页</el-breadcrumb-item>
          <el-breadcrumb-item>人才培养</el-breadcrumb-item>
          <el-breadcurmb-item>{{where}}</el-breadcurmb-item>
        </el-breadcrumb>
        <el-header><p>通知</p></el-header>
        <el-main>
          <div class="news-list">
            <el-table :data="inforsList.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%"
                      @cell-click="changetodetail">
              <el-table-column prop="name" label="标题" width="600px"/>
              <el-table-column prop="pub_time" label="时间" width="300px"/>
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

export default {
  name: "Graduate",
  components: {Header, Footer},
  data() {
    return {
      inforsList: [],
      totalPages: 0,
      pageSize: 10,
      currentPage: 1,
      detail: 'majorDetail',
      activeMenu: "1",
      where: '专业介绍',
    }
  },
  methods: {
    getList(url) {
      axios
          .get(url)
          .then(response => {
            this.totalPages = response.data.count,
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
          .then(
              response => {
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
    handleSelect(key,keyPath) {
      if (keyPath === '1-1') {
        this.getList('/api/student/major?category=本科生')
        this.detail = "majorDetail"
        this.where = "专业介绍"
        this.reload()
      }
      if (keyPath === '1-2') {
        this.getList('/api/student/plan?category=本科生')
        this.detail = "planDetail"
        this.where = "培养方案"
        this.reload()
      }
      if (keyPath === '1-3') {
        this.getList('/api/student/teaching?category=本科生')
        this.detail = "teachingDetail"
        this.where = "教学成果"
      }
      if (keyPath === '1-4') {
        this.getList('/api/student/course?category=本科生')
        this.detail = "courseDetail"
        this.where = "精品课程"
      }
      if (keyPath === '2-1') {
        this.getList('/api/student/major?category=研究生')
        this.detail = "majorDetail"
        this.where = "学位点介绍"
      }
      if (keyPath === '2-2') {
        this.getList('/api/student/plan?category=研究生')
        this.detail = "planDetail"
        this.where = "培养方案"
      }
      if (keyPath === '2-3') {
        this.getList('/api/student/notice')
        this.detail = "noticeDetail"
        this.where = "信息公告"
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
