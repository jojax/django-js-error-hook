from django.conf import settings
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse

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
  
