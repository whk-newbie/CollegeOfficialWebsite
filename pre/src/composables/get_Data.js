import axios from 'axios';
import {onMounted} from 'vue'

export default function get_Data(data, choice) {
    const get_all_data = async () => {
        let url = '/api/';
        // let params = new URLSearchParams();
        let choices = {1: 'news', 2: 'infos', 3: "teacher"}
        url += choices[choice]

        console.log(url)
        const response = await axios.get(url);
        data.value = response.data;
        console.log(response.data.next)
        if (response.next != null) {
            getData(response.data.next.charAt(response.data.next.length - 1), data)
        }
    };

    onMounted(get_all_data);
    console.log(data.value)
}

function getData(number, data) {
    axios.get('api/news', {params: {page: number}})
        .then(
            response => {
                data.value = data.value.concat(response.data.results)
                // console.log(this.newsList)
                if (response.data.next !== null) {
                    this.getData(response.data.next.charAt(response.data.next.length - 1))
                }
            }
        )
}


function formatted_time(row, column) {
    const date = new Date(row[column.property]);
    // return date.toLocaleDateString()
    return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate()
}
