from pages.base_page import BasePage


class LoginPage(BasePage):
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/login'
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    expected_title = ['Scouts panel - sign in', 'Scouts panel - zaloguj']
    title_of_box_xpath = '//form//h5'
    header_of_box = 'Scouts Panel'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def do_login(self, email, password):
        self.type_in_email(email)
        self.type_in_password(password)
        self.click_sign_in_button()

    def check_title(self):
        assert self.get_page_title() in self.expected_title

