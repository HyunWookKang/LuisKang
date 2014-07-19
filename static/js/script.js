$(document).ready(function() {
	$('.Profile').hide();
	$('#Hobbycontents').hide();
	$('#Bookcontents').hide();
	$('#Idealink').hide();
	$('#Profilebutton').click(function() {
		$('#grid').fadeOut('fast');
		$('.Profile').slideToggle('fast');
	}); 
	$('#Footballbutton').click(function(){
		$('#grid').fadeOut('fast');
		$('#Hobbycontents').slideToggle('fast');
	});
	$('#Bookbutton').click(function(){
		$('#grid').fadeOut('fast');
		$('#Bookcontents').slideToggle('fast');
	});
	$('#Ideabutton').click(function(){
		$('#grid').fadeOut('fast');
		$('#Idealink').slideToggle('fast');
	});
});