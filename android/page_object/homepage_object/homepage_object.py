import time
from android.page_object.login_page import LoginProcedure
from android.page_object.dashboard_page import DashboardPage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium import webdriver
from android.helpers.utilities import KumuBaseClass
from selenium.webdriver.support import expected_conditions as EC

class home(DashboardPage):
    def view_notification(self):
        notification_button = self.wait_displayed(self.notification_page)
        assert notification_button is True, "Notification button is not tappable"
        self.wait_click(self.notification_page)

        textname = self.wait_get_text(self.notification_title)
        assert textname == "Notifications", "Textname is not Notifications"



    def for_you(self):
        for_you_button = self.wait_displayed(self.for_you_subheader)
        assert for_you_button is True, "For you subheader button is not tappable"
        self.wait_click(self.for_you_subheader)

    def all(self):
        all_button = self.wait_displayed(self.all_subheader)
        assert all_button is True, "All subheader button is not tappable"
        self.wait_click(self.all_subheader)

    def newbies(self):
        newbies_button = self.wait_displayed(self.newbies_subheader)
        assert newbies_button is True, "Newbies subheader button is not tappable"
        self.wait_click(self.newbies_subheader)


    def solo(self):
        solo_button = self.wait_displayed(self.solo_subheader)
        assert solo_button is True, "Solo subheader button is not tappable"
        self.wait_click(self.solo_subheader)

    def coHost(self):
        co_host_button = self.wait_displayed(self.co_host_subheader)
        assert co_host_button is True, "Co-host subheader button is not tappable"
        self.wait_click(self.co_host_subheader)

    def audio(self):
        audio_button = self.wait_displayed(self.audio_subheader)
        assert audio_button is True, "Audio subheader button is not tappable"
        self.wait_click(self.audio_subheader)

    def team(self):
        team_button = self.wait_displayed(self.team_subheader)
        assert team_button is True, "Team subheader button is not tappable"
        self.wait_click(self.team_subheader)
    def live_page(self):
        live_page = self.wait_displayed(self.pager_live)
        assert live_page is True, "Live Page is not displayed"

class homepage(LoginProcedure, home):
    def dashboard(self):
        self.login_account(account="matt", account_type="prod_main")
        self.close_dashboard_adds()
        self.verify_tour_popup()


    def sub_newbies(self):
        self.newbies()
        self.live_page()

    def sub_solo(self):
        self.solo()
        self.live_page()

    def sub_co_host(self):
        self.coHost()
        self.live_page()

    def sub_audio(self):
        self.audio()
        self.live_page()

    def sub_team(self):
        self.team()
        self.live_page()

    def sub_all(self):
        self.all()
        self.live_page()

    def sub_for_you(self):
        self.for_you()
        self.live_page()

    def notification(self):
        self.view_notification()
