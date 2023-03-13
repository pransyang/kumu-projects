import time
from android.page_object.login_page import LoginProcedure
from android.page_object.livestreams.livestream_page import CreateLivestream
from selenium.common.exceptions import NoSuchElementException


class KumunityPage(LoginProcedure, CreateLivestream):
    def tap_kumunity_page(self):
        self.wait.until(self.visible(self.kumunity_page)).click()
        self.wait.until(self.visible(self.kumunity_team)).click()

    def kumunity_livestream(self):
        start_kumunity_ls = self.wait.until(self.clickable(self.kumunity_livestream_go_live))
        assert start_kumunity_ls.is_enabled() is True, "Go live button is not enabled"
        start_kumunity_ls.click()
        self.wait.until(self.clickable(self.kumunity_start_livestream)).click()

    def exit_kumunity_page(self):
        # self.close_livestream()
        for Kumu_back_btn in range(2):
            self.wait.until(self.clickable(self.kumunity_back_button)).click()
        self.wait.until(self.clickable(self.home_page)).click()
