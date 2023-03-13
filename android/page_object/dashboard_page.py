import time

from android.page_object.login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from android.helpers.locators import KumuLocators


class DashboardPage(KumuLocators):
    def claim_daily_rewards(self):
        try:
            if self.wait_displayed(self.daily_rewards) is True:
                self.wait_short_click(self.claim_reward)
                assert self.wait_displayed(self.rewards_claimed_text) is True, "Error on claiming daily Rewards"
                self.wait_short_click(self.confirm_reward_claimed)
                print("Claimed daily rewards!")
            else:
                print("Daily Rewards did not appear")
                pass
        except (NoSuchElementException, TimeoutException):
            pass

    def verify_tour_popup(self):
        try:
            dismiss = self.wait_displayed(self.tour_dismiss)
            if dismiss is True:
                self.wait_short_click(self.tour_dismiss)
                print("Pop up tour dismissed")
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print("Pop Up tour did not Appear")
            pass

    def accept_terms(self):
        try:
            self.clickElement(self.intro_accept)
        except (NoSuchElementException, TimeoutException):
            # print(e)
            pass

        print("Accept terms did not Appear")

    def verify_live_tab(self):
        live_tab = self.wait_short_displayed(self.live_tab)
        assert live_tab is True, "Live Tab is missing"
        print("Live tab is displayed")

    def tap_karlito_logo(self):
        karlito = self.driver.find_elements("id", self.bottom_tabs)
        self.clickElement(karlito[4])

    def select_post_or_live(self, option):
        if option == "livestream":
            self.clickElement(self.create_livestream)
            print("selected livestream option")
        else:
            self.clickElement(self.timeline_post)

    def close_dashboard_adds(self):
        try:
            self.wait_short_click(self.close_adds_pop_up)
        except (NoSuchElementException, TimeoutException):
            pass
        print("Ads did not Appear")

    def dashboard(self):
        time.sleep(3)
        self.claim_daily_rewards()
        self.close_dashboard_adds()
        self.accept_terms()
        time.sleep(3)
        self.verify_tour_popup()
        self.verify_live_tab()

    def back_to_homepage(self):
        for i in range(3):
            self.wait_click(self.close_livestream_btn)
            time.sleep(3)
