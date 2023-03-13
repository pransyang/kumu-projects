import time
from android.page_object.login_page import LoginProcedure
from android.page_object.dashboard_page import DashboardPage
from android.helpers.element_actions import Actions
from android.helpers.locators import KumuLocators



class SideMenu(DashboardPage):
    def tap_side_menu(self):
        side_menu_bar = self.wait_displayed(self.side_menu)
        assert side_menu_bar is True, "Side menu bar is not displayed"
        self.wait_click(self.side_menu)

    def tap_campaign(self):
        self.is_visible(self.clickElement(self.campaign_page))
        title = self.wait_displayed(self.title_campaign)
        assert title is True, "Campaign title is not displayed"
        time.sleep(3)
        campaign_image = self.wait_displayed(self.campaign_image)
        assert campaign_image is True, "Campaign Image is not displayed"
        self.wait_click(self.campaign_image)

    def tap_campaign_leaderboard(self):
        leaderboard = self.wait_displayed(self.leaderboard_campaigns)
        assert leaderboard is True, "Leaderboard is not displayed"
        self.wait_click(self.leaderboard_campaigns)

    def back_to_homepage(self):
        for x in range(2):
            self.wait_click(self.back_button)
        self.wait_click(self.close_livestream_btn)


class SideMenuPage(LoginProcedure, SideMenu):
    def dashboard(self):
        self.login_account(account="matt", account_type="prod_main")
        time.sleep(6)
        self.close_dashboard_adds()
        time.sleep(3)
        self.verify_tour_popup()
        time.sleep(3)

    def campaign(self):
        self.tap_side_menu()
        time.sleep(3)
        self.tap_campaign()
        time.sleep(3)
        self.tap_campaign_leaderboard()
        time.sleep(3)
        self.back_to_homepage()
        self.driver.quit()





