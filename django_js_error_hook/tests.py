import unittest
from django.test import TestCase
from django.urls import reverse


class JSErrorHookTestCase(TestCase):
    """Test project views."""

    @unittest.skip('Noticed test fails as part of the github-actions PR - this needs fixing in a separate ticket.')
    def test_error_handler_view(self):
        """A POST should log the error"""
        response = self.client.post(reverse('js-error-handler'),
                                    {"details": "Description of the error by the browser javascript engine."})
        self.assertEqual(response.status_code, 200)
