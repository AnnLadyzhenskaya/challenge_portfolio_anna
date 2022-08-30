from pages.base_page import BasePage


class Player(BasePage):
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    add_player_expected_titles = ["Add player", "Dodaj gracza"]
    edit_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/{}/edit"
    edit_player_expected_titles = ["Edit player", "Edycja gracza"]

    edit_player_header_xpath = "//form/div[contains(@class, 'MuiCardHeader-root')]"

    """Required fields"""
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    age_field_xpath = "//input[@name='age']"
    main_position_field_xpath = "//input[@name='mainPosition']"

    """Buttons"""
    button_submit_xpath = "//button[@type='submit']"
    button_clear_xpath = "//button[@type='submit']/following-sibling::button"

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_position(self, position):
        self.field_send_keys(self.main_position_field_xpath, position)

    def click_submit_button(self):
        self.click_on_the_element(self.button_submit_xpath)

    def click_clear_button(self):
        self.click_on_the_element(self.button_clear_xpath)

    """ check title of the page in both localizations"""
    """ actual title of edit page has the name of player, that's why we check substring"""
    def check_title(self, page):
        if page == 'add':
            assert self.get_page_title() in self.add_player_expected_titles
        elif page == 'edit':
            self.is_visible(self.edit_player_header_xpath)
            for title in self.edit_player_expected_titles:
                if title in self.get_page_title():
                    return True
            assert False





