import logging
import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.servers.basehttp import WSGIRequestHandler
from django.core.servers.basehttp import WSGIServer
from django.test.testcases import LiveServerThread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


logger = logging.getLogger(__name__)


class VerboseLiveServerTestCase(StaticLiveServerTestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        if os.getenv("CI"):
            # Github Actions
            options.binary_location = "/usr/bin/google-chrome-stable"
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            cls.wait_time = 20
        else:
            # Ubuntu Desktop, etc.
            cls.wait_time = 6
        cls.driver = webdriver.Chrome(
            service=ChromiumService(
                ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(),
            ),
            options=options,
        )
        cls.driver.implicitly_wait(cls.wait_time)
        super().setUpClass()

    def tearDown(self):
        # Source: https://stackoverflow.com/a/39606065
        if hasattr(self._outcome, "errors"):
            # Python 3.4 - 3.10  (These two methods have no side effects)
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.errors)
        else:
            # Python 3.11+
            result = self._outcome.result
        ok = all(test != self for test, text in result.errors + result.failures)
        if not ok:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            screenshotfile = f"screenshots/{self._testMethodName}.png"
            logger.info(f"Saving {screenshotfile}")
            self.driver.save_screenshot(screenshotfile)
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    class VersboseLiveServerThread(LiveServerThread):
        def _create_server(self):
            WSGIRequestHandler.handle = WSGIRequestHandler.handle_one_request
            return WSGIServer(
                (self.host, self.port),
                WSGIRequestHandler,
                allow_reuse_address=False,
            )

    server_thread_class = VersboseLiveServerThread
