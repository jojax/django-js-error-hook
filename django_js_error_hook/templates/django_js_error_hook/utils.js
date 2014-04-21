{% load url from future %}
(function(){

	function getCookie(name){
	    var nameEQ = name + "=";
	    var c, ca = document.cookie.split(';');
	    
	    for(var i = 0; i < ca.length; i++){
		c = ca[i];
		while(c.charAt(0) == ' ') 
		    c = c.substring(1, c.length);
		if(c.indexOf(nameEQ) == 0) 
		    return c.substring(
			nameEQ.length, c.length);
	    }
	    return null;
	}

	function logError(details){
	    var cookie = getCookie('csrftoken'),
    	        query = [],
	        data = {
		    context: navigator.userAgent,
		    details: details
		},
                xhr;

	    try{
		xhr = new ActiveXObject('Msxml2.XMLHTTP');
	    }
	    catch(e1){
		try{
		    xhr = new ActiveXObject('Microsoft.XMLHTTP');
		}catch(e2){
		    xhr = new XMLHttpRequest();
		}
	    }

	    xhr.open(
		"POST", 
		"{% url 'js-error-handler' %}", 
		false
	    );

	    xhr.setRequestHeader(
		'Content-type', 
		'application/x-www-form-urlencoded'
	    );

	    if(cookie){
		xhr.setRequestHeader("X-CSRFToken", cookie);
	    }

	    for(var key in data){
		query.push(
		    encodeURIComponent(key) + 
			'=' + 
			encodeURIComponent(data[key])
		);
	    }
	    xhr.send(query.join('&'));
	}

	window.onerror = function(error_msg, url, line_number){
	    logError(url + ':' + line_number + ': ' + error_msg);
	};

    {% if proxy_console %}
    
        var proxied_log = window.console.log;

        window.console.log = function(){
	    logError(Array.prototype.slice.call(
		arguments).join(','));
	    return proxied_log.apply(this, arguments);
        };

    {% endif %}
    
})();
