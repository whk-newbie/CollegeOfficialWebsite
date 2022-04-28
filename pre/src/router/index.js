import {createRouter, createWebHashHistory} from 'vue-router'
import Home from "@/views/Home.vue"
import CollegeOverview from "@/views/CollegeOverview/CollegeOverview"
import Leaders from "@/views/CollegeOverview/Leaders"
import Organization from "@/views/CollegeOverview/Organization"
import NewsCenter from "@/views/news/NewsCenter"
import Information from "@/views/news/Information"
import InfosDetail from '@/views/news/InforsDetail'
import NewsDetail from "@/views/news/NewsDetail"
import Teachers from "@/views/teachers/Teachers"
import TeacherDetail from '@/views/teachers/TeacherDetail'
import Tmorality from '@/views/teachers/Tmorality'
import TmoralityDetail from '@/views/teachers/TmoralityDetail'
import Professor from "@/views/teachers/Professor"
import Tutor from "@/views/teachers/Tutor"
import Enrollful from "@/views/teachers/Enrollful"
import LaboratoryOverView from "@/views/Laboratory/LaboratoryOverView"
import Gerneral from "@/views/Laboratory/Gerneral"
import Hardware from "@/views/Laboratory/Hardware"
import IOT from "@/views/Laboratory/IOT"
import Network from "@/views/Laboratory/Network"
import Embedded from "@/views/Laboratory/Embedded"

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
        path: "/news/:id",
        name: "NewsDetail",
        component: NewsDetail,
    },
    {
        path: '/information',
        name: 'information',
        component: Information
    },
    {
        path: '/information/:id',
        name: 'InfosDetail',
        component: InfosDetail
    },
    {
        path: '/teacher',
        name: 'teacher',
        component: Teachers
    },
    {
        path: "/teachers/:id",
        name: 'TeacherDetail',
        component: TeacherDetail
    },
    {
        path: '/Tmorality',
        name: 'Tmorality',
        component: Tmorality
    },
    {
        path: '/Tmorality/:id',
        name: 'TmoralityDetail',
        component: TmoralityDetail
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
    },
    {
        path: '/laboratory',
        name: 'laboratoryOverView',
        component: LaboratoryOverView
    },
    {
        path: '/gerneral',
        name: 'Gerneral',
        component: Gerneral
    },
    {
        path: '/hardware',
        name: 'Hardware',
        component: Hardware
    },
    {
        path: '/network',
        name: "Network",
        component: Network
    },
    {
        path: '/IOT',
        name: 'IOT',
        component: IOT
    },
    {
        path: '/embedded',
        name: 'Embedded',
        component: Embedded
    }

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
