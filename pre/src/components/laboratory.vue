<template>
  <el-col>
    <el-row>
      <el-button type="info" @click="$router.push('/laboratory')">中心概况</el-button>
    </el-row>
    <el-row>
      <el-button type="info" @click="$router.push('/gerneral')">综合实验室</el-button>
    </el-row>
    <el-row>
      <el-button type="info" @click="$router.push('/hardware')">硬件实验室</el-button>
    </el-row>
    <el-row>
      <el-button type="info" @click="$router.push('/network')">网络实验室</el-button>
    </el-row>
    <el-row>
      <el-button type="info" @click="$router.push('/IOT')">物联网验室</el-button>
    </el-row>
    <el-row>
      <el-button type="info" @click="$router.push('/embedded')">嵌入式验室</el-button>
    </el-row>
  </el-col>
</template>

<script>
export default {
name: "laboratory"
}
</script>

<style scoped>
.el-row {
  margin-top: 10%;
  margin-left: 30%;
  margin-bottom: 10%;
}

.el-button {
  margin-top: 10px;
  height: 40px;
  width: 240px;
}
</style>
