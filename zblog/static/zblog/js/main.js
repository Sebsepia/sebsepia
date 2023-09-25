$(document).ready(function () {

  $('#menutoggle').click(function()  {
   $('.menu').toggleClass('switch');
/*   $('.contenu').toggleClass('switch');*/
  });

  $('#p_overlay').click(function()  {
   $('#p_overlay').toggleClass('switch');
/*   $('.contenu').toggleClass('switch');*/
  });
/*csdc*/

  $('.sketchbook_cover').click(function(){
    $(this).find('div').toggleClass('switch');
    });
  $(".sketchbook .sketchbook_page").click(function(e) {
      e.stopPropagation();
   });
/*  isolates title letters in separate spans
   $("#titlecard").html(function(index, html) {
    return html.replace(/\S/g, '<span>$&</span>');
  });
  /*gives each span an ID
  titleLetters = $('header span')
  titleLetters.each(function(n) {
    $(this).attr("id", "title" +n);
  });
*/
  var infinite = new Waypoint.Infinite({
      element: $('.contenu'),
      handler:function(direction){

      },
      offset:'bottom-in-view',

      onBeforePageLoad: function () {
        $('.loader').show();
      },
      onAfterPageLoad: function () {
        $('.loader').hide();
      }
    });

});
