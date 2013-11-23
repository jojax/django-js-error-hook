{% load url from future %}
(function() {
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}
	function logError(details) {
		var xhr;
		try {
			xhr = new ActiveXObject('Msxml2.XMLHTTP');
		} catch (e1) {
			try {
				xhr = new ActiveXObject('Microsoft.XMLHTTP');
			} catch (e2) {
				xhr = new XMLHttpRequest();
			}
		}
		xhr.open("POST", "{% url 'js-error-handler' %}", false);
		xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
		xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		var query = [], data = {
			context: navigator.userAgent,
			details: details
		};
		for (var key in data) {
			query.push(encodeURIComponent(key) + '=' + encodeURIComponent(data[key]));
		}
		xhr.send(query.join('&'));
	}

	window.onerror = function(error_msg, url, line_number) {
		logError(url + ':' + line_number + ': ' + error_msg);
	};
})();
