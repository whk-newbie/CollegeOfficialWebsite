<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-aside width="20%">
        <el-col>
          <el-row>
            <el-button type="info" @click="$router.push('/news')">学院新闻</el-button>
          </el-row>
          <el-row>
            <el-button type="info" @click="$router.push('/information')">通知公告</el-button>
          </el-row>
        </el-col>
      </el-aside>
      <el-container>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/news'}">新闻中心</el-breadcrumb-item>
          <el-breadcrumb-item>学院通知</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>通知</p></el-header>
        <el-main>
          <div class="news-list">
            <el-table :data="inforsList.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%"
                      @cell-click="changetodetail">
              <el-table-column prop="title" label="标题" width="600px"/>
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
import axios from "axios";

export default {
  name: "Information",
  components: {Header, Footer},
  data() {
    return {
      loading: false,
      inforsList: [],
      totalPages: 0,
      pageSize: 10,
      currentPage: 1,
    }
  },
  mounted() {
    this.loading = true;
    this.getList();
  },
  methods: {
    getList() {
      axios
          .get('/api/infos')
          .then(response => {
            this.totalPages = response.data.count,
                (this.inforsList = response.data.results)
            // console.log(this.newsList)
            if (response.data.next !== null) {
              this.getData(response.data.next.charAt(response.data.next.length - 1))
            }
          })
      this.loading = false;
    },
    getData(number) {
      axios.get('api/infos', {params: {page: number}})
          .then(
              response => {
                this.inforsList = this.inforsList.concat(response.data.results)
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
    // formatted_time: function (row, column) {
    //   const date = new Date(row[column.property]);
    //   // return date.toLocaleDateString()
    //   return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate()
    // },
    changetodetail(row) {
      this.$router.push({name: 'NewsDetail', params: {id: row.id}})
    },
  }
}
</script>

<style scoped>

.container {
  margin: 2% 2% 2% 10%;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}

.el-main > h3 {
  font-size: 22px;
  font-family: 微软雅黑 serif;
  margin-left: 5%;
  padding: 0;
}

.el-breadcrumb {
  margin-top: 10px;
  margin-left: 10px;
  font-family: 微软雅黑 serif;
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
