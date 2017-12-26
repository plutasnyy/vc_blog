var targetWidth = 980;
var deviceWidth = 'device-width';
var viewport = $('meta[name="viewport"]');

// check to see if local storage value is set on page load
localStorage.isResponsive = (localStorage.isResponsive == undefined) ? 'true' : localStorage.isResponsive;

var showFullSite = function(){
    viewport.attr('content', 'width=' + targetWidth);

    if(!$('#view-options #view-responsive').length){
        $('#view-options').append('View Mobile Optimized');
    }

    localStorage.isResponsive = 'false';
}



$(document).ready(function() {
  showFullSite();
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
