import {createRouter, createWebHashHistory} from 'vue-router'
import Home from "@/views/Home.vue"
import CollegeOverview from "@/views/CollegeOverview/CollegeOverview"
import Leaders from "@/views/CollegeOverview/Leaders"
import Organization from "@/views/CollegeOverview/Organization"
import NewsCenter from "@/views/news/NewsCenter"
import Information from "@/views/news/Information"
import ImageNews from "@/views/news/ImageNews"
import Teachers from "@/views/teachers/Teachers"
import Professor from "@/views/teachers/Professor"
import Tutor from "@/views/teachers/Tutor"
import Enrollful from "@/views/teachers/Enrollful"

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
    {
        path: '/teacher',
        name: 'teacher',
        component: Teachers
    },
    {
        path: '/professor',
        name: 'professor',
        component: Professor
    },
    {
        path: '/tutor',
        name: 'tutor',
        component: Tutor
    },
    {
        path: '/enrollful',
        name: 'enrollful',
        component: Enrollful
    }

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
