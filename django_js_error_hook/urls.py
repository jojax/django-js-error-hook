from django.conf.urls import patterns, url
from views import JSErrorHandlerView

urlpatterns = patterns("",
    url(r"^$", JSErrorHandlerView.as_view(), name="js-error-handler"),
)
