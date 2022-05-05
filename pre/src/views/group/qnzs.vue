<template>
  <div class="body">
    <el-progress type="circle" :percentage="percentage" style="margin-left: 40%;margin-top:10%;">
      <template #default="{ percentage }">
        <span class="percentage-value">{{ percentage }}s</span>
        <span class="percentage-label">正在跳转</span>
      </template>
    </el-progress>
    <el-button @click="go_back">点此返回</el-button>
  </div>
</template>

<script>
export default {
  name: "qnzs",
  data() {
    return {
      percentage: 5,
      time: 5,
      active: false
    };
  },
  created() {
    this.decrease();

  },
  methods: {
    decrease() {
      let me = this;
      let interval = window.setInterval(function () {
         //取整数
        me.percentage = Number((me.time / 1)).toFixed(0);
        --me.time; //每隔1s时间减1
        if (me.time < 0) {
          me.percentage = 0;
          me.time = 0;
          window.clearInterval(interval);
          if (this.active===false){
            window.location.href = 'http://jxnu.jx.qnzs.youth.cn/'
          }
        }
      }, 1000);
    },
    go_back(){
      this.active = true;
      this.$router.push('/home')
    }
  }
}
</script>

<style scoped>
.percentage-value {
  display: block;
  margin-top: 10px;
  font-size: 28px;
}
.percentage-label {
  display: block;
  margin-top: 10px;
  font-size: 12px;
}
.demo-progress .el-progress--line {
  margin-bottom: 15px;
  width: 350px;
}
.demo-progress .el-progress--circle {
  margin-right: 15px;
}

</style>
