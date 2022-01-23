import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// 引入element-ui
import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css'
createApp(App).use(ElementPlus).use(router).mount('#app')
