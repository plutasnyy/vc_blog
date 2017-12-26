$(document).ready(function() {
    $('.btn_to_braian').on("click",function(){
        $('html, body').animate({
            scrollTop: $('#braian').offset().top
        }, 500, 'swing');
    });
    $(".btn_to_us").on("click",function(){
        $('html, body').animate({
            scrollTop: $('#us').offset().top
        }, 500, 'swing');
    });
});