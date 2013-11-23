{% load url from future %}
function logError(details) {
    $.ajax({
		type: "POST",
		url: "{% url 'js-error-handler' %}",
		data: {
			context: navigator.userAgent,
			details: details
		},
		headers: {
			"X-CSRFToken": $.cookie('csrftoken')
		},
	});
}

window.onerror = function(error_msg, url, line_number) {
    logError(url + ':' + line_number + ': ' + error_msg);
};
