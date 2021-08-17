$(document).ready(function () {

  $('#collapsebtn').click(function()  {
   $('.linktree').toggleClass('switch');
   $('#collapsebtn').toggleClass('switch');
  });

  $('#mobilecollapsebtn').click(function()  {
   $('.linktree').toggleClass('switch');
   $('#collapsebtn').toggleClass('switch');
  });

  $('#menubtn').click(function()  {
   $('.menu').toggleClass('switch');
   $('nav').toggleClass('switch');
  });

  /*isolates title letters in separate spans*/
   $("#titlecard").html(function(index, html) {
    return html.replace(/\S/g, '<span>$&</span>');
  });
  /*gives each span an ID*/
  titleLetters = $('nav span')
  titleLetters.each(function(n) {
    $(this).attr("id", "title" +n);
  });

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



  var panorama, viewer, container;
  var panorama = ["panorama1", "panorama1", "panorama1", "panorama1", "panorama1", "panorama1", "panorama1", "panorama1", "panorama1", "panorama1", ]
  $('.pano-image').each(function(n) {

    panoLoc = "currentPano";
    panoLoc = panoLoc.concat(n);

    panorama[n] = new PANOLENS.ImagePanorama(eval(panoLoc));
    viewer = new PANOLENS.Viewer( { container: this} );
    viewer.add( panorama[n] );
    n = n+1;
    console.log(eval(panoLoc));
  });

});
