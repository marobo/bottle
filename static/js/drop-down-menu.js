$(document).ready(function(){
	$("ul.navigation li span").mouseover(function() 
	{
		$(this).parent().find("ul.submenu").slideDown('fast').show(); //Showing Submenu when mouseover

		$(this).parent().hover(function() //This is to show the current submenu alive. If we remove this function the submenu will show and hide immediately.
		{
		}, 
		function()
		{	
			$(this).parent().find("ul.submenu").slideUp('slow'); //Hiding Submenu when mouseout
		});
	});
});