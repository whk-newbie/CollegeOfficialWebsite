<template>
  <Header/>
  <div class="body">
    <el-container>
      <el-aside width="20%">
        <PTTE/>
      </el-aside>
      <el-container>
        <el-main>
          <el-breadcrumb separator="/">
            <el-breadcrumb-item>当前位置:</el-breadcrumb-item>
            <el-breadcrumb-item :to="{ path: '/' }">主页</el-breadcrumb-item>
            <el-breadcrumb-item :to="{ path: '/CollegeOverview'}">学院概况</el-breadcrumb-item>
            <el-breadcrumb-item>师资队伍</el-breadcrumb-item>
            <el-breadcrumb-item>专任教师</el-breadcrumb-item>
          </el-breadcrumb>
          <el-table :data="tableData" style="width: 100%" height="850px" size="small" border="true">
            <el-table-column prop="list1" label="计算机科学系" width="150"/>
            <el-table-column prop="list2" label="计算机技术系" width="150"/>
            <el-table-column prop="list3" label="计算机网络工程系" width="150"/>
            <el-table-column prop="list4" label="信息技术系" width="150"/>
            <el-table-column prop="list5" label="物联网系" width="150"/>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header"
import Footer from "@/components/Footer"
import PTTE from "@/components/PTTE"

export default {
  name: "Teachers",
  components: {Header, Footer, PTTE},
  data() {
    return {
      tableData: [{'list1': '程 艳', 'list2': '邓华锋', 'list3': '邓少辉', 'list4': '敖小玲', 'list5': '雷浩鹏'},
        {'list1': '程柏良', 'list2': '胡全连', 'list3': '方剑英', 'list4': '傅清平', 'list5': '雷震春'},
        {'list1': '冯 悦', 'list2': '江爱文', 'list3': '郭 帆', 'list4': '甘朝红', 'list5': '李汉曦'},
        {'list1': '化志章', 'list2': '李宏伟', 'list3': '胡 蕾', 'list4': '李建元', 'list5': '刘长红'},
        {'list1': '揭安全', 'list2': '李云洪', 'list3': '胡珍新', 'list4': '李雪斌', 'list5': '徐 凡'},
        {'list1': '李茂西', 'list2': '刘 超', 'list3': '黄林颖', 'list4': '廖云燕', 'list5': '叶继华'},
        {'list1': '李云清', 'list2': '黄 箐', 'list3': '李 佳', 'list4': '刘 洪', 'list5': '张光河'},
        {'list1': '刘建明', 'list2': '马明磊', 'list3': '罗 芬', 'list4': '罗 坚', 'list5': '左家莉'},
        {'list1': '卢家兴', 'list2': '曲彦文', 'list3': '万宇文', 'list4': '罗 玮', 'list5': ''},
        {'list1': '彭 云', 'list2': '谢旭升', 'list3': '汪文义', 'list4': '倪海英', 'list5': ''},
        {'list1': '漆志群', 'list2': '叶茂盛', 'list3': '王明文', 'list4': '聂伟强', 'list5': ''},
        {'list1': '石海鹤', 'list2': '张练兴', 'list3': '王晓庆', 'list4': '万 芳', 'list5': ''},
        {'list1': '万剑怡', 'list2': '郑 燚', 'list3': '熊建华', 'list4': '王 萍', 'list5': ''},
        {'list1': '万中英', 'list2': '周 新', 'list3': '熊晓华', 'list4': '王昌晶', 'list5': ''},
        {'list1': '王 岚', 'list2': '周 勇', 'list3': '周新宇', 'list4': '王国纬', 'list5': ''},
        {'list1': '吴水秀', 'list2': '周琪云', 'list3': '曾锦山', 'list4': '王丽君', 'list5': ''},
        {'list1': '杨庆红', 'list2': '朱明华', 'list3': '', 'list4': '吴克捷', 'list5': ''},
        {'list1': '钟林辉', 'list2': '曾纪国', 'list3': '', 'list4': '熊 刚', 'list5': ''},
        {'list1': '左正康', 'list2': '', 'list3': '', 'list4': '徐 培', 'list5': ''},
        {'list1': '', 'list2': '', 'list3': '', 'list4': '徐文胜', 'list5': ''},
        {'list1': '', 'list2': '', 'list3': '', 'list4': '杨印根', 'list5': ''},
        {'list1': '', 'list2': '', 'list3': '', 'list4': '张 婕', 'list5': ''
        }]
      ,
    }
  }
}
</script>

<style scoped>
.body {
  margin: 2% 2% 2% 10%;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}
.el-breadcrumb {
  margin-top: 10px;
  margin-left: 10px;
  height:5%;
  font-family: 微软雅黑;
}

.el-aside {
  background-color: #92f6ce;
}
.el-main {
  height: 900px;
}
.el-table {
  margin-left: 20%;
}

</style>
