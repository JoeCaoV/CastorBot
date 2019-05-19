$(document).ready(function() {
	$('form').on('submit', function(event) {
		event.preventDefault();
		$.ajax({
			data : {
				question: $('#question').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {
			if(data.error){
				$('#error').show().text(data.error);
				$('#map, #intro').hide();
			}else{
				$('#error').hide()
			    $('#google_map').attr('src', data.map);
			    $('#address').text(data.address);
			    $('#text').text(data.story);
			    $('#link').attr('href', data.url);
			    $('#story, #map, #intro').show();
			    if(data.url){
			    	$('#text').text(data.story);
			        $('#link').attr('href', data.url).text('[En savoir plus sur Wikipédia]');
			    }else{
			    	$('#text').text('Enfaite je ne sais plus ce que je voulais dire... Je suis si vieux...')
			    	$('#link').text('')
			    }
		    }
		});
	});
});