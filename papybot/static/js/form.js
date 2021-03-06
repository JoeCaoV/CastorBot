$(document).ready(function() {
	$('form').on('submit', function(event) {
		event.preventDefault();
		$('.spinner-border').css('display', 'inline-block')
		$.ajax({
			data : {
				question: $('#question').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {
			$('.spinner-border').hide()
			if(data.error){
				$('#error').show().text(data.error);
				$('#map, #intro, #story').hide();
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
		    $('#list').show()
		    $('#previous').prepend('<li>' + $('#question').val() + '</li>')
		});
	});
});