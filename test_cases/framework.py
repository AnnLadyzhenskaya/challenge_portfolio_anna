import time
import unittest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.navigation import Navigation
from utils.credentials import TestUser
from utils.settings import IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

        login_page = LoginPage(self.driver)
        login_page.do_login(TestUser.TEST_LOGIN, TestUser.TEST_PASSWORD)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")

    def test_test(self):
        nav = Navigation(self.driver)
        nav.detect_language()
        time.sleep(3)
        nav.click_language_button()
        time.sleep(3)