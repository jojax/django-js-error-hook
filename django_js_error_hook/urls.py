from django.conf.urls import patterns, url
from views import JSErrorHandlerView, MimetypeTemplateView

urlpatterns = patterns("",
    url(r"^$", JSErrorHandlerView.as_view(), name="js-error-handler"),
    url(r"^utils.js$", MimetypeTemplateView.as_view(), name="js-error-handler-js"),
)
