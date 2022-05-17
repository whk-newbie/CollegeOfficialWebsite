<template>
  <Header/>
  <div class="container">
    <el-container>
      <el-header>
        <el-button type="primary" @click="dialogFormVisible=true" style="margin-top:10px;margin-left: 10px;">我也要提建议</el-button>
        <el-dialog v-model="dialogFormVisible"
                   :lock-scroll="false" width="80%">
          <el-form :model="formData" :rules="rules">
            <el-form-item label="昵称" prop="who" :label-width="formLabelWidth">
              <el-input v-model="formData.who" type="text" clearable required></el-input>
            </el-form-item>
            <el-form-item label="邮箱" prop="email" :label-width="formLabelWidth">
              <el-input type="email" v-model="formData.email"  clearable required ></el-input>
            </el-form-item>
            <el-form-item label="地址" prop="address" :label-width="formLabelWidth">
              <el-input v-model="formData.address" type="text" clearable></el-input>
            </el-form-item>
            <el-form-item label="标题" prop="title" :label-width="formLabelWidth">
              <el-input v-model="formData.title" type="text" clearable required ></el-input>
            </el-form-item>
            <el-form-item label="意见内容" prop="content" :label-width="formLabelWidth">
              <el-input v-model="formData.content" type="textarea" :rows="10" required ></el-input>
            </el-form-item>
          </el-form>
          <el-row :gutter="20">
            <el-col :span="8">
              <el-button type="primary" @click="postms">确 定</el-button>
            </el-col>
            <el-col :span="8">
              <el-button @click="dialogFormVisible = false">取 消</el-button>
            </el-col>
          </el-row>
        </el-dialog>
      </el-header>
      <el-main>
        <div class="card-header">
          <el-card v-for="(item,index) in comments" :key="index" class="box-card">
            <el-container>
              <div class="avatar">
              <div class="angle_mark" v-if="item.is_reply">
                <span>{{val}}</span>
              </div>
              <el-header style="height:10%">【留言】{{ item.who }}</el-header>
              <el-main style="height:90%">
                <el-header style="height:10%">【内容】{{ item.title }}</el-header>
                <el-main style="height:90%">
                  {{ item.content }}
                </el-main>
              </el-main>
              </div>
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
import {ref,reactive} from 'vue'
import get_Data from "@/composables/get_Data";
import axios from "axios";

export default {
  name: "MSBoard",
  components: {Header, Footer},

  setup() {
    const comments = ref('')
    const val = "已收集"
    get_Data(comments, '/api/board/')
    const validatewho = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入昵称内容'))
      } else {
        callback()
      }
    }
    const validateEmail = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入邮箱'))
      } else {
        if (!/^([A-Za-z0-9_\-.])+@([A-Za-z0-9_\-.])+\.([A-Za-z]{2,4})$/.test(value)){
          callback(new Error("请输入正确的邮箱"))
        }
        callback()
      }
    }
    const validateTitle = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入标题'))
      } else {
        callback()
      }
    }
    const validateContent = (rule, value, callback) => {
      if (value === '') {
        callback(new Error("意见内容不能为空"))
      } else {
        callback()
      }
    }
    const rules = reactive({
      who:[{ validator: validatewho, trigger: 'blur' }],
      email:[{ validator: validateEmail, trigger: 'blur' }],
      title:[{ validator: validateTitle, trigger: 'blur' }],
      content:[{ validator: validateContent, trigger: 'blur' }],
    })
    return {
      comments,
      rules,
      val
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
      formLabelWidth: '80px'
    }
  },
  methods: {
    postms() {
      const time_now = new Date().toLocaleString()
      axios
          .post('/api/board/', {
            who: this.formData.who,
            email: this.formData.email,
            address: this.formData.address,
            title: this.formData.title,
            content: this.formData.content,
            created_at: time_now
          })
          .then(
              this.reload()
          )
      this.dialogFormVisible = false
    }
  }

}
</script>

<style scoped>
@import "~@/styles/body.css";
.el-form-item{
  font-family: 黑体,serif ;
}

.el-form-item .el-input {
  width: 40%;
}

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
  display: inline-block;
  border-radius: 15px;
  padding:0;
}


.el-row {
  height: 30px;
  margin-bottom: 20px;

}

.el-row:last-child {
  margin-bottom: 0;
}

.el-col {
  border-radius: 4px;
  margin-left: 10%;
  font-family: "Arial Black",serif ;
}


.avatar {
  width: 400px;
  height: 400px;
  overflow: hidden;
  position: relative;
}
.avatar .angle_mark {
  position: absolute;
  top: -50px;
  right: -50px;
  background-color: #1a8dc2;
  width: 100px;
  height: 100px;
  transform: rotate(45deg);
}
.avatar .angle_mark span {
  position: absolute;
  display: inline-block;
  color: #fff;
  width: 100%;
  bottom: 0;
  left: 0;
  text-align: center;
}
</style>
