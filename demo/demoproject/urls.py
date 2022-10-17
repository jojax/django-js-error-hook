from django.urls import include
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="error_test.html")),
    path("error_hook/", include("django_js_error_hook.urls")),
]
