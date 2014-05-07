{% load url from future %}
var djErrorHook = (function(djErrorHook, undefined){
    
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

    djErrorHook.logError = function(details){
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
    };

    window.onerror = function(error_msg, url, line_number){
	djErrorHook.logError(
	    url + ':' + line_number + ': ' + error_msg);
    };

    {% if proxy_console %}
    
    var proxied_log = window.console && window.console.log;

    window.console.log = function(){
	djErrorHook.logError(
	    'CONSOLE: ' + Array.prototype.slice.call(
		arguments).join(','));
	if(proxied_log && proxied_log.apply){
	    proxied_log.apply(this, arguments);
	}
    };

    {% endif %}

    return djErrorHook;
    
})(
    djErrorHook || {}
);
