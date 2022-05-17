<template>
  <div class="news-list">
    <el-table :data="lists.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%"
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
</template>

<script>
import {ref} from 'vue'
import formatted_time from "@/composables/formatted_time";
import get_Data from "@/composables/get_Data";

export default {
  name: "list",
  props: {url: String},
  setup(props){
    const lists = ref([])
    const totalPages = ref(0)
    // console.log(props)
    get_Data(lists,props.url,totalPages)
    // console.log(totalPages)
    return {
      lists,
      totalPages,
      formatted_time
    }
  },
  data() {
    return {
      pageSize: 10,
      currentPage: 1,
    }
  },
  methods: {
    handleSizeChange(val) {
      this.pageSize = val;
    },
    handleCurrentChange(val) {
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
      this.$router.push({name: names, params: {id: row.id}})
    },
  },
}
</script>

<style scoped>
@import "~@/styles/body.css";
</style>
