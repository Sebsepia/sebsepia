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

  /*Creates simpler preview of posts in  Portfolio */
  $('div.portintime').each(function (){
    $('img').not('img:first-of-type').hide();
  });



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
  /* stops Posts from making images stretch by having too much text  */
/*      var alignTextToImg = function(){
      var setter;
      $("div.intime").each(function(obj){
        var target = $(this).find("p");
        var setter = target.find("img");
        target.css("max-width", setter.width()+"px");
        console.log(setter.width(), target.text());
        });
      };*/
