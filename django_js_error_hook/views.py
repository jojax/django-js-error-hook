from django.conf import settings
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

import logging
logger = logging.getLogger(getattr(settings, 'JAVASCRIPT_ERROR_ID', 'javascript_error'))


class JSErrorHandlerView(View):
    """View that take the JS error as POST parameters and log it"""

    def post(self, request):
        """Read POST data and log it as an JS error"""
        error_dict = request.POST.dict()
        error_dict['user'] = request.user if request.user.is_authenticated() else "<UNAUTHENTICATED>"
        logger.error("Got error: \n%s", '\n'.join("\t%s: %s" % i for i in error_dict.items()))
        return HttpResponse('Error logged')

class MimetypeTemplateView(TemplateView):
    """TemplateView with mimetype override"""
    template_name = "django_js_error_hook/utils.js"
    mimetype = "text/javascript"

    def render_to_response(self, context, **response_kwargs):
        """Use self.mimetype to return the right mimetype"""
        response_kwargs['mimetype'] = self.mimetype
        return super(MimetypeTemplateView, self).render_to_response(context, **response_kwargs)

utils_js = cache_page(2 * 31 * 24 * 60 * 60)(MimetypeTemplateView.as_view()) #: Cache 2 months
