function previewBeforeUpload(id){
    document.querySelector("#"+id).addEventListener("change",function(e){
        
        if(e.target.files.length == 0){
            return;
        }

        let file = e.target.files[0];
        let url = URL.createObjectURL(file);
        
        document.querySelector("#"+id+"-preview img").src = url;
    });
}

previewBeforeUpload("file");
previewBeforeUpload("file-2");

