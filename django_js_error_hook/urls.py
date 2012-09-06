from django.conf.urls import patterns, url
from views import JSErrorHandlerView, utils_js

urlpatterns = patterns("",
    url(r"^$", JSErrorHandlerView.as_view(), name="js-error-handler"),
    url(r"^utils.js$", utils_js, name="js-error-handler-js"),
)
