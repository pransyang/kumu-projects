import time
from threading import Thread
from android.page_object.search_object.search_page import SearchObject
from android.page_object.other_profile_object.other_profile_page import OtherProfilePage


class TestOtherProfile(OtherProfilePage, SearchObject):
    def test_view_like_comment(self):
        self.login_account("matt", "prod_main")
        time.sleep(6)
        self.close_dashboard_adds()
        time.sleep(3)
        self.verify_tour_popup()
        self.verify_live_tab()
        time.sleep(3)
        self.search_data("test_matthewqa")
        self.tap_search_user()
        time.sleep(4)
        self.view_post()
        time.sleep(3)
        self.like_post()
        time.sleep(3)
        self.comment("This is testing")
        time.sleep(3)
        self.back_feed_page()
        time.sleep(3)
        self.back_home_page()
        time.sleep(3)
        self.driver.quit()
