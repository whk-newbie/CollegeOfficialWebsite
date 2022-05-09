<template>
  <Header/>
  <div class="body">
    <el-container>
      <el-aside width="20%">
        <el-menu
            :default-active="activeMenu"
            class="el-menu-vertical-demo"
            @select="handleSelect"
            background-color="#92f6ce"
            :unique-opened=true
        >
          <el-sub-menu index="1">
            <template #title>
              <span>本科生教育</span>
            </template>
            <el-menu-item index="1-1">专业介绍</el-menu-item>
            <el-menu-item index="1-2">培养方案</el-menu-item>
            <el-menu-item index="1-3">教学成果</el-menu-item>
            <el-menu-item index="1-4">精品课程</el-menu-item>
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
          <el-breadcrumb-item>{{it}}</el-breadcrumb-item>
          <el-breadcrumb-item>{{ where }}</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>{{ where }}</p></el-header>
        <el-main>
          <div class="news-list">
            <el-table :data="inforsList.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%"
                      @cell-click="changetodetail">
              <el-table-column prop="title" width="600px"/>
              <el-table-column prop="create_time" width="300px" :formatter="formatted_time"/>
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
  name: "Graduate",
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
      activeMenu: "1-1",
      it:'本科生教育',
      where: '专业介绍',
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
        this.$router.push('/education/graduate/magjor')
        this.judge()
      }
      if (key === '1-2') {
        this.$router.push('/education/graduate/plan')
        this.judge()
      }
      if (key === '1-3') {
        this.$router.push('/education/graduate/achieve')
        this.judge()
      }
      if (key === '1-4') {
        this.$router.push('/education/graduate/course')
        this.judge()
      }

      if (key === '2-1') {
        this.$router.push('/education/undergraduate/major')
        this.judge()
      }
      if (key === '2-2') {
        this.$router.push('/education/undergraduate/plan')
        this.judge()
      }
      if (key === '2-3') {
        this.$router.push('/education/undergraduate/notice')
        this.judge()
      }
    },
    judge() {
      // console.log(this.$route.fullPath)
      const paths = this.$route.fullPath.split('/')
      // console.log(paths)
      if (paths[2] === "graduate") {
        if (paths[3] === "major") {
          this.getList('/api/student/major?category=本科生')
          this.detail = "majorDetail"
          this.where = "专业介绍"
          this.activeMenu='1-1'
        }
        if (paths[3] === "plan") {
          this.getList('/api/student/plan?category=本科生')
          this.detail = "planDetail"
          this.where = "培养方案"
          this.activeMenu='1-2'
        }
        if (paths[3] === "achieve") {
          this.getList('/api/student/teaching?category=本科生')
          this.detail = "teachingDetail"
          this.where = "教学成果"
          this.activeMenu='1-3'
        }
        if (paths[3] === "course") {
          this.getList('/api/student/course?category=本科生')
          this.detail = "courseDetail"
          this.where = "精品课程"
          this.activeMenu='1-4'
        }

      } else {
        this.it="研究生教育"
        if (paths[3]==='major') {
          this.getList('/api/student/major?category=研究生')
          this.detail = "majorDetail"
          this.where = "学位点介绍"
          this.activeMenu='2-1'
        }
        if (paths[3]==='plan') {
          this.getList('/api/student/plan?category=研究生')
          this.detail = "planDetail"
          this.where = "培养方案"
          this.activeMenu='2-2'
        }
        if (paths[3]==='notice') {
          this.getList('/api/student/notice')
          this.detail = "noticeDetail"
          this.where = "信息公告"
          this.activeMenu='2-3'
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


.el-aside {
  background-color: #92f6ce;
}


@import "~@/styles/body.css";
</style>
