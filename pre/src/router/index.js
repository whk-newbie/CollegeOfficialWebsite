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
            path: '/newsAndinfos/newscenter',
            name: '/newscenter',
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
                component: Second,
                meta: {
                    is_show: true,
                    title: "本科生教育"
                },
                children: [{
                    path: '/education/graduate/major',
                    name: "major1",
                    component: () => import ("@/views/education/Graduate"),
                    meta: {
                        is_show: true,
                        title: "专业介绍"
                    },
                    children: []
                }, {
                    path: '/education/graduate/plan',
                    name: "plan1",
                    component: () => import ("@/views/education/Graduate"),
                    meta: {
                        is_show: true,
                        title: "培养方案"
                    },
                    children: []
                }, {
                    path: '/education/graduate/achieve',
                    name: "achieve",
                    component: () => import ("@/views/education/Graduate"),
                    meta: {
                        is_show: true,
                        title: "教学成果"
                    },
                    children: []
                }, {
                    path: '/education/graduate/course',
                    name: "course",
                    component: () => import ("@/views/education/Graduate"),
                    meta: {
                        is_show: true,
                        title: "精品课程"
                    },
                    children: []
                },
                ]
            },
            {
                path: '/education/undergraduate',
                name: "undergraduate_1",
                component: Second,
                meta: {
                    is_show: true,
                    title: "研究生教育"
                },
                children: [{
                    path: '/education/undergraduate/major',
                    name: "major2",
                    component: () => import('@/views/education/Undergraduate'),
                    meta: {
                        is_show: true,
                        title: "学位点介绍"
                    },
                    children: []
                },
                    {
                        path: '/education/undergraduate/plan',
                        name: "plan2",
                        component: () => import('@/views/education/Undergraduate'),
                        meta: {
                            is_show: true,
                            title: "培养方案"
                        },
                        children: []
                    },{
                        path: '/education/undergraduate/notice',
                        name: "notice",
                        component: () => import('@/views/education/Undergraduate'),
                        meta: {
                            is_show: true,
                            title: "信息公告"
                        },
                        children: []
                    }]
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
        path: '/PartyLearning',
        name: 'PartyLearning',
        component: () => import("@/views/Party/PartyLearning"),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/thematic',
        name: 'thematic',
        component: () => import("@/views/Party/ThematicEducation"),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/newsDetail/:id',
        name: 'newsDetail',
        component: () => import('@/views/PageDetail/NewsDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/infosDetail/:id',
        name: 'infosDetail',
        component: () => import('@/views/PageDetail/InforsDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/TeacherDetail/:id',
        name: 'TeacherDetail',
        component: () => import('@/views/PageDetail/TeacherDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/majorDetail/:id',
        name: 'majorDetail',
        component: () => import('@/views/PageDetail/majorDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/planDetail/:id',
        name: 'planDetail',
        component: () => import('@/views/PageDetail/planDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/teachingDetail/:id',
        name: 'teachingDetail',
        component: () => import('@/views/PageDetail/teachingDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/courseDetail/:id',
        name: 'courseDetail',
        component: () => import('@/views/PageDetail/courseDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/noticeDetail/:id',
        name: 'noticeDetail',
        component: () => import('@/views/PageDetail/noticeDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/researchDetail/:id',
        name: 'researchDetail',
        component: () => import('@/views/PageDetail/researchDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/institutionDetail/:id',
        name: 'institutionDetail',
        component: () => import('@/views/PageDetail/institutionDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/achievementsDetail/:id',
        name: 'achievementsDetail',
        component: () => import('@/views/PageDetail/achievementsDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/TmoralityDetail/:id',
        name: 'TmoralityDetail',
        component: () => import('@/views/PageDetail/TmoralityDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/enrollmentDetail/:id',
        name: 'enrollmentDetail',
        component: () => import('@/views/PageDetail/enrollmentDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/employmentDetail/:id',
        name: 'employmentDetail',
        component: () => import('@/views/PageDetail/employmentDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path: '/buildingDetail/:id',
        name: 'buildingDetail',
        component: () => import('@/views/PageDetail/buildingDetail'),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path:'/groupnewsDetail/:id',
        name: "groupnewsDetail",
        component: () => import("@/views/PageDetail/groupnewsDetail"),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path:'/groupDetail/:id',
        name: "groupDetail",
        component: () => import("@/views/PageDetail/groupDetail"),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path:'/partyDetail/:id',
        name: "partyDetail",
        component: () => import("@/views/PageDetail/partyDetail"),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path:'/honorDetail/:id',
        name: "honorDetail",
        component: () => import("@/views/PageDetail/honorDetail"),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path:'/Download/:id',
        name: "Download",
        component: () => import("@/views/Download"),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path:'/fileleanDetail/:id',
        name: "fileleanDetail",
        component: () => import("@/views/PageDetail/PartyLearnDetail"),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path:'/filelearnDetail/:id',
        name: "filelearnDetail",
        component: () => import("@/views/PageDetail/filelearnDetail"),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path:'/inforDetail/:id',
        name: "inforDetail",
        component: () => import("@/views/PageDetail/inforDetail"),
        meta: {
            is_show: false,
        },
        children: null
    },
    {
        path:'/reportDetail/:id',
        name: "reportDetail",
        component: () => import("@/views/PageDetail/reportDetail"),
        meta: {
            is_show: false,
        },
        children: null
    },

]


const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export default router
