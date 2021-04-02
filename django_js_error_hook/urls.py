from django.urls import re_path
from .views import js_error_view

urlpatterns = [
    re_path("^$", js_error_view, name="js-error-handler"),
]
