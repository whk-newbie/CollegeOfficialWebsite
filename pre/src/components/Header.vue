<template>
  <div class="header">
    <div class="img">
      <div class="imgs">
        <span class="head-text">计算机信息工程学院</span>
      </div>
    </div>
    <div class="list">
        <el-menu
            :default-active="activeIndex"
            class="el-menu-demo"
            mode="horizontal"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b"
            @select="handleSelect"
            ellipsis="false"
        >
          <el-menu-item index="1">首页</el-menu-item>
          <el-sub-menu index="2">
            <template #title>学院概况</template>
            <el-menu-item index="2-1">学院简介</el-menu-item>
            <el-menu-item index="2-2">学院领导</el-menu-item>
            <el-menu-item index="2-3">内设机构</el-menu-item>
            <el-sub-menu index="2-4">
              <template #title>师资队伍</template>
              <el-menu-item index="2-4-1">专人教师</el-menu-item>
              <el-menu-item index="2-4-2">教授队伍</el-menu-item>
              <el-menu-item index="2-4-3">硕士生导师</el-menu-item>
              <el-menu-item index="2-4-4">招贤纳才</el-menu-item>
            </el-sub-menu>
          </el-sub-menu>
          <el-sub-menu index="3">
            <template #title>人才培养</template>
            <el-menu-item index="3-1">研究生教育</el-menu-item>
            <el-menu-item index="3-2">本科生教育</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="4">
            <template #title>科学研究</template>
            <el-menu-item index="4-1">科研动态</el-menu-item>
            <el-menu-item index="4-2">科研机构</el-menu-item>
            <el-menu-item index="4-3">科研成果</el-menu-item>
          </el-sub-menu>
          <el-menu-item index="5">师德师风</el-menu-item>
          <el-sub-menu index="6">
            <template #title>招生就业</template>
            <el-menu-item index="6-1">本科生</el-menu-item>
            <el-menu-item index="6-2">研究生</el-menu-item>
          </el-sub-menu>
          <el-menu-item index="7">党建工作</el-menu-item>
          <el-sub-menu index="8">
            <template #title>团学工作</template>
            <el-menu-item index="8-1">学工新闻</el-menu-item>
            <el-menu-item index="8-2">青年之声江西师范大学</el-menu-item>
            <el-menu-item index="8-3">团学组织</el-menu-item>
            <el-menu-item index="8-4">党员服务</el-menu-item>
            <el-menu-item index="8-5">管理制度</el-menu-item>
            <el-menu-item index="8-6">荣誉室</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="9">
            <template #title>实验中心</template>
            <el-menu-item index="9-1">中心概况</el-menu-item>
            <el-menu-item index="9-2">综合实验室</el-menu-item>
            <el-menu-item index="9-3">硬件实验室</el-menu-item>
            <el-menu-item index="9-4">网络实验室</el-menu-item>
            <el-menu-item index="9-5">物联网实验室</el-menu-item>
            <el-menu-item index="9-6">嵌入式实验室</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="10">
            <template #title>主题教育专题</template>
            <el-menu-item index="10-1">活动报告</el-menu-item>
            <el-menu-item index="10-2">通知公告</el-menu-item>
            <el-menu-item index="10-3">文件学习</el-menu-item>
            <el-menu-item index="10-4">意见征集</el-menu-item>
          </el-sub-menu>
          <el-sub-menu index="11">
            <template #title>下载中心</template>
            <el-menu-item index="11-1">学习资料</el-menu-item>
            <el-menu-item index="11-2">软件下载</el-menu-item>
            <el-menu-item index="11-3"><a class="ccf" href="https://dl.ccf.org.cn/index.html?_ack=1">CCF数字图书馆</a></el-menu-item>
          </el-sub-menu>
        </el-menu>

    </div>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      activeIndex: '1',
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
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
.ccf{
  color:#F5FFFA;
  text-decoration: none
}

</style>
