<template>
  <div class="body">
    <div class="newsbox">
      <el-row :gutter="28">
        <el-col :span="12">
          <div class="grid-content bg-purple">
            <!--    轮播图-->
            <el-carousel class="carousel">
              <!--              生成五个-->
              <template v-for="(item,index) in tableData" :key="index">

                <el-carousel-item v-if="index < 6 && item.cover"
                                  @click="$router.push({ name: 'newsDetail', params: { id: item.id }})">
                  <!--                  <router-view :to="{ name: 'NewsDetail', params: { id: item.id }}">-->
                  <div class="pic_item">
                    <img class="small" :src="item.cover" alt="封面图片"/>
                    <h3>{{ item.title }}</h3>
                  </div>
                </el-carousel-item>
              </template>
            </el-carousel>
          </div>
        </el-col>
        <el-col :span="12">
          <div class="grid-content bg-purple">
            <div class="newslist">
              <el-table :data="tableData" stripe style="width: 100%;height:135%"
                        @cell-click="changetoNewsDetail">
                <el-table-column prop="title" label="学院新闻"/>
                <el-table-column prop="create_time" :formatter="formatted_time" width="180">
                  <template #header>
                    <el-button style="border:0;" @click="$router.push('/newsAndinfos/newscenter')">更多+</el-button>
                  </template>
                </el-table-column>
              </el-table>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="midlist">
      <el-row :gutter="2">
        <el-col :span="6">
          <div class="grid-content dangshi" @click="this.$router.push('/PartyLearning')">
            <el-icon :size="30" color="white" class="icon">
              <reading/>
            </el-icon>
            <span>党史学习专栏</span></div>
        </el-col>
        <el-col :span="6">
          <div class="grid-content zhuti" @click="this.$router.push('/thematic')">
            <el-icon :size="30" color="white" class="icon">
              <collection/>
            </el-icon>
            <span>主题学习专栏</span>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="grid-content xiaoqing" @click="this.$router.push('/anniversary')">
            <el-icon :size="30" color="white" class="icon">
              <checked/>
            </el-icon>
            <span>80周年校庆</span>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="grid-content xiaoyou" @click="this.$router.push('/alumnus')">
            <el-icon :size="30" color="white" class="icon">
              <connection/>
            </el-icon>
            <span>计信校友专栏</span>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="info">
      <el-table :data="infoData" stripe style="width: 100%;height:400px;"
                @cell-click="changetoInfosdetail">
        <el-table-column prop="title" label="通知"/>
        <el-table-column prop="create_time" :formatter="formatted_time" width="180">
          <template #header>
            <el-button @click="$router.push('/newsAndinfos/inforsCenter')" style="border:0;">更多+</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div class="achives">
      <el-header>
        <el-container>
          <div style="margin-right: 90%;margin-top:1%">成就</div>
          <el-button @click="moreinfo" style="border:0;margin-top:1%">更多+</el-button>
        </el-container>
      </el-header>
      <el-container>
        <el-aside width="30%">
          <el-card :body-style="{ padding: '0px' }" shadow="hover">
            <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                 class="image" alt="成就图片"/>
            <div style="padding: 14px">
              <span>Yummy hamburger</span>
            </div>
          </el-card>
        </el-aside>
        <el-container>
          <el-main>
            <el-row :gutter="12" style="margin-top:2%;margin-bottom: 2%">
              <el-col :span="8">
                <el-card shadow="hover"> hover</el-card>
              </el-col>
              <el-col :span="8">
                <el-card shadow="hover"> Hover</el-card>
              </el-col>
              <el-col :span="8">
                <el-card shadow="hover"> hover</el-card>
              </el-col>
            </el-row>
            <el-row :gutter="12" style="margin-top:2%;margin-bottom: 2%">
              <el-col :span="8">
                <el-card shadow="hover"> hover</el-card>
              </el-col>
              <el-col :span="8">
                <el-card shadow="hover"> Hover</el-card>
              </el-col>
              <el-col :span="8">
                <el-card shadow="hover"> hover</el-card>
              </el-col>
            </el-row>
          </el-main>
        </el-container>
      </el-container>
    </div>
    <div class="Academic">

    </div>
  </div>
  <el-backtop/> #快速回顶部
</template>

<script>
import {Connection, Checked, Collection, Reading} from '@element-plus/icons-vue'
// import axios from 'axios';
import {ref} from "vue"
import formatted_time from '@/composables/formatted_time';
import get_Data from "@/composables/get_Data";

export default {
  name: "homebody",
  components: {
    Connection, Checked, Collection, Reading
  },
  setup() {
    const tableData = ref([])
    const infoData = ref([])
    get_Data(tableData, '/api/news')
    get_Data(infoData, '/api/infos')
    return {
      tableData,
      infoData,
      formatted_time
    }
  },
  data() {
    return {};
  },
  methods: {
    changetoNewsDetail(row) {
      this.$router.push({name: 'newsDetail', params: {id: row.id}})
    },
    changetoInfosdetail(row) {
      this.$router.push({name: 'infosDetail', params: {id: row.id}})
    },
    moreinfo() {
      console.log("test")
    },
  }
}
</script>

<style scoped>
.newsbox {
  margin: 2% 10%;
  width: 80%;
  height: 35%;
  box-shadow: 5px 4px 15px #dad9d9;
  border-radius: 5px;
}

.small {
  width: 100%;
  height: 100%;
  position: relative;
}

.pic_item {
  position: relative;
  height: 100%;
}

.pic_item:hover {
  cursor: pointer;
}

.pic_item img {
  width: 100%;
  height: 100%;
}

.pic_item h3 {
  position: absolute;
  color: #fff;
  left: 4rem;
  bottom: 2rem;
}

.newslist {
  height: 190px;
}

.newslist span {
  margin-left: 2%;
  color: brown;
}

.midlist {
  margin: 2% 10%;
  width: 80%;
  height: 35%;
  box-shadow: 5px 4px 15px #dad9d9;
  border-radius: 5px;
}

.info {
  margin: 2% 10%;
  width: 80%;
  height: 135%;
  box-shadow: 5px 5px 15px #dad9d9;
  border-radius: 5px;
}

.info span {
  margin-right: 2%;
  color: brown;
  float: right;
}

.achives {
  margin: 2% 10%;
  width: 80%;
  height: 35%;
  box-shadow: 5px 5px 15px #dad9d9;
  border-radius: 5px;
}

.carousel {
  width: 100%;
}

.carousel > h4 {
  float: right;
}

.midlist .grid-content {
  transition: all 0.6s;
  box-shadow: 5px 5px 15px #dad9d9;
}

.midlist .grid-content:hover {
  transform: scale(1.2);
}

.grid-content > span {
  font-family: 华文仿宋, serif;
  font-style: normal;
  font-size: 28px;
  margin-left: 20%;
  padding: 5%;
  display: flex;
}

.icon {
  margin-top: 5%;
}

.dangshi {
  background-color: #b1b817;
  text-align: center;
  height: auto;

}

.zhuti {
  background-color: #1a8dc2;
  text-align: center;
  height: auto;
}

.xiaoqing {
  background-color: #b82b2c;
  text-align: center;
  height: auto;
}

.xiaoyou {
  background-color: #8e0e0a;
  text-align: center;
  height: auto;
}

</style>


