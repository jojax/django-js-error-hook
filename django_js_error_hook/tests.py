from django.test import TestCase
from django.core.urlresolvers import reverse

class JSErrorHookTestCase(TestCase):
    """Test project views."""
    
    def test_error_handler_view(self):
        """A POST should log the error"""
        response = self.client.post(reverse('js-error-handler'), {"details": "Description of the error by the browser javascript engine."})
        self.assertEqual(response.status_code, 200)

    def test_error_js_utils_view(self):
        response = self.client.get(reverse('js-error-handler-js'))
        self.assertEqual(response.status_code, 200)
        
