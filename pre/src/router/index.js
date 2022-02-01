import {createRouter, createWebHashHistory} from 'vue-router'
import Home from "@/views/Home.vue"
import CollegeOverview from "@/views/CollegeOverview/CollegeOverview"
import Leaders from "@/views/CollegeOverview/Leaders"
import Organization from "@/views/CollegeOverview/Organization"
import NewsCenter from "@/views/news/NewsCenter"
import Information from "@/views/news/Information"
import ImageNews from "@/views/news/ImageNews"
const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/CollegeOverview',
        name: 'CollegeOverview',
        component: CollegeOverview
    },
    {
        path: '/leaders',
        name: 'leaders',
        component: Leaders
    },
    {
        path: '/organization',
        name: 'organization',
        component: Organization
    },
    {
        path: '/news',
        name: 'news',
        component: NewsCenter
    },
    {
        path: '/imagenews',
        name: 'imagenews',
        component: ImageNews
    },
    {
        path: '/information',
        name: 'information',
        component: Information
    },

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
