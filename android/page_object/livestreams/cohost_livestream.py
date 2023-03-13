import time
from android.helpers.element_actions import Actions
from android.helpers.locators import KumuLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from android.page_object.livestreams.livestream_page import CreateLivestream
from android.page_object.login_page import LoginProcedure
from android.page_object.search_object.search_page import SearchObject
from android.page_object.dashboard_page import DashboardPage


class CohostLivestream(LoginProcedure, SearchObject, DashboardPage):

    def select_livestream_account(self, search_account):
        self.search_data(search_value=search_account)
        self.tap_search_user()
        time.sleep(10)
        self.wait_click(self.profile_photo)
        # assert self.wait_displayed(self.cohost_layout_container) is True, "Cohost container is not visible"
        print("User joined a livestream!!")

    def click_cohost_btn(self):
        self.wait_click(self.request_cohost)
        self.wait_click(self.request_cohost)
        try:
            for i in range(2):
                self.wait_click(self.allow_while_using_app)
        except (NoSuchElementException, TimeoutException) as e:
            print(e)
            pass

        print("User cohosted on Livestream!!")

    def verify_cohost(self):
        assert self.wait_displayed(self.media_container) is True, "Media container is not visible"
        assert self.wait_displayed(self.diamond_container) is True, "Diamond Container is not visible"
        print("Cohost verification Success !!")

    def end_cohost(self):
        self.wait_click(self.leave_cohost)
