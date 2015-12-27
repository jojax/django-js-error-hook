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

	window.onerror = function(error_msg, url, line_number) {
		logError(url + ':' + line_number + ': ' + error_msg);
	};
})();
