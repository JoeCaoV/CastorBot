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
				$('#story').show().text(data.error);
				$('#map, #intro').hide();
			}else{
			    $('#text').text(data.story);
			    $('#google_map').attr('src', data.map);
			    $('#address').text(data.address);
			    $('#link').attr('href', data.url);
			    $('#story, #map, #intro').show();
		    }
		});
	});
});