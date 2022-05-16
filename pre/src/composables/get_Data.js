import axios from 'axios';
import {onMounted} from 'vue'

export default function get_Data(data, url) {
    const get_all_data = async () => {
        getList(url, data)

    };

    onMounted(get_all_data);
    console.log(data.value)
}


function getList(url, data) {
    axios
        .get(url)
        .then(response => {
                (data.value = response.data.results)
            if (response.data.next !== null) {
                getData(response.data.next.charAt(response.data.next.length - 1), url, data)
            }
        })
}

function getData(number, url, data) {
    axios.get(url, {params: {page: number}})
        .then(
            response => {
                data.value = data.value.concat(response.data.results)
                // console.log(this.newsList)
                if (response.data.next !== null) {
                    this.getData(response.data.next.charAt(response.data.next.length - 1), url, data)
                }
            }
        )
}


