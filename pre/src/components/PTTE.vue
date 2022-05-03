<template>
  <el-col>
    <el-row>
      <el-button type="info" @click="$router.push('/teacher/teachers')">专任教师</el-button>
    </el-row>
    <el-row>
      <el-button type="info" @click="$router.push('/teacher/professor')">教授队伍</el-button>
    </el-row>
    <el-row>
      <el-button type="info" @click="$router.push('/teacher/tutor')">研究生导师</el-button>
    </el-row>
    <el-row>
      <el-button type="info" @click="$router.push('/teacher/enrollful')">招贤纳士</el-button>
    </el-row>
  </el-col>
</template>

<script>
export default {
  name: "PTTE"
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
