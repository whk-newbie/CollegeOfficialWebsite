function getName(file){
    if (file){
        return file.split('/')[file.split('/').length - 1]
    }
}

function tofile(url){
    window.location.href = url;
}

export{
    getName,
    tofile
}

