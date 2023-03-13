import time

from android.page_object.livestreams.kumunity_page import KumunityPage


class TestKumunityLivestream(KumunityPage):
    def test_solo_livestream(self):
        self.login_account("matt", "prod_main")
        time.sleep(4)
        self.close_dashboard_adds()
        time.sleep(3)
        self.verify_tour_popup()
        time.sleep(3)
        self.verify_live_tab()
        time.sleep(3)
        self.tap_kumunity_page()
        time.sleep(3)
        self.kumunity_livestream()
        time.sleep(3)
        self.verify_solo_livestream_started()
        time.sleep(3)
        self.close_livestream()
        self.exit_kumunity_page()
        time.sleep(3)
        self.driver.quit()
