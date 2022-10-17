import time

from .helpers import VerboseLiveServerTestCase


class InteractionTest(VerboseLiveServerTestCase):
    def test_error_in_browser(self):
        self.driver.maximize_window()
        self.driver.get(self.live_server_url + "/")
        time.sleep(1000)
