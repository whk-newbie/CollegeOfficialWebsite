<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-header>
        <el-button type="primary" @click="dialogFormVisible=true">我也要题意见</el-button>
        <el-dialog v-model="dialogFormVisible"
                   :lock-scroll="false" width="80%">
          <el-form :model="formData">
            <el-form-item label="昵称" prop="who"
                          :label-width="formLabelWidth">
              <el-input v-model="formData.who" type="text" clearable></el-input>
            </el-form-item>
            <el-form-item label="邮箱" prop="email"
                          :label-width="formLabelWidth">
              <el-input v-model="formData.email" type="text" clearable></el-input>
            </el-form-item>
            <el-form-item label="地址" prop="address"
                          :label-width="formLabelWidth">
              <el-input v-model="formData.address" type="text"></el-input>
            </el-form-item>
            <el-form-item label="标题" prop="title"
                          :label-width="formLabelWidth">
              <el-input v-model="formData.title" type="text" clearable></el-input>
            </el-form-item>
            <el-form-item label="意见内容" prop="content"
                          :label-width="formLabelWidth">
              <vue-editor v-model="formData.content"></vue-editor>
            </el-form-item>
            <el-form-item label="时间" prop="created_at"
                          :label-width="formLabelWidth">
              <el-time-picker v-model="formData.created_at" readonly="true"
                              format="HH:mm:ss" value-format="HH:mm:ss" :editable="true"
                              :label-width="formLabelWidth"></el-time-picker>
            </el-form-item>
          </el-form>
          <el-row :gutter="20">
            <el-col :span="6">
              <el-button type="primary">确 定</el-button>
            </el-col>
            <el-col :span="6">
              <el-button @click="dialogFormVisible = false">取 消</el-button>
            </el-col>
          </el-row>

        </el-dialog>
      </el-header>
      <el-main>
        <div class="card-header">
          <el-card v-for="(item,index) in comments" :key="index" class="box-card">
            <el-container>
              <el-header style="height:10%">【留言】{{ item.who }}</el-header>
              <el-main style="height:90%">
                <el-header style="height:10%">【内容】{{ item.title }}</el-header>
                <el-main style="height:90%">
                  {{ item.content }}
                </el-main>
              </el-main>
            </el-container>
          </el-card>
        </div>
      </el-main>
    </el-container>
  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header"
import Footer from "@/components/Footer"
import {ref} from 'vue'
import get_Data from "@/composables/get_Data";

export default {
  name: "MSBoard",
  components: {Header, Footer},

  setup() {
    const comments = ref('')
    get_Data(comments, '/api/board/')
    return {
      comments
    }
  },
  data() {
    return {
      dialogFormVisible: false,//弹出层默认为关闭
      //弹出层中的表单
      formData: {
        who: '',
        email: '',
        address: '',
        title: '',
        content: '',
        created_at: '',
      },
      formLabelWidth: '50px'
    }
  },
  methods: {}

}
</script>

<style scoped>
@import "~@/styles/body.css";

.el-header {
  font-size: 24px;
}

.el-main {
  font-size: 18px;
}

.box-card {
  width: 400px;
  margin-top: 20px;
  margin-bottom: 10px;
  margin-left: 30px;
  display: inline-block
}


.el-row {
  margin-bottom: 20px;
}

.el-row:last-child {
  margin-bottom: 0;
}

.el-col {
  border-radius: 4px;
}
</style>
