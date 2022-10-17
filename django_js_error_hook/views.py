from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
import logging

ERROR_ID = getattr(settings, "JAVASCRIPT_ERROR_ID", "javascript_error")
CSRF_EXEMPT = getattr(settings, "JAVASCRIPT_ERROR_CSRF_EXEMPT", False)
BLACKLIST_USERAGENT = getattr(
    settings, "JAVASCRIPT_ERROR_USERAGENT_BLACKLIST", ["googlebot", "bingbot"]
)
BLACKLIST_ERRORS = getattr(settings, "JAVASCRIPT_ERROR_BLACKLIST", [])

logger = logging.getLogger(ERROR_ID)


class JSErrorHandlerView(View):
    """View that take the JS error as POST parameters and log it"""

    def post(self, request):
        """Read POST data and log it as an JS error"""
        error_dict = request.POST.dict()
        if hasattr(request, "user"):
            error_dict["user"] = (
                request.user if request.user.is_authenticated else "<UNAUTHENTICATED>"
            )
        else:
            error_dict["user"] = "<UNAUTHENTICATED>"

        level = logging.ERROR
        if any(
            useragent in error_dict["context"].lower()
            for useragent in BLACKLIST_USERAGENT
        ) or any(error in error_dict["details"].lower() for error in BLACKLIST_ERRORS):
            level = logging.WARNING

        logger.log(
            level,
            "Got error: \n%s",
            "\n".join("\t%s: %s" % (key, value) for key, value in error_dict.items()),
            extra={"status_code": 500, "request": request},
        )
        return HttpResponse("Error logged")


if CSRF_EXEMPT:
    js_error_view = csrf_exempt(JSErrorHandlerView.as_view())
else:
    js_error_view = JSErrorHandlerView.as_view()
