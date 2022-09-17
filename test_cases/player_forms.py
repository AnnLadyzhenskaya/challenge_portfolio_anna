import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.player import Player
from utils.credentials import TestUser
from utils.settings import IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.test_player import TestPlayer


class TestPlayerForms(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

        """Preconditions: user should be logged in"""
        login_page = LoginPage(self.driver)
        login_page.do_login(TestUser.TEST_LOGIN, TestUser.TEST_PASSWORD)
        time.sleep(3)

        self.dashboard_page = Dashboard(self.driver)
        self.player = Player(self.driver)

    def test_add_player_success(self):
        self.dashboard_page.go_to_add_player_form()

        # fill in required fields
        self.player.type_in_name(TestPlayer.name)
        self.player.type_in_surname(TestPlayer.surname)
        self.player.type_in_age(TestPlayer.age)
        self.player.type_in_position(TestPlayer.main_position)

        # submit and wait until toasts disappear
        self.player.click_submit_button()
        # time.sleep(10)

        # check if redirected to edit page
        self.player.check_title('edit')

    def test_add_player_without_required_data(self):
        self.dashboard_page.go_to_add_player_form()

        # fill in only 2 of 4 required fields
        self.player.type_in_name(TestPlayer.name)
        self.player.type_in_age(TestPlayer.age)

        self.player.click_submit_button()

        # check if stayed at add player page
        self.player.check_title('add')
        time.sleep(3)

    def test_clear_form(self):
        self.dashboard_page.go_to_add_player_form()
        fields = self.driver.find_elements(By.XPATH, "//input[@type='text']")

        # fill in all text inputs on the page
        for field in fields:
            field.send_keys("test")

        time.sleep(2)
        self.player.click_clear_button()
        time.sleep(2)

        # check if all text inputs are clear
        for field in fields:
            if field.text == "":
                continue
            else:
                assert False

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
