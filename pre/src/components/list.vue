<template>
  <div class="news-list">
    <el-table :data="lists.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%"
              @cell-click="changetodetail" v-loading="loading">
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
</template>

<script>
import formatted_time from "@/composables/formatted_time";
import axios from "axios";

export default {
  name: "list",
  props: {url: String},
  data() {
    return {
      lists: [],
      totalPages: 0,
      pageSize: 10,
      currentPage: 1,
      loading: false,
      formatted_time
    }
  },
  mounted() {
    this.loading = true;
    this.getData();
    this.loading = false;
  },
  methods: {
    getList() {
      axios
          .get(this.url)
          .then(response => {
            this.lists = response.data.results;
            if (response.data.next !== null) {
              this.getData(response.data.next.charAt(response.data.next.length - 1))
            }

          })
      this.loading = false;
    },
    getData(number) {
      axios.get(this.url, {params: {page: number}})
          .then(
              response => {
                // console.log(response.data);
                this.totalPages = response.data.count;
                this.lists = this.lists.concat(response.data.results)
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
      const locat = this.url.split('/')
      // console.log(locat)
      const names = locat[locat.length - 1] + 'Detail'
      if (names === 'Learning?category=学习资料Detail' || names === 'Learning?category=软件Detail') {
        this.$router.push({name: 'Download', params: {id: row.id}})
      }
      if (names === 'fileandtrends?category=教育文件Detail' || names === 'fileandtrends?category=教育动态Detail') {
        this.$router.push({name: 'fileleanDetail', params: {id: row.id}})
      }
      // if (locat[2] === 'education')
      // {
      //   if (locat[3] === 'report') {
      //     this.$router.push({name: 'EreportDetail', params: {id: row.id}})
      //   }
      //   else if(locat[3]==='infos'){
      //     this.$router.push({name: 'EinfosDetail', params: {id: row.id}})
      //   }
      //   else {
      //     this.$router.push({name: 'EfileLearnDetail', params: {id: row.id}})
      //   }
      // }
      this.$router.push({name: names, params: {id: row.id}})
    },
  },
}
</script>

<style scoped>
@import "~@/styles/body.css";
</style>
