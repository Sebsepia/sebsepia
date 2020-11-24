$(document).ready(function () {

  /*isolates title letters in separate spans*/
  title = $("#titlecard");
  title.html(function(index, html) {
    return html.replace(/\S/g, '<span>$&</span>');
  });
  /*gives each span an ID*/
  titleLetters = $('nav span')
  titleLetters.each(function(n) {
    $(this).attr("id", "title" +n);
  });

/*  bgOverlayHeight = img In P;
*/


  var infinite = new Waypoint.Infinite({
      element: $('.contenu')[0],
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
