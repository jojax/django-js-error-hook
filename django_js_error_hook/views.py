from django.conf import settings
from django.views.generic import TemplateView, View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page

import logging 

logger = logging.getLogger(getattr(settings, 'JAVASCRIPT_ERROR_ID', 'javascript_error'))

class JSErrorHandlerView(View):
   """View that take the JS error as POST parameters and log it"""

   @method_decorator(csrf_exempt)
   def dispatch(self, *args, **kwargs):
      return super(JSErrorHandlerView, self).dispatch(*args, **kwargs)
   
   def post(self, request, *args, **kwargs):  
      """Read POST data and log it as an JS error"""
      error_dict = request.POST.dict()
      logger.error("javascript error: %s", error_dict)
      return HttpResponse('Error logged')
  
class MimetypeTemplateView(TemplateView):
   """TemplateView with mimetype override"""
   template_name="django_js_error_hook/log_error.js"
   mimetype="text/javascript"

   def render_to_response(self, context, **response_kwargs):
      """Use self.mimetype to return the right mimetype"""
      response_kwargs['mimetype'] = self.mimetype
      return super(MimetypeTemplateView, self).render_to_response(context, **response_kwargs)

utils_js = cache_page(2 * 31 * 24 * 60 * 60)(MimetypeTemplateView.as_view()) #: Cache 2 months
