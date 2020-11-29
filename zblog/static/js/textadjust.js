  /* stops Posts from making images stretch by having too much text  */

  var alignTextToImg = function(){
      var setter;
      $("div.intime").each(function(obj){
        var setter = $(this).find("img");
        var target = $(this).find("p");
        target.css("max-width", setter.width()+"px");
        console.log(setter.width(), target.text());
      });
  };
  alignTextToImg();
