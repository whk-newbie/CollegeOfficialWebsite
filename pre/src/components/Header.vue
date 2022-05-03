<template>
  <div class="header">
    <div class="img">
      <div class="imgs">
        <span class="head-text">计算机信息工程学院</span>
      </div>
    </div>
    <div class="menu-list">
        <MenuList/>
    </div>
  </div>
</template>

<script>
// import router from "../router/index.js";
import MenuList from "@/components/MenuList"
export default {
  name: 'Header',
  components: {MenuList},
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
  font-family: "华文行楷",serif;
  font-weight: bolder;
  font-size: 36px;
}

.ccf {
  color: #F5FFFA;
  text-decoration: none
}
.menu-list {
  position: relative;
  padding: 0 5% ;
  background:#4a967a;

}
</style>
