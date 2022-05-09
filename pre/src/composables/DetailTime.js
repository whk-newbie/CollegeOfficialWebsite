export default function Detail(time) {
    const date = new Date(time);
    // return date.toLocaleDateString()
    return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate() + ' ' + date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds()
}
