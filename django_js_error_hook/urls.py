from django.conf.urls import patterns, url
from views import js_error_view, utils_js


urlpatterns = patterns("",
    url(r"^$", js_error_view, name="js-error-handler"),
    url(r"^utils.js$", utils_js, name="js-error-handler-js"),
)
