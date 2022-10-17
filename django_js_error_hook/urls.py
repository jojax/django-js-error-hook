from django.urls import re_path
from .views import js_error_view, utils_js


urlpatterns = [
    re_path("^$", js_error_view, name="js-error-handler"),
]