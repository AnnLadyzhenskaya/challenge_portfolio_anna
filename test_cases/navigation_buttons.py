import time
import unittest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.navigation import Navigation
from utils.credentials import TestUser
from utils.settings import IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestNavigationButtons(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

        """Preconditions: user should be logged in"""
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestUser.TEST_LOGIN, TestUser.TEST_PASSWORD)
        time.sleep(3)

        self.navigation_page = Navigation(self.driver)

    def test_change_language(self):
        default_language = self.navigation_page.detect_language()
        self.navigation_page.click_language_button()
        time.sleep(1)
        self.assertNotEqual(default_language, self.navigation_page.detect_language())

    def test_sign_out(self):
        self.navigation_page.click_sign_out()
        time.sleep(1)
        self.login_page.check_title()


    @classmethod
    def tearDownClass(self):
        self.driver.quit()