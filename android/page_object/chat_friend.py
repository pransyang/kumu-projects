from android.helpers.locators import KumuLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class ChatFriend(KumuLocators):
    def verify_user_followed(self):
        try:
            follow_btn = self.wait_displayed(self.user_follow)
            if follow_btn is True:
                self.wait_short_click(self.user_follow)
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            print("Account is already followed by user")
            pass

    def click_message_btn(self):
        assert self.wait_displayed(self.profile_message_btn) is True, "Message button is not visible"
        self.wait_short_click(self.profile_message_btn)
        print("Clicked message button")

    def verify_chat_box(self):
        assert self.wait_short_displayed(self.chat_input_field) is True, "Chat input is not visible"
        assert self.wait_short_displayed(self.chat_camera_icon) is True, "Camera icon is not visible"
        assert self.wait_short_displayed(self.chat_img_icon) is True, "Image icon is visible"
        assert self.wait_short_displayed(self.username_text) is True, "Friend username is not visible"
        print("Chat box elements is displayed")

    def send_message(self):
        self.wait_send_keys(self.chat_input_field, "hi")
        self.wait_short_click(self.chat_send_btn)
        print("Successfully send a message.")
