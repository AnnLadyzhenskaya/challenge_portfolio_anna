import time
from pages.base_page import BasePage


class Dashboard (BasePage):
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"

    # title
    page_title_xpath = "//h6[text() = 'Scouts Panel']"

    # tickets
    players_count_text_xpath = "(//main/div[count(div) = 4]//div[text()])[1]"
    matches_count_text_xpath = "(//main/div[count(div) = 4]//div[text()])[2]"
    reports_count_text_xpath = "(//main/div[count(div) = 4]//div[text()])[3]"
    events_count_text_xpath = "(//main/div[count(div) = 4]//div[text()])[4]"

    players_count_number_xpath = "(//main/div[count(div) = 4]//b[text()])[1]"
    matches_count_number_xpath = "(//main/div[count(div) = 4]//b[text()])[2]"
    reports_count_number_xpath = "(//main/div[count(div) = 4]//b[text()])[3]"
    events_count_number_xpath = "(//main/div[count(div) = 4]//b[text()])[4]"

    # tabs
    scouts_panel_title_xpath = "(//main/div[count(div) = 3]//div/h2)[1]"
    scouts_panel_description_xpath = "//main/div[count(div) = 3]//div/p"
    shortcuts_title_xpath = "(//main/div[count(div) = 3]//div/h2)[2]"
    activity_title_xpath = "(//main/div[count(div) = 3]//div/h2)[3]"
    last_created_player_title_xpath = "//main/div[count(div) = 3]//h6[1]"
    last_updated_player_title_xpath = "//main/div[count(div) = 3]//h6[2]"
    last_updated_report_title_xpath = "//main/div[count(div) = 3]//h6[3]"

    # action links in tabs
    dev_team_contact_link_xpath = "//main/div[count(div) = 3]/div[1]//a"
    add_player_link_xpath = "//main/div[count(div) = 3]/div[2]//a"
    last_created_player_link_xpath = "//main/div[count(div) = 3]/div[3]//a[1]"
    last_updated_player_link_xpath = "//main/div[count(div) = 3]/div[3]//a[2]"
    last_updated_report_link_xpath = "//main/div[count(div) = 3]/div[3]//a[3]"

    def check_title(self):
        time.sleep(3)
        assert self.get_page_title(self.dashboard_url) == self.expected_title





