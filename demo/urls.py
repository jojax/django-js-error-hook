from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
    url('^$', TemplateView.as_view(template_name = "error_test.html")),
    url('^error_hook/', include('django_js_error_hook.urls')),
]
