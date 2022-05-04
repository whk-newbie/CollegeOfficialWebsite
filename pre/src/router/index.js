import {createRouter, createWebHashHistory} from 'vue-router'
import Home from "@/views/Home.vue"
import Second from '@/views/CollegeOverview/Second'
import CollegeOverview from "@/views/CollegeOverview/CollegeOverview"
import Leaders from "@/views/CollegeOverview/Leaders"
import Organization from "@/views/CollegeOverview/Organization"

import NewsCenter from "@/views/news/NewsCenter"
import Information from "@/views/news/Information"
import InfosDetail from '@/views/news/InforsDetail'
import NewsDetail from "@/views/news/NewsDetail"


import Teachers from "@/views/teachers/Teachers"
import TeacherDetail from '@/views/teachers/TeacherDetail'
import TmoralityDetail from '@/views/teachers/TmoralityDetail'
import Professor from "@/views/teachers/Professor"
import Tutor from "@/views/teachers/Tutor"
import Enrollful from "@/views/teachers/Enrollful"
//
// import test from "@/views/education/test"
//
// import LaboratoryOverView from "@/views/Laboratory/LaboratoryOverView"
// import Gerneral from "@/views/Laboratory/Gerneral"
// import Hardware from "@/views/Laboratory/Hardware"
// import IOT from "@/views/Laboratory/IOT"
// import Network from "@/views/Laboratory/Network"
// import Embedded from "@/views/Laboratory/Embedded"

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: {
            is_show: false,
            title: '首页',
        },
        children: null
    },
    {
        path: '/home',
        name: 'home',
        component: Home,
        meta: {
            is_show: true,
            title: "首页",
            children: 0
        },
        children: []
    },
    {
        path: '/collegeOverView',
        name: 'collegeOverView',
        component: Second,
        meta: {
            is_show: true,
            title: "学院概况",
            children: 1
        },
        children: [{
            path: '/collegeOverView/overview',
            name: 'collegeOverViewoverview',
            component: CollegeOverview,
            meta: {
                is_show: true,
                title: "学院简介"
            },
            children: []
        }, {
            path: '/collegeOverView/leaders',
            name: 'leaders',
            component: Leaders,
            meta: {
                is_show: true,
                title: "学院领导"
            },
            children: []
        }, {
            path: '/collegeOverView/organization',
            name: 'organization',
            component: Organization,
            meta: {
                is_show: true,
                title: "内设机构"
            },
            children: []
        }, {
            path: '/teacher',
            name: 'teacher',
            component: Second,
            meta: {
                is_show: true,
                title: "师资力量"
            },
            children: [
                {
                    path: '/teacher/teachers',
                    name: 'teachers',
                    component: Teachers,
                    meta: {
                        is_show: true,
                        title: "专任教师"
                    },
                },
                {
                    path: '/teacher/professor',
                    name: 'professor',
                    component: Professor,
                    meta: {
                        is_show: true,
                        title: "教授队伍"
                    },
                },
                {
                    path: '/teacher/tutor',
                    name: 'tutor',
                    component: Tutor,
                    meta: {
                        is_show: true,
                        title: "硕士生导师"
                    },
                },
                {
                    path: '/teacher/enrollful',
                    name: 'enrollful',
                    component: Enrollful,
                    meta: {
                        is_show: true,
                        title: "专任教师"
                    },
                },
            ]
        },]
    },
    {
        path: '/newsAndinfos',
        name: 'newsAndinfos',
        component: Second,
        meta: {
            is_show: true,
            title: "新闻公告",
        },
        children: [{
            path: '/newsAndinfos/overview',
            name: '/collegeOverViewoverview',
            component: NewsCenter,
            meta: {
                is_show: true,
                title: "学院新闻"
            },
            children: []
        },
            {
                path: '/newsAndinfos/inforsCenter',
                name: 'infosCenter',
                component: Information,
                meta: {
                    is_show: true,
                    title: "通知公告"
                },
                children: []
            }]
    },
    {
        path: '/education',
        name: 'deucation',
        component: Second,
        meta: {
            is_show: true,
            title: "人才培养"
        },
        children: [
            {
                path: '/education/graduate',
                name: "graduate",
                component: () => import('@/views/education/Graduate'),
                meta: {
                    is_show: true,
                    title: "本科生教育"
                },
                children: []
            },
            {
                path: '/education/undergraduate',
                name: "undergraduate",
                component: () => import('@/views/education/Undergraduate'),
                meta: {
                    is_show: true,
                    title: "研究生教育"
                },
                children: []
            }
        ]
    },
    {
        path: '/research',
        name: 'research',
        component: Second,
        meta: {
            is_show: true,
            title: '科学研究'
        },
        children: [
            {
                path: '/research/research',
                name: 'researchers',
                component: () => import('@/views/research/research'),
                meta: {
                    is_show: true,
                    title: '科研动态'
                },
                children: []
            },
            {
                path: '/research/institutions',
                name: 'insitutions',
                component: () => import('@/views/research/institutions'),
                meta: {
                    is_show: true,
                    title: '科研机构'
                },
                children: []
            },
            {
                path: '/research/achievement',
                name: 'achievement',
                component: () => import('@/views/research/achievement'),
                meta: {
                    is_show: true,
                    title: '科研成果'
                },
                children: []
            },
        ]
    },
    {
        path: '/newdetail/:id',
        name: 'NewsDetail',
        component: NewsDetail,
        meta: {is_show: false,},
        children: null
    },
    {
        path: '/infosdetail/:id',
        name: 'InfosDetail',
        component: InfosDetail,
        meta: {is_show: false,},
        children: null
    },
    {
        path: '/teacherDetail/:id',
        name: 'TeacherDetail',
        component: TeacherDetail,
        meta: {is_show: false,},
        children: null
    },
    {
        path: '/TmoralityDetail/:id',
        name: 'TmoralityDetail',
        component: TmoralityDetail,
        meta: {is_show: false,},
        children: null
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
