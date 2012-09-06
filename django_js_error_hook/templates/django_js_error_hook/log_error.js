{% load url from future %}
function logError(details) {
    $.ajax({
		type: "POST",
		url: "{% url 'js-error-handler' %}",
		data: {context: navigator.userAgent, details: details},
		contentType: 'application/json; charset=utf-8'
	}); 
}

window.onerror = function(error_msg, url, line_number) {
    logError(url + ':' + line_number + '\n\n' + error_msg);
};
