from distutils.version import StrictVersion

from django import get_version
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
import logging

ERROR_ID = getattr(settings, 'JAVASCRIPT_ERROR_ID', 'javascript_error')
CSRF_EXEMPT = getattr(settings, 'JAVASCRIPT_ERROR_CSRF_EXEMPT', False)

logger = logging.getLogger(ERROR_ID)

class JSErrorHandlerView(View):
    """View that take the JS error as POST parameters and log it"""

    def post(self, request):
        """Read POST data and log it as an JS error"""
        error_dict = request.POST.dict()
        error_dict['user'] = request.user if request.user.is_authenticated() else "<UNAUTHENTICATED>"
        logger.error("Got error: \n%s", '\n'.join("\t%s: %s" % (key, value) for key, value in error_dict.items()), extra={
                        'status_code': 500,
                        'request': request
                    })
        return HttpResponse('Error logged')

class MimetypeTemplateView(TemplateView):
    """TemplateView with mimetype override"""
    template_name = "django_js_error_hook/utils.js"
    mimetype = "text/javascript"

    def render_to_response(self, context, **response_kwargs):
        """
            Before django 1.5 : 'mimetype'
            From django 1.5 : 'content_type'

            Add the parameter to return the right mimetype
        """
        if StrictVersion(get_version()) < StrictVersion('1.5'):
            mimetype_parameter = 'mimetype'
        else:
            mimetype_parameter = 'content_type'

        response_kwargs[mimetype_parameter] = self.mimetype
        return super(MimetypeTemplateView, self).render_to_response(context, **response_kwargs)

utils_js = cache_page(2 * 31 * 24 * 60 * 60)(MimetypeTemplateView.as_view()) #: Cache 2 months

if CSRF_EXEMPT:
    js_error_view = csrf_exempt(JSErrorHandlerView.as_view())
else:
    js_error_view = JSErrorHandlerView.as_view()
