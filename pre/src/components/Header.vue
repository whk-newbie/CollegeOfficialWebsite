<template>
  <div class="header">
    <div class="img">
      <div class="imgs">
        <span class="head-text">计算机信息工程学院</span>
      </div>
    </div>
    <div class="list">
      <el-menu
          router
          :default-active="this.$route.path"
          class="el-menu-demo"
          mode="horizontal"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
          @select="handleSelect"
      >
        <el-menu-item index="/" >首页</el-menu-item>
        <el-sub-menu index="2">
          <template #title>学院概况</template>
          <el-menu-item index="CollegeOverview">学院简介</el-menu-item>
          <el-menu-item index="leaders">学院领导</el-menu-item>
          <el-menu-item index="organization">内设机构</el-menu-item>
          <el-sub-menu index="2-4">
            <template #title>师资队伍</template>
            <el-menu-item index="teacher">专人教师</el-menu-item>
            <el-menu-item index="professor">教授队伍</el-menu-item>
            <el-menu-item index="tutor">硕士生导师</el-menu-item>
            <el-menu-item index="2-4-4">招贤纳才</el-menu-item>
          </el-sub-menu>
        </el-sub-menu>
        <el-sub-menu index="3">
          <template #title>新闻中心</template>
          <el-menu-item index="news">学院新闻</el-menu-item>
          <el-menu-item index="information">学院通知</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="4">
          <template #title>人才培养</template>
          <el-sub-menu index="graduate">
            <template #title>本科生教育</template>
            <el-menu-item index="">专业介绍</el-menu-item>
            <el-menu-item index="4-1-2">培养方案</el-menu-item>
            <el-menu-item index="4-1-3">教学成果</el-menu-item>
            <el-menu-item index="4-1-4">精品课程</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="undergraduate">
            <template #title>研究生教育</template>
            <el-menu-item index="4-2-1">学位点介绍</el-menu-item>
            <el-menu-item index="4-2-2">培养方案</el-menu-item>
            <el-menu-item index="4-2-3">信息公告</el-menu-item>
          </el-sub-menu>
        </el-sub-menu>
        <el-sub-menu index="5">
          <template #title>科学研究</template>
          <el-menu-item index="5-1">科研动态</el-menu-item>
          <el-menu-item index="5-2">科研机构</el-menu-item>
          <el-menu-item index="5-3">科研成果</el-menu-item>
        </el-sub-menu>
        <el-menu-item index="6">师德师风</el-menu-item>
        <el-sub-menu index="7">
          <template #title>招生就业</template>
          <el-sub-menu index="7-1">
            <template #title>本科生</template>
            <el-menu-item index="7-1-1">招生</el-menu-item>
            <el-menu-item index="7-1-2">就业</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="7-2">
            <template #title>研究生</template>
            <el-menu-item index="7-2-1">招生</el-menu-item>
            <el-menu-item index="7-2-2">就业</el-menu-item>
          </el-sub-menu>
        </el-sub-menu>
        <el-menu-item index="8">党建工作</el-menu-item>
        <el-sub-menu index="9">
          <template #title>团学工作</template>
          <el-menu-item index="9-1">学工新闻</el-menu-item>
          <el-menu-item index="9-2">青年之声江西师范大学</el-menu-item>
          <el-menu-item index="9-3">团学组织</el-menu-item>
          <el-menu-item index="9-5">党员服务</el-menu-item>
          <el-menu-item index="9-5">管理制度</el-menu-item>
          <el-menu-item index="9-6">荣誉室</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="10">
          <template #title>实验中心</template>
          <el-menu-item index="laboratory">中心概况</el-menu-item>
          <el-menu-item index="gerneral">综合实验室</el-menu-item>
          <el-menu-item index="hardware">硬件实验室</el-menu-item>
          <el-menu-item index="network">网络实验室</el-menu-item>
          <el-menu-item index="IOT">物联网实验室</el-menu-item>
          <el-menu-item index="embedded">嵌入式实验室</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="12">
          <template #title>下载中心</template>
          <el-menu-item index="12-1">学习资料</el-menu-item>
          <el-menu-item index="12-2">软件下载</el-menu-item>
          <el-menu-item index="12-3"><a class="ccf" href="https://dl.ccf.org.cn/index.html?_ack=1">CCF数字图书馆</a></el-menu-item>
        </el-sub-menu>
      </el-menu>
    </div>
  </div>
</template>

<script>
// import router from "../router/index.js";

export default {
  name: 'Header',
  // setup() {
  //   let menuItems = router.options.routes.filter(item => item.meta.isShow || item.children != null)
  //   console.info(menuItems)
  //   return {
  //     menuItems
  //   }
  // },
  data() {
    return {
      activeIndex: this.$route.path,
      handleSelect:this.$route.path,
    };
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header {
  margin: 0;
  border: 0;
  padding: 0;
}

.img {
  width: 100%;
  height: auto;
  background: url("https://jsjxy.jxnu.edu.cn/_upload/tpl/00/d8/216/template216/images/head.jpg");
  background-size: cover;
}

.imgs {
  padding: 80px 50px;
}

.imgs span {
  margin-left: 35%;
  color: #01697c;
  font-family: "华文行楷";
  font-weight: bolder;
  font-size: 36px;
}

.ccf {
  color: #F5FFFA;
  text-decoration: none
}

</style>
