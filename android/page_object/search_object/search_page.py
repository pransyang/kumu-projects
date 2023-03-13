from android.page_object.dashboard_page import DashboardPage
from android.page_object.login_page import LoginProcedure
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


class SearchObject(DashboardPage):
    def search_data(self, search_value):
        search_icon = self.wait_displayed(self.homepage_search)
        assert search_icon is True, "Search icon is not displayed"
        self.wait_click(self.homepage_search)
        self.wait_send_keys(self.search_box, search_value)
        self.wait_click(self.search_box)
        self.wait_click(self.search_button)

    def tap_search_user(self):
        self.wait_click(self.search_username)

    def back_home_page(self):
        self.wait_click(self.kumunity_back_button)
        self.wait_click(self.home_page)

    def all_tab(self):
        self.wait_click(self.search_all_tab)

    def streamer_tab(self):
        self.wait_click(self.search_streamers_tab)

    def livetream_tab(self):
        self.wait_click(self.search_livestreams_tab)

    def upcoming_tab(self):
        self.wait_click(self.search_upcoming_tab)

    def kumunity_tab(self):
        self.wait_click(self.search_kumunity_tab)

    def klip_tab(self):
        self.wait_click(self.search_klips_tab)

    def post_tab(self):
        self.wait_click(self.search_post_tab)


class Search(SearchObject, LoginProcedure):
    def dashboard(self):
        self.login_account(account="matt", account_type="prod_main")
        time.sleep(3)
        self.verify_tour_popup()

    def search_page(self):
        self.search_data("t")
        time.sleep(3)
        self.livetream_tab()
        self.upcoming_tab()
        self.kumunity_tab()
        self.klip_tab()
        self.post_tab()
        self.streamer_tab()
        self.all_tab()
