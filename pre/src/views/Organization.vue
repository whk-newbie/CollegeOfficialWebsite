<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-aside width="20%">
        <CLO/>
      </el-aside>
      <el-container>
        <el-header><p>内设机构</p></el-header>
        <el-main>
          <el-tabl v-for="item in tableData" :key="item.department">
            <el-container>
              <el-header>{{item.department}}</el-header>
              <el-main>
                <el-table :data="item.names" style="width: 100%"
                          border>
                  <el-table-column label="系/部门" prop="name"></el-table-column>
                  <el-table-column label="联系人" prop="hosts"></el-table-column>
                  <el-table-column label="联系电话" prop="phonenumber"></el-table-column>
                  <el-table-column label="办公地址" prop="locat"></el-table-column>
                </el-table>
              </el-main>
            </el-container>
          </el-tabl>

        </el-main>
      </el-container>
    </el-container>

  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import CLO from "@/components/CLO"

export default {
  name: "Organization",
  components: {Header, Footer, CLO},
  data() {
    return {
      tableData: [{
        "id": "1",
        "department": "系",
        "names": [{"name": "计算机科学系", "hosts": "", "phonenumber": "", "locat": ""},
          {"name": "计算机技术系", "hosts": "", "phonenumber": "", "locat": ""},
          {"name": "计算机网络工程系", "hosts": "", "phonenumber": "", "locat": ""},
          {"name": "信息技术系", "hosts": "", "phonenumber": "", "locat": ""},
          {"name": "物联网工程系", "hosts": "", "phonenumber": "", "locat": ""},
          {"name": "实验中心", "hosts": "余彤仑", "phonenumber": "88120417", "locat": "先驌楼4-4316"},
        ]
      },
        {
          "id": "2",
          "department": "行政管理",
          "names": [
            {"name": "院主任办公室", "hosts": "毛阳芳", "phonenumber": "88120411", "locat": "先驌楼4-4217"},
            {"name": "院办公室", "hosts": "邓 涛", "phonenumber": "88120410", "locat": "先驌楼4-3228"},
            {"name": "研究生办公室", "hosts": "乐 兵", "phonenumber": "88120860", "locat": "先驌楼4-4204"},
            {"name": "资料室", "hosts": "黄 勤", "phonenumber": "", "locat": "先驌楼4-3225"},
            {"name": "院团委书记办公室", "hosts": "李海燕", "phonenumber": "88133728", "locat": "先驌楼4-4205"},
            {"name": "辅导员办公室", "hosts": "", "phonenumber": "88120416", "locat": "先驌楼4-4206"},
          ]
        },
        {
          "id": "3",
          "department": "党务工作",
          "names": [{"name": "教工党支部", "hosts": "", "phonenumber": "", "locat": ""},
            {"name": "本科生党支部", "hosts": "", "phonenumber": "", "locat": ""},
            {"name": "研究生党支部", "hosts": "", "phonenumber": "", "locat": ""},
          ]
        }
      ],
    }
  }
}
</script>

<style scoped>
.container {
  margin: 2% 2% 2% 10%;
  width: 80%;
  box-shadow: 4px 4px 15px #dad9d9;
}

.el-aside {
  background-color: #92f6ce;
}


.el-header {
  text-align: -webkit-left;
  font-size: 24px;
  font-style: normal;
  font-family: 仿宋_GB2312;
}

.el-header > p {
  margin-top: 10px;
  margin-left: 5px;
  color: gray;
}
</style>
