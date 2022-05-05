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
          <el-breadcrumb-item>团学工作</el-breadcrumb-item>
          <el-breadcrumb-item>{{ where }}</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>{{ where }}</p></el-header>
        <el-main>

          <div class="news-list">
            <el-table :data="newsList.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%"
                      @cell-click="changetodetail" v-loading="loading">
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
import Header from "@/components/Header"
import Footer from "@/components/Footer"
import formatted_time from "@/composables/formatted_time";
import axios from "axios";

export default {
  name: "GroupNews",
  components: {Header, Footer}
  ,
  data: function () {
    return {
      loading: false,
      newsList: [],
      totalPages: 0,
      pageSize: 10,
      currentPage: 1,
      where: "学工新闻",
      formatted_time
    }
  },
  created() {
    this.change()
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
      this.$router.push({name: 'NewsDetail', params: {id: row.id}})
    },
    change() {
      const paths = this.$route.fullPath.split('/')[2]
      console.log(paths)
      if (paths === "research") {
        this.getList('/api/research/research')
      }
      if (paths === "institutions") {
        this.getList('/api/research/institutions')
        this.where = "科研机构"
      }
      if (paths === "achievement") {
        this.getList('/api/research/achievements')
        this.where = "科研成果"
      }
    }
  }
}
</script>

<style scoped>
 @import "~@/styles/body.css";
</style>
