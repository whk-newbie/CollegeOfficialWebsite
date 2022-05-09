export default function formatted_time(row, column) {
    const date = new Date(row[column.property]);
    // return date.toLocaleDateString()
    return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate()
}


