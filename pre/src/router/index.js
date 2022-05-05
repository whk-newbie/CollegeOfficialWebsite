import {createRouter, createWebHashHistory} from 'vue-router'

import Second from '@/views/CollegeOverview/Second'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import("@/views/Home.vue"),
        meta: {
            is_show: false,
            title: '首页',
        },
        children: null
    },
    {
        path: '/home',
        name: 'home',
        component: () => import("@/views/Home.vue"),
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
            component: () => import("@/views/CollegeOverview/CollegeOverview"),
            meta: {
                is_show: true,
                title: "学院简介"
            },
            children: []
        }, {
            path: '/collegeOverView/leaders',
            name: 'leaders',
            component: () => import("@/views/CollegeOverview/Leaders"),
            meta: {
                is_show: true,
                title: "学院领导"
            },
            children: []
        }, {
            path: '/collegeOverView/organization',
            name: 'organization',
            component: () => import("@/views/CollegeOverview/Organization"),
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
                    component: () => import("@/views/teachers/Teachers"),
                    meta: {
                        is_show: true,
                        title: "专任教师"
                    },
                },
                {
                    path: '/teacher/professor',
                    name: 'professor',
                    component: () => import("@/views/teachers/Professor"),
                    meta: {
                        is_show: true,
                        title: "教授队伍"
                    },
                },
                {
                    path: '/teacher/tutor',
                    name: 'tutor',
                    component: () => import("@/views/teachers/Tutor"),
                    meta: {
                        is_show: true,
                        title: "硕士生导师"
                    },
                },
                {
                    path: '/teacher/enrollful',
                    name: 'enrollful',
                    component: () => import("@/views/teachers/Enrollful"),
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
            component: () => import("@/views/news/NewsCenter"),
            meta: {
                is_show: true,
                title: "学院新闻"
            },
            children: []
        },
            {
                path: '/newsAndinfos/inforsCenter',
                name: 'infosCenter',
                component: () => import("@/views/news/Information"),
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
        component: () => import('@/views/teachers/Tmorality'),
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
                component: () => import('@/views/EnrollmentAndEmployment/Enrollment'),
                meta: {
                    is_show: true,
                    title: "招生"
                },
            }, {
                path: '/graduate/employment',
                name: "employment1",
                component: () => import('@/views/EnrollmentAndEmployment/Employment'),
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
                component: () => import('@/views/EnrollmentAndEmployment/Enrollment'),
                meta: {
                    is_show: true,
                    title: "招生"
                },

            }, {
                path: '/undergraduate/employment',
                name: "Employment2",
                component: () => import('@/views/EnrollmentAndEmployment/Employment'),
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
        component: () => import('@/views/Party/PartyBuilding'),
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
        children: [
            {
                path: '/group/news',
                name: "groupnews",
                component: () => import("@/views/group/GroupNews"),
                meta: {
                    is_show: true,
                    title: '学工新闻'
                },
                children: []
            },
            {
                path: '/group/qnzs',
                name: "qnzs",
                component: () => import("@/views/group/qnzs"),
                meta: {
                    is_show: true,
                    title: '青年之声江西师范大学'
                },
                children: []
            }, {
                path: '/group/group',
                name: "group",
                component: () => import("@/views/group/Group"),
                meta: {
                    is_show: true,
                    title: '团学组织'
                },
                children: []
            }, {
                path: '/group/service',
                name: "service",
                component: () => import("@/views/group/Service"),
                meta: {
                    is_show: true,
                    title: '党员服务'
                },
                children: []
            }, {
                path: '/group/management',
                name: "management",
                component: () => import("@/views/group/Management"),
                meta: {
                    is_show: true,
                    title: '管理制度'
                },
                children: []
            }, {
                path: '/group/honor',
                name: "grouphonor",
                component: () => import('@/views/group/Honor'),
                meta: {
                    is_show: true,
                    title: '荣誉室'
                },
                children: []
            }
        ]
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
                component: () => import("@/views/Laboratory/LaboratoryOverView"),
                meta: {
                    is_show: true,
                    title: "中心概况",
                },
                children: []
            },
            {
                path: '/Laboratory/gerneral',
                name: "gerneral",
                component: () => import("@/views/Laboratory/Gerneral"),
                meta: {
                    is_show: true,
                    title: "综合实验室",
                },
                children: []
            },
            {
                path: '/Laboratory/hardware',
                name: "hardware",
                component: () => import("@/views/Laboratory/Hardware"),
                meta: {
                    is_show: true,
                    title: "硬件实验室",
                },
                children: []
            },
            {
                path: '/Laboratory/network',
                name: "network",
                component: () => import("@/views/Laboratory/Network"),
                meta: {
                    is_show: true,
                    title: "网络实验室",
                },
                children: []
            },
            {
                path: '/Laboratory/IOT',
                name: "IOT",
                component: () => import("@/views/Laboratory/IOT"),
                meta: {
                    is_show: true,
                    title: "物联网实验室",
                },
                children: []
            },
            {
                path: '/Laboratory/embedded',
                name: "embedded",
                component: () => import("@/views/Laboratory/Embedded"),
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
        component: () => import("@/views/news/NewsDetail"),
        meta: {is_show: false,},
        children: null
    },
    {
        path: '/infosdetail/:id',
        name: 'InfosDetail',
        component: () => import('@/views/news/InforsDetail'),
        meta: {is_show: false,},
        children: null
    },
    {
        path: '/teacherDetail/:id',
        name: 'TeacherDetail',
        component: () => import('@/views/teachers/TeacherDetail'),
        meta: {is_show: false,},
        children: null
    },
    {
        path: '/TmoralityDetail/:id',
        name: 'TmoralityDetail',
        component: () => import('@/views/teachers/TmoralityDetail'),
        meta: {is_show: false,},
        children: null
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
