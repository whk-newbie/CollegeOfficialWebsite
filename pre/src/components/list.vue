<template>
  <div class="news-list">
    <el-table :data="lists.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%"
              @cell-click="changetodetail" v-loading="loading">
      <el-table-column prop="title"  width="600px"/>
      <el-table-column prop="create_time"  width="300px" :formatter="formatted_time"/>
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
      const loact = this.url.split('/')
      console.log(loact)
      if (loact.length === 4 && loact[2]==='news')
      {
        this.$router.push({name: 'newsDetail', params: {id: row.id}})
      }
      if (loact.length === 3 && loact[2]==='infos')
      {
        this.$router.push({name: 'infosDetail', params: {id: row.id}})
      }
      if (loact.length === 4 && loact[3]==='Tmorality')
      {
        this.$router.push({name: 'TmoralityDetail', params: {id: row.id}})
      }

      // this.$router.push({name: 'TmoralityDetail', params: {id: row.id}})
    },
  },
}
</script>

<style scoped>
@import "~@/styles/body.css";
</style>
