from django.conf.urls import url
from .views import js_error_view, utils_js


urlpatterns = [
    url("^$", js_error_view, name="js-error-handler"),
    url("^utils.js$", utils_js, name="js-error-handler-js"),
]
