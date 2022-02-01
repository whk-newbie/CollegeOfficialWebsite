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
            <el-button type="info" @click="$router.push('/imagenews')">图片新闻</el-button>
          </el-row>
          <el-row>
            <el-button type="info" @click="$router.push('/information')">通知公告</el-button>
          </el-row>
        </el-col>
      </el-aside>
      <el-container>
        <el-breadcrumb separator="/">
          <el-breadcrumb-item>当前位置: </el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
          <el-breadcrumb-item :to="{ path: '/news'}">新闻中心</el-breadcrumb-item>
          <el-breadcrumb-item>图片新闻</el-breadcrumb-item>
        </el-breadcrumb>
        <el-header><p>图片新闻</p></el-header>
        <el-main>
          <div class="news-list">
            <el-row :gutter="2" class="listitem">
              <el-col :span="8">发布内容</el-col>
              <el-col :span="4">发布时间</el-col>
            </el-row>
            <el-row :gutter="2" width="100%" v-for="item in infos" :key="item.title" class="listitem">
              <el-col :span="8">{{ item.title }}</el-col>
              <el-col :span="4">{{ item.create_time }}</el-col>
            </el-row>
          </div>
          <div class="paginationbox">
            <el-pagination
                v-model:currentPage="currentPage"
                :page-sizes="[14, 28, 42, 56]"
                :page-size="14"
                layout="total, sizes, prev, pager, next, jumper"
                :total="400"
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

export default {
  name: "ImageNews",
  components: {Header, Footer},
}
</script>

<style scoped>

.container {
  margin: 2% 2% 2% 10%;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}
.el-breadcrumb {
  margin-top: 10px;
  margin-left:10px;
  font-family: 微软雅黑;
}

.el-main > h3 {
  font-size: 22px;
  font-family: 微软雅黑;
  margin-left: 5%;
}

.el-aside {
  background-color: #92f6ce;
}


.el-header {
  text-align: -webkit-left;
  font-size: 24px;
  font-style: normal;
  font-family: 仿宋_GB2312;
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

.news-list{
  width: 100%;
  height: 400px;
  margin: 0;
  padding: 0;
}

.listitem {
  margin: 1px auto 0 30px;
  padding: 2px 10px;
  width: 100%;
  height: 20px;
}

.paginationbox {
  position: relative;
  left: auto;
}
</style>
