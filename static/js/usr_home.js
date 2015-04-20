$(document).ready(function(){
    $('#buy').mouseenter(function(){
        $('#buy').fadeTo('fast', 1);
    });
    $('#buy').mouseleave(function(){
        $('#buy').fadeTo('fast', 0.5);
    });
});
