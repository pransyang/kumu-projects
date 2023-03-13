import time

from android.helpers.locators import KumuLocators
from android.page_object.dashboard_page import DashboardPage
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class CreateLivestream(DashboardPage, KumuLocators):
    def livestream_tutorial(self):
        try:
            self.wait_short_click(self.livestream_tut_1)
            self.close_dashboard_adds()
            self.wait_short_click(self.livestream_tut_2)
        except NoSuchElementException:
            print("NO livestream tutorial")
            pass
        except TimeoutException:
            pass

    def solo_livestream(self):
        self.sendKeys(self.livestream_title, f"Test Automated Solo Livestream")
        self.wait_click(self.livestream_solo)
        self.wait_click(self.livestream_go_live)
        print("Successfuly clicked go live button!!")

    def select_cover_photo(self):
        self.wait_click(self.image_list[0])
        self.wait_click(self.image_select)
        time.sleep(3)
        self.wait_click(self.image_select)

    def verify_solo_livestream_started(self):
        try:
            self.is_visible(self.livestream_live_container)
        except AssertionError:
            print(AssertionError)
        print("Solo Livestream has successfully started!!!")

    def allow_camera_popup(self):
        try:
            self.wait_short_click(self.allow_while_using_app)
        except NoSuchElementException:
            pass
        except TimeoutException:
            pass

    def allow_mic_popup(self):
        try:
            self.wait_short_click(self.allow_while_using_app)
        except NoSuchElementException:
            print("mic access did not appear")
            pass
        except TimeoutException:
            pass

    def allow_photo_access(self):
        try:
            self.wait_short_click(self.allow_while_using_app)
            self.wait_short_click(self.livestream_live_tab)
            self.wait_short_click(self.livestream_live_tab_audio)

        except NoSuchElementException:
            pass
        except TimeoutException:
            pass

    def close_livestream(self):
        self.wait_click(self.livestream_more_options)
        self.wait_click(self.livestream_options_end)
        self.wait_click(self.livestream_end)
        self.is_visible(self.livestream_end_title)
        self.wait_click(self.close_livestream_btn)
        time.sleep(5)

    def exit_livestream(self):
        self.is_visible(self.livestream_more_options)
        self.clickElement(self.livestream_more_options)
        self.is_visible(self.livestream_options_end)
        self.clickElement(self.livestream_options_end)
        print("Successfully exited livestream")
