import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// 引入element-ui
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css'
import locale from 'element-plus/lib/locale/lang/zh-cn'
import 'default-passive-events'
// 使用路由
createApp(App).use(ElementPlus,{locale}).use(router).mount('#app')
