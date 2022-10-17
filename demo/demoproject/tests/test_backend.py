from django.test import TestCase
from django.urls import reverse


class BackendTestCase(TestCase):
    """Test project views."""

    def test_error_handler_view(self):
        """A POST should log the error"""
        response = self.client.post(
            reverse("js-error-handler"),
            {
                "context": (
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
                ),
                "details": "Description of the error by the browser javascript engine.",
            },
        )
        self.assertEqual(response.status_code, 200)
