<template>
  <div class="body">
    <div class="newsbox">
      <el-row :gutter="28">
        <el-col :span="12">
          <div class="grid-content bg-purple">
            <!--    轮播图-->
            <el-carousel class="carousel">
              <el-carousel-item v-for="item in pics" :key="item.url">
                <router-view v-bind:to={}><img :src="item.url"/>
                  <h3>{{ item.title }}</h3></router-view>
              </el-carousel-item>
            </el-carousel>
          </div>
        </el-col>
        <el-col :span="12">
          <div class="grid-content bg-purple">
            <div class="newslist">
              <el-table v-loading="loading" :data="tableData" stripe style="width: 100%;height:135%"
                        @cell-click="changetodetil">
                <el-table-column prop="article.title" label="学院新闻"/>
                <el-table-column prop="article.date" width="180"/>
              </el-table>
              <div style="border:0;margin-bottom: 50%">
                <el-button style="border:0;margin-left:85%;" @click="$router.push('/News')">更多+</el-button>
              </div>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="midlist">
      <el-row :gutter="2">
        <el-col :span="6">
          <div class="grid-content dangshi">
            <el-icon :size="30" color="white" class="icon">
              <reading/>
            </el-icon>
            <span>党史学习专栏</span></div>
        </el-col>
        <el-col :span="6">
          <div class="grid-content zhuti">
            <el-icon :size="30" color="white" class="icon">
              <collection/>
            </el-icon>
            <span>主题学习专栏</span>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="grid-content xiaoqing">
            <el-icon :size="30" color="white" class="icon">
              <checked/>
            </el-icon>
            <span>80周年校庆</span>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="grid-content xiaoyou">
            <el-icon :size="30" color="white" class="icon">
              <connection/>
            </el-icon>
            <span>计信校友专栏</span>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="info">
      <el-table v-loading="loading" :data="infoData" stripe style="width: 100%;height:135%" height="100%"
                @cell-click="changetodetil">
        <el-table-column prop="info.title" label="通知"/>
        <el-table-column prop="info.date" width="180">
          <template #header>
            <el-button @click="moreinfo" style="border:0;textStyle:#8e0e0a">更多+</el-button>
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
                 class="image"/>
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
  <el-backtop/>
</template>

<script>
import {Connection, Checked, Collection, Reading} from '@element-plus/icons-vue'

export default {
  name: "homebody",
  components: {
    Connection, Checked, Collection, Reading
  },
  data() {
    return {
      pics: [
        {url: require("../assets/pic1.jpg"), title: "标题1sdfasdf"},
        {url: require("../assets/pic2.jpg"), title: "标题2sdfasdf"},
        {url: require("../assets/pic3.jpg"), title: "标题3dfasdfsda"},
        {url: require("../assets/pic4.jpg"), title: "标题4dfasdfdsa"}
      ],
      tableData: [
        {
          article: {
            title: "test",
            date: '2016-05-02',
          },
          id: '',
        },
        {
          article: {
            title: "test",
            date: '2016-05-02',
          },
          id: '',
        },
        {
          article: {
            title: "test",
            date: '2016-05-02',
          },
          id: '',
        },
        {
          article: {
            title: "test",
            date: '2016-05-02',
          },
          id: '',
        },
        {
          article: {
            title: "test",
            date: '2016-05-02',
          },
          id: '',
        },

      ],
      infoData: [
        {
          info: {
            title: "test",
            date: '2016-05-02',
          },
          id: '',
        },
        {
          info: {
            title: "test",
            date: '2016-05-02',
          },
          id: '',
        },
        {
          info: {
            title: "test",
            date: '2016-05-02',
          },
          id: '',
        },
        {
          info: {
            title: "test",
            date: '2016-05-02',
          },
          id: '',
        },
        {
          info: {
            title: "test",
            date: '2016-05-02',
          },
          id: '',
        }, {
          info: {
            title: "test",
            date: '2016-05-02',
          },
          id: '',
        },

      ],
    };
  },
  methods: {
    changetodetil() {
      alert("跳转中")
    },
    moreinfo() {
      alert("正在跳转到更多")
    }
  }
}
</script>

<style scoped>
.newsbox {
  margin: 2% 10%;
  width: 80%;
  height: 35%;
  box-shadow: 4px 4px 15px #dad9d9;
  border-radius: 5px;
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
  box-shadow: 4px 4px 15px #dad9d9;
  border-radius: 5px;
}

.info {
  margin: 2% 10%;
  width: 80%;
  height: 40%;
  box-shadow: 4px 4px 15px #dad9d9;
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
  box-shadow: 4px 4px 15px #dad9d9;
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
  box-shadow: 4px 4px 15px #dad9d9;
}

.midlist .grid-content:hover {
  transform: scale(1.2);
}

.grid-content > span {
  font-family: 华文仿宋;
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


