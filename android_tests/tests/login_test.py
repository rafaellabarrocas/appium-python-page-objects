from android_tests.pages.login_page import LoginPage
from android_tests.tests.base_test import BaseTest


class LoginTest(BaseTest):
    """Container for all login page tests."""
    EMAIL = 'quality'
    VALID_PASSWORD = "2918"
    INVALID_PASSWORD = 'passwrod'

    def setUp(self):
        """Set up Appium connection and navigate to login page."""
        BaseTest.setUp(self)
        self.login = LoginPage(self.driver)

    def test_valid_login(self):
        """Login with valid credentials, verify valid login message, log out, verify back at log in."""
        self.login.enter_email(email=self.EMAIL)
        self.login.click_on_continue()
        self.login.enter_password(password=self.VALID_PASSWORD)

    def tearDown(self):
        BaseTest.tearDown(self)
