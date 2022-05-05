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
import Tmorality from '@/views/teachers/Tmorality'
import TmoralityDetail from '@/views/teachers/TmoralityDetail'
import Professor from "@/views/teachers/Professor"
import Tutor from "@/views/teachers/Tutor"
import Enrollful from "@/views/teachers/Enrollful"

import Enrollment from '@/views/EnrollmentAndEmployment/Enrollment'
import Employment from '@/views/EnrollmentAndEmployment/Employment'

import PartyBuilding from '@/views/Party/PartyBuilding'

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
        name: 'education',
        component: Second,
        meta: {
            is_show: true,
            title: "人才培养"
        },
        children: [
            {
                path: '/education/graduate',
                name: "graduate_1",
                component: () => import('@/views/education/Graduate'),
                meta: {
                    is_show: true,
                    title: "本科生教育"
                },
                children: []
            },
            {
                path: '/education/undergraduate',
                name: "undergraduate_1",
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
        path: '/teacherMorality',
        name: 'teacherMorality',
        component: Tmorality,
        meta: {
            is_show: true,
            title: '师德师风'
        },
        children: []
    },
    {
        path: '/enrollAndEmploy',
        name: "enrollAndEmploy",
        component: Second,
        meta: {
            is_show: true,
            title: "招生就业"
        },
        children: [{
            path: '/graduate',
            name: 'graduate21',
            component: Second,
            meta: {
                is_show: true,
                title: '本科生'
            },
            children: [{
                path: '/graduate/enrollment',
                name: "enrollment1",
                component: Enrollment,
                meta: {
                    is_show: true,
                    title: "招生"
                },
            }, {
                path: '/graduate/employment',
                name: "employment1",
                component: Employment,
                meta: {
                    is_show: true,
                    title: "就业"
                },

            }]
        }, {
            path: '/undergraduate',
            name: 'undergraduate22',
            component: Second,
            meta: {
                is_show: true,
                title: '研究生'
            },
            children: [{
                path: '/undergraduate/enrollment',
                name: "Enrollment1",
                component: Enrollment,
                meta: {
                    is_show: true,
                    title: "招生"
                },

            }, {
                path: '/undergraduate/employment',
                name: "Employment2",
                component: Employment,
                meta: {
                    is_show: true,
                    title: "就业"
                },
            }]
        }]
    },
    {
        path: '/party',
        name: 'Party',
        component: PartyBuilding,
        meta: {
            is_show: true,
            title: '党建工作'
        },
        children: []
    },
    {
        path: '/group',
        name: 'group',
        component: Second,
        meta: {
            is_show: true,
            title: "团学工作"
        },
        children: []
    },
    {
        path: '/Laboratory',
        name: 'exCenter',
        component: Second,
        meta: {
            is_show: true,
            title: "实验中心"
        },
        children: [
            {
                path: '/Laboratory/laboratory',
                name: "laboratory",
                component: LaboratoryOverView,
                meta: {
                    is_show: true,
                    title: "中心概况",
                },
                children: []
            },
            {
                path: '/Laboratory/gerneral',
                name: "gerneral",
                component: Gerneral,
                meta: {
                    is_show: true,
                    title: "综合实验室",
                },
                children: []
            },
            {
                path: '/Laboratory/hardware',
                name: "hardware",
                component: Hardware,
                meta: {
                    is_show: true,
                    title: "硬件实验室",
                },
                children: []
            },
            {
                path: '/Laboratory/network',
                name: "network",
                component: Network,
                meta: {
                    is_show: true,
                    title: "网络实验室",
                },
                children: []
            },
            {
                path: '/Laboratory/IOT',
                name: "IOT",
                component: IOT,
                meta: {
                    is_show: true,
                    title: "物联网实验室",
                },
                children: []
            },
            {
                path: '/Laboratory/embedded',
                name: "embedded",
                component: Embedded,
                meta: {
                    is_show: true,
                    title: "嵌入式实验室",
                },
                children: []
            },

        ]
    },
    {
        path: '/downloadCenter',
        name: 'downloadCenter',
        component: Second,
        meta: {
            is_show: true,
            title: "下载中心"
        },
        children: [
            {
                path: '/downloadCenter/materials',
                name: "materials",
                component: () => import('@/views/downloadCenter/downloadCenter'),
                meta: {
                    is_show: true,
                    title: "学习资料",
                },
                children: []
            },
            {
                path: '/downloadCenter/application',
                name: "application",
                component: () => import('@/views/downloadCenter/application'),
                meta: {
                    is_show: true,
                    title: "软件下载",
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
