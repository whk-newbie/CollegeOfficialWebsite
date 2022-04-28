<template>
  <Header/>
  <div class="container">
    <div class="news-list">
      <el-table :data="lists.slice((currentPage-1)*pageSize,currentPage*pageSize)" style="width: 100%"
                @cell-click="changetodetail" v-loading="loading">
        <el-table-column prop="title" label="标题" width="600px"/>
        <el-table-column prop="created" label="时间" width="300px"/>
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
  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import axios from "axios";

export default {
  name: "Tmorality",
  components: {Header, Footer},
  data() {
    return {
      lists: [],
      totalPages: 0,
      pageSize: 10,
      currentPage: 1,
      loading: false,
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
          .get('/api/Tmorality')
          .then(response => {
            this.totalPages = response.data.count,
                (this.lists = response.data.results)
            if (response.data.next !== null) {
              this.getData(response.data.next.charAt(response.data.next.length - 1))
            }
          })
      this.loading = false;
    },
    getData(number) {
      axios.get('api/Tmorality', {params: {page: number}})
          .then(
              response => {
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
      this.$router.push({name: 'TmoralityDetail', params: {id: row.id}})
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

.news-list {
  /*width: 100%;*/
  height: 500px;
  position: relative;
  margin-left: 20%;
  margin-right: 20%;
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
