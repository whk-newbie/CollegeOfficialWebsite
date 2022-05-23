<template>
  <div class="body">
    <div class="news-box">
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
          <div class="grid-content xiaoyou" @click="xiaoyou">
            <el-icon :size="30" color="white" class="icon">
              <connection/>
            </el-icon>
            <span style="padding-left: 18%;">校友会</span>
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
      <el-container>
        <el-header class="span-head">
          <el-row :gutter="24">
            <el-col :span="12">
              <div class="span-1">成就</div>
            </el-col>
            <el-col :span="12">
              <el-button class="head-button" @click="this.$router.push('/group/honor')">更多+</el-button>
            </el-col>
          </el-row>
        </el-header>
        <el-main style="padding-bottom: 0;padding-top: 0">
          <el-row :gutter="24">
            <el-col :span="8">
              <el-card class="card-box" :body-style="{ padding: '0px'}">
                <div v-if="achieve[0]">
                  <img class="card-image" alt="成就图片" :src="achieve[0].photo"/>
                  <span class="card-title">{{ achieve[0].title }}</span>
                </div>
              </el-card>
            </el-col>
            <el-col :span="16">
              <el-row :gutter="20" style="margin: 0;padding: 0;">
                <el-col :span="6">
                  <el-card class="card-box" :body-style="{ padding: '0px'}">
                    <div v-if="achieve[0]">
                      <img class="card-image" alt="成就图片" :src="achieve[0].photo"/>
                      <span class="card-title">{{ achieve[0].title }}</span>
                    </div>
                  </el-card>
                </el-col>
                <el-col :span="6">
                  <el-card class="card-box" :body-style="{ padding: '0px'}">
                    <div v-if="achieve[0]">
                      <img class="card-image" alt="成就图片" :src="achieve[0].photo"/>
                      <span class="card-title">{{ achieve[0].title }}</span>
                    </div>
                  </el-card>
                </el-col>
                <el-col :span="6">
                  <el-card class="card-box" :body-style="{ padding: '0px'}">
                    <div v-if="achieve[0]">
                      <img class="card-image" alt="成就图片" :src="achieve[0].photo"/>
                      <span class="card-title">{{ achieve[0].title }}</span>
                    </div>
                  </el-card>
                </el-col>
              </el-row>
              <el-row :gutter="20" style="margin: 0;padding: 0;">
                <el-col :span="6">
                  <el-card class="card-box" :body-style="{ padding: '0px'}">
                    <div v-if="achieve[0]">
                      <img class="card-image" alt="成就图片" :src="achieve[0].photo"/>
                      <span class="card-title">{{ achieve[0].title }}</span>
                    </div>
                  </el-card>
                </el-col>
                <el-col :span="6">
                  <el-card class="card-box" :body-style="{ padding: '0px'}">
                    <div v-if="achieve[0]">
                      <img class="card-image" alt="成就图片" :src="achieve[0].photo"/>
                      <span class="card-title">{{ achieve[0].title }}</span>
                    </div>
                  </el-card>
                </el-col>
                <el-col :span="6">
                  <el-card class="card-box" :body-style="{ padding: '0px'}">
                    <div v-if="achieve[0]">
                      <img class="card-image" alt="成就图片" :src="achieve[0].photo"/>
                      <span class="card-title">{{ achieve[0].title }}</span>
                    </div>
                  </el-card>
                </el-col>
              </el-row>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </div>
    <div class="Academic">

    </div>
  </div>
  <el-backtop/>
</template>

<script>
import {Connection, Checked, Collection, Reading} from '@element-plus/icons-vue'
import {ref} from "vue"
import formatted_time from '@/composables/formatted_time';
import get_Data from "@/composables/get_Data";
import get_achieve from "@/composables/get_achieve";

export default {
  name: "homebody",
  components: {
    Connection, Checked, Collection, Reading
  },
  setup() {
    const tableData = ref([])
    const infoData = ref([])
    const achieve = ref([])
    get_Data(tableData, '/api/news')
    get_Data(infoData, '/api/infos')
    get_achieve(achieve)
    return {
      tableData,
      infoData,
      achieve,
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
    xiaoyou() {
      window.open('https://xy.jxnu.edu.cn/#/', '_blank')
    }
  }
}
</script>

<style scoped>
.news-box {
  margin: 2% 10%;
  width: 80%;
  height: 35%;
  box-shadow: 5px 4px 15px #dad9d9;
  border-radius: 5px;
}

.el-row {
  margin-top: 0;
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
  height: 25%;
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



.head-button {
  border: 0;
  margin-top: 3%;
  margin-left: 75%;
}

.span-1 {
  margin-top: 4%;
  font-size: 14px;
  font-family: 微软雅黑, serif;
  color: gray;
}

.card-box ::v-deep {
  width: 80%;
  height: 60%;
}

.card-box div {
  width: 100%;
  height: 100%;
}

.card-image {
  width: 100%;
  height: 100%;
  padding-bottom: 0;
  margin-bottom: 0;
}

.card-title {
  position: relative;
  color: black;
  left: 1rem;
  bottom: 3rem;
}
</style>


