from django.conf.urls import url
from .views import js_error_view

urlpatterns = [
    url("^$", js_error_view, name="js-error-handler"),
]
