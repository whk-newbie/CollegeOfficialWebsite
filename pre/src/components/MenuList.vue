<template>
  <el-menu :default-active="activeIndex" mode="horizontal" background-color="#4a967a" text-color="#fff"
           active-text-color="bisque" @select="handleSelect" :ellipsis=false router>
    <div v-for="(item,index) in menuItems" :key="index">
      <!--        第一层-->
      <el-sub-menu v-if="item.children.length > 0" :index="item.path">
        <template #title>
          {{ item.meta.title }}
          <el-icon>
          </el-icon>
        </template>
        <!--        第二层-->
        <div v-for="(item2,index2) in item.children " :key="index2">
          <el-sub-menu v-if="item2.children.length > 0" :index="item2.path">
            <template #title>{{ item2.meta.title }}</template>
            <!--            第三层-->
            <el-menu-item v-for="(item3,index3) in item2.children" :key="index3" :index="item3.path">
              {{ item3.meta.title }}
            </el-menu-item>
          </el-sub-menu>
          <el-menu-item v-else :index="item2.path">{{ item2.meta.title }}</el-menu-item>
        </div>
      </el-sub-menu>
      <el-menu-item v-else :index="item.path">{{ item.meta.title }}</el-menu-item>
    </div>
    <button @click="toadmin" color="" size="small" class="admin-button">管理员登录</button>
  </el-menu>

</template>

<script>
import router from "@/router";

export default {
  name: "MenuList",
  data() {
    return {
      activeIndex: this.$route.path,
      handleSelect: this.$route.path,
    }
  },

  setup() {
    let menuItems = router.options.routes.filter(item => item.meta.isShow || item.children !== null)
    return {
      menuItems
    }
  },
  methods: {
    toadmin() {
      window.location.href = 'http://127.0.0.1:8000/admin/'
    }
  }
}
</script>

<style scoped>
. {
  margin: 0;
  padding: 0;
}

.el-submenu .el-icon {
  margin-right: 2px;
}

.admin-button{
  left: 2px;
  width: 80px;
  height: 50px;
  font-size: 5px;
  background-color: #4a967a;
  color: #fff;
  margin-top: 4px;
  border-radius: 10px;
  border: 0;
}
.admin-button:hover{
  cursor: pointer;
  color: #1a8dc2;

}
</style>
