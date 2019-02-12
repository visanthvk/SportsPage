$(function() {
  $('#colorselector').change(function(){
    $('.colors').hide();
    $('#' + $(this).val()).show();
  });
});

$(function() {
  $('#colorselector1').change(function(){
    $('.colors').hide();
    $('#' + $(this).val()).show();
  });
});