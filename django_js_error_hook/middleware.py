'''
Javascript Error Hook Middleware

Inspired by Debug Toolbar middleware see:
https://github.com/django-debug-toolbar/django-debug-toolbar/blob/master/debug_toolbar/middleware.py
'''

from __future__ import absolute_import, unicode_literals

from django.utils.encoding import force_text
from django.conf import settings
from django.core.urlresolvers import reverse_lazy as reverse

import re


_HTML_TYPES = ('text/html', 'application/xhtml+xml')
_SCRIPT_TAG = '<script type="text/javascript" src="%s"></script>'


INSERT_BEFORE = getattr(
    settings,
    'JAVASCRIPT_ERROR_INSERT_BEFORE',
    '</body>'
)


class JSErrorHookMiddleware(object):
    def process_response(self, request, response):
        # Check for responses where the js-logger can't be inserted.
        content_encoding = response.get('Content-Encoding', '')
        content_type = response.get(
            'Content-Type', '').split(';')[0]
        
        if any((getattr(response, 'streaming', False),
                'gzip' in content_encoding,
                content_type not in _HTML_TYPES)):
            return response

        # Insert the js-logger in the response.
        content = force_text(
            response.content, encoding=settings.DEFAULT_CHARSET)

        pattern = re.escape(INSERT_BEFORE)
        bits = re.split(pattern, content, flags=re.IGNORECASE)

        if len(bits) > 1:
            bits[-2] += _SCRIPT_TAG % reverse('js-error-handler-js')
            response.content = INSERT_BEFORE.join(bits)
            if response.get('Content-Length', None):
                response['Content-Length'] = len(response.content)
        return response