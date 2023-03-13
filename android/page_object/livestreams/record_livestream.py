import time
from android.helpers.element_actions import Actions
from android.helpers.locators import KumuLocators
from selenium.common.exceptions import NoSuchElementException
from android.page_object.livestreams.livestream_page import CreateLivestream
from android.page_object.login_page import LoginProcedure


class RecordLivestream(KumuLocators, Actions):
    def select_livestream(self):
        ls = self.driver.find_elements("xpath", self.ls_stream)
        self.clickElement(ls[0])
        print("livestream selected")

    def click_record_button(self):
        time.sleep(3)
        # tap anywhere on screen
        self.driver.tap([(0, 1950), ([1440, 2160])], 100)
        self.driver.tap([(0, 1950), ([1440, 2160])], 100)
        self.driver.tap([(0, 1950), ([1440, 2160])], 100)
        # assert self.is_visible(self.ls_record_btn), "Cannot locate record button"
        self.clickElement(self.ls_record_btn)
        time.sleep(3)
        self.verify_allow_audio_photo_access()
        self.clickElement(self.ls_record_btn)
        self.verify_start_record_popup()
        print("clicked record button")

    def save_recorded_klip(self):
        time.sleep(10)
        self.is_visible(self.save_video_container)
        self.is_visible(self.share_button)
        self.clickElement(self.save_video_btn)
        self.clickElement(self.close_container)

    def allow_recording(self):
        print("")

    def verify_klip_recorder(self):
        print("")

    def verify_allow_audio_photo_access(self):
        try:
            self.clickElement(self.allow_while_using_app)
            self.clickElement(self.allow_media_access_btn)
        except NoSuchElementException:
            pass

    def verify_start_record_popup(self):
        try:
            start_record_container = self.wait_displayed(self.allow_recording_holder)
            if start_record_container is True:
                self.wait_short_click(self.start_recording)
        except NoSuchElementException:
            pass

    def post_comment(self):
        self.is_visible(self.say_hi_btn)
        self.clickElement(self.say_hi_btn)
        self.is_visible(self.comment_text_field)
        self.sendKeys(self.comment_text_field, "hi")
        self.is_visible(self.comment_send_btn)
        self.clickElement(self.comment_send_btn)
        print("User commented on livestream")
