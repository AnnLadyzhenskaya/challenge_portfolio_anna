from pages.base_page import BasePage


class Navigation(BasePage):
    main_page_button_xpath = "//ul[1]/div[@role='button'][1]"
    players_button_xpath = "//ul[1]/div[@role='button'][2]"
    language_button_xpath = "//ul[2]/div[@role='button'][1]"
    sign_out_button_xpath = "//ul[2]/div[@role='button'][2]"

    def click_main_page_button(self):
        self.click_on_the_element(self.main_page_button_xpath)

    def click_players_button(self):
        self.click_on_the_element(self.players_button_xpath)

    def click_language_button(self):
        self.click_on_the_element(self.language_button_xpath)

    def click_sign_out(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def detect_language(self):
        text = self.is_visible(self.main_page_button_xpath).text
        if text == 'Strona główna':
            return 'pl'
        else:
            return 'en'




