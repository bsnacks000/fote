// main.js placeholder
$(document).ready(function(){

    $('#id_upload_image').on('change', (e)=>{
        let fname = e.target.files[0].name
        $('#filename').text(fname);
    });
});
