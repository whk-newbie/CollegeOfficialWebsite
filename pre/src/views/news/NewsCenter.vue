<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-aside width="20%">
        <el-col>
          <el-row>
            <el-button type="info" @click="$router.push('/newsAndinfos/overview')">学院新闻</el-button>
          </el-row>
          <el-row>
            <el-button type="info" @click="$router.push('/newsAndinfos/inforsCenter')">通知公告</el-button>
          </el-row>
        </el-col>
      </el-aside>
      <el-container>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/news'}">新闻中心</el-breadcrumb-item>
          <el-breadcrumb-item>学院新闻</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>学院新闻</p></el-header>
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
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import axios from "axios";
import formatted_time from '@/composables/formatted_time';
// import {ref} from "@vue/reactivity";
// import get_Data from "@/composables/get_Data";

export default {
  name: "NewsCenter",
  components: {Header, Footer},

  data: function () {
    return {
      loading: false,
      newsList: [],
      totalPages: 0,
      pageSize: 10,
      currentPage: 1,
      formatted_time
    }
  },
  mounted() {
    this.loading = true;
    this.getList();
  },
  methods: {
    getList() {
      axios
          .get('/api/news')
          .then(response => {
            this.totalPages = response.data.count,
                (this.newsList = response.data.results)
            // console.log(this.newsList)
            if (response.data.next !== null) {
              this.getData(response.data.next.charAt(response.data.next.length - 1))
            }
          })
      this.loading = false;

    },
    getData(number) {
      axios.get('api/news', {params: {page: number}})
          .then(
              response => {
                this.newsList = this.newsList.concat(response.data.results)
                // console.log(this.newsList)
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
    changetodetail(row) {
      this.$router.push({name: 'NewsDetail', params: {id: row.id}})
    },
  }
}
</script>

<style scoped>

@import "~@/styles/body.css";
</style>
