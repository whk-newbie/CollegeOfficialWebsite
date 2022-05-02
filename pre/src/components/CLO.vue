<template>
  <el-col>
    <el-row>
      <el-button type="info" @click="$router.push('/collegeOverView/overview')">学院简介</el-button>
    </el-row>
    <el-row>
      <el-button type="info" @click="$router.push('/collegeOverView/leaders')">学院领导</el-button>
    </el-row>
    <el-row>
      <el-button type="info" @click="$router.push('/collegeOverView/organization')">内设机构</el-button>
    </el-row>
  </el-col>
</template>

<script>
export default {
  name: "CLO"
}
</script>

<style scoped>
.el-row {
  margin-top: 10%;
  margin-left: 50%;
}

.el-button {
  margin-top: 10px;
  height: 40px;
  width: 120px;
}
</style>
