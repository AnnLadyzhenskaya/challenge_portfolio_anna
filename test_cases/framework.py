import unittest
from selenium import webdriver
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

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")


class TestMediumPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://medium.com/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_check_title(self):
        actual_title = self.get_page_title('https://medium.com/')
        expected_title = 'Medium – Where good ideas find you.'
        assert actual_title == expected_title

    def get_page_title(self, url):
        return self.driver.title

    @classmethod
    def tearDown(self):
        self.driver.quit()