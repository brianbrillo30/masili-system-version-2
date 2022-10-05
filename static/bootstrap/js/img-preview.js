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
<<<<<<< HEAD

=======
>>>>>>> 53f633fa2dd62706b7321697417a7a16f702d118

