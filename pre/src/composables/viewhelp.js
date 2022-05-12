function getName(file){
    if (file){
        const news = decodeURIComponent(file)
        return news.split('/')[file.split('/').length - 1]
    }
}

function tofile(url){
    window.location.href = url;
}

export{
    getName,
    tofile
}

