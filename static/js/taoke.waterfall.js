/*!
  jQuery taoke.waterfall
  @name taoke.waterfall.js
  @author gplin
  @version 1.0.0
  @date 2013-07-06
  @category jQuery plugin
*/
(function($){


	$.fn.setwaterfall = function(options){

		// var scrollTop= document.documentElement.scrollTop || document.body.scrollTop;

		var boxwith = $(this).width()+parseInt($(this).css("paddingLeft"))*2+parseInt($(this).css("marginLeft"))*2;
		alert(boxwith);
		var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
		// var self = this;
		// alert(scrollTop - self.scrollTop);
	};
})(jQuery)