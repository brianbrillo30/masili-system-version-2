$(function(){
    $('.date', ).datepicker({
        format: 'yyyy-mm-dd'
    });
});



$("#year").datepicker({
    format: "yyyy",
    viewMode: "years", 
    minViewMode: "years",
    autoclose:true //to close picker once year is selected
});