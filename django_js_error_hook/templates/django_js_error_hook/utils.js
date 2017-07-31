(function() {
	function getCookie(name) {
		var nameEQ = name + "=";
		var ca = document.cookie.split(';');
		for(var i=0;i < ca.length;i++) {
			var c = ca[i];
			while (c.charAt(0)==' ') c = c.substring(1,c.length);
			if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
		}
		return null;
	}
	function logError(details) {
		var xhr = new XMLHttpRequest();

		xhr.open("POST", "{% url 'js-error-handler' %}", true);
		xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
		var cookie = getCookie('csrftoken');
		if (cookie) {
			xhr.setRequestHeader("X-CSRFToken", cookie);
		}
		var query = [], data = {
			context: navigator.userAgent,
			details: details
		};
		for (var key in data) {
			query.push(encodeURIComponent(key) + '=' + encodeURIComponent(data[key]));
		}
		xhr.send(query.join('&'));
	}

	window.onerror = function(msg, url, line_number, column_number, error_obj) {
		var log_message = url + ': ' + line_number + ': ' + msg;
		if (column_number) {
			log_message += ", " + column_number;
		}
		if (error_obj && error_obj.stack) {
			log_message += ", " + error_obj.stack;
		}
		logError(log_message);
	};
})();
