(function () {
  function getCookie (name) {
    const nameEQ = name + '='
    const ca = document.cookie.split(';')
    for (let i = 0; i < ca.length; i++) {
      let c = ca[i]
      while (c.charAt(0) === ' ') c = c.substring(1, c.length)
      if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length)
    }
    return null
  }

  function logError (details) {
    const xhr = new XMLHttpRequest()

    xhr.open('POST', window.djangoJSErrorHandlerUrl, true)
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded')
    const cookie = getCookie('csrftoken')
    if (cookie) {
      xhr.setRequestHeader('X-CSRFToken', cookie)
    }
    const query = []; const data = {
      context: navigator.userAgent,
      details
    }
    for (const key in data) {
      query.push(encodeURIComponent(key) + '=' + encodeURIComponent(data[key]))
    }
    xhr.send(query.join('&'))
  }

  window.onerror = function (msg, url, lineNumber, columnNumber, errorObj) {
    let logMessage = url + ': ' + lineNumber + ': ' + msg
    if (columnNumber) {
      logMessage += ', ' + columnNumber
    }
    if (errorObj && errorObj.stack) {
      logMessage += ', ' + errorObj.stack
    }
    logError(logMessage)
  }

  if (window.addEventListener) {
    window.addEventListener('unhandledrejection', function (rejection) {
      let logMessage = rejection.type
      if (rejection.reason) {
        if (rejection.reason.message) {
          logMessage += ', ' + rejection.reason.message
        } else {
          logMessage += ', ' + JSON.stringify(rejection.reason)
        }
        if (rejection.reason.stack) {
          logMessage += ', ' + rejection.reason.stack
        }
      }
      logError(logMessage)
    })
  }
})()
