import axios from 'axios';
import{onMounted, watch} from 'vue'
export default function getPages(urls,pages,route){
    const getPage = async () => {
        let url = urls;
        // console.log(route.fullPath)
        url += route.params.id
        const response = await axios.get(url);
        pages.value = response.data
    }
    onMounted(getPage);
    watch(route, getPage);
}
