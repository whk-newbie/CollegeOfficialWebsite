import {createRouter, createWebHashHistory} from 'vue-router'
import Home from "@/views/Home.vue"
import CollegeOverview from "@/views/CollegeOverview";
import Leaders from "@/views/Leaders";
import Organization from "@/views/Organization";
import Information from "@/views/Information";
import NewsCenter from "@/views/NewsCenter";
import ImageNews from "@/views/ImageNews";

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
        path: '/News',
        name: 'News',
        component: NewsCenter
    },
    {
        path: '/ImageNews',
        name: 'ImageNews',
        component: ImageNews
    },
    {
        path: '/Information',
        name: 'Information',
        component: Information
    },

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
