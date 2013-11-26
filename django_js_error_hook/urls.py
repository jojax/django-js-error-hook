from django.conf import settings
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from views import JSErrorHandlerView, utils_js

CSRF_EXEMPT = getattr(settings, 'JAVASCRIPT_ERROR_CSRF_EXEMPT', False)

if CSRF_EXEMPT:
    js_error_view = csrf_exempt(JSErrorHandlerView.as_view())
else:
    js_error_view = JSErrorHandlerView.as_view()

urlpatterns = patterns("",
    url(r"^$", js_error_view, name="js-error-handler"),
    url(r"^utils.js$", utils_js, name="js-error-handler-js"),
)
