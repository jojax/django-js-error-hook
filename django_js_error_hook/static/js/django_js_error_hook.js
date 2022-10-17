(function () {
  function getCookie (name) {
    if (!document.cookie || document.cookie === '') {
      return null
    }
    const cookie = document.cookie.split(';').map(cookie => cookie.trim()).find(cookie => {
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        return true
      } else {
        return false
      }
    })
    if (cookie) {
      return decodeURIComponent(cookie.substring(name.length + 1))
    }
    return null
  }
  function logError (details) {
    const cookie = getCookie('csrftoken')
    const data = {
      context: String(navigator.userAgent),
      details: String(details)
    }

    if (window.fetch) {
      const body = new FormData()
      body.append('context', data.context)
      body.append('details', data.details)

      return fetch(window.djangoJSErrorHandlerUrl, {
        method: 'POST',
        headers: {
          'X-CSRFToken': cookie
        },
        credentials: 'include',
        body
      })
    } else {
      const xhr = new XMLHttpRequest()

      xhr.open('POST', window.djangoJSErrorHandlerUrl, true)
      xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded')

      if (cookie) {
        xhr.setRequestHeader('X-CSRFToken', cookie)
      }
      const query = []
      for (const key in data) {
        query.push(encodeURIComponent(key) + '=' + encodeURIComponent(data[key]))
      }
      xhr.send(query.join('&'))
    }
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
