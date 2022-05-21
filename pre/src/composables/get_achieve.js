import { getList } from "@/composables/get_Data"
import {onMounted,ref} from 'vue';

export default function get_achieve(data) {
    const get_all_data = async () => {
        getList( '/api/group/honor/?photo=1',data, ref(0))
    }
    onMounted(get_all_data)
}
