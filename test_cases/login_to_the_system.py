import time
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.credentials import test_user


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

        self.login_page = LoginPage(self.driver)

    """ test if title of the page is as expected """
    def test_login_page_title(self):
        self.login_page.check_title()

    """ test login functionality of the page"""
    def test_log_in_to_the_system(self):
        self.login_page.do_login(test_user['login'], test_user['password'])
        time.sleep(5)
        dashboard = Dashboard(self.driver)
        dashboard.check_title()

    def test_check_header(self):
        self.login_page.assert_element_text(self.driver,
                                            self.login_page.title_of_box_xpath,
                                            self.login_page.header_of_box)

    @classmethod
    def tearDown(self):
        self.driver.quit()
