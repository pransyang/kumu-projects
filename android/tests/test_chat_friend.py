from android.page_object.chat_friend import ChatFriend
from android.page_object.login_page import LoginProcedure
from android.page_object.search_object.search_page import SearchObject


class TestChatFriend(ChatFriend, LoginProcedure, SearchObject):
    def test_chat_friend(self):
        self.login_account("franz", "dev_sub")
        self.dashboard()
        self.search_data("test_franz101")
        self.tap_search_user()
        self.verify_user_followed()
        self.click_message_btn()
        self.verify_chat_box()
        self.send_message()
        self.driver.quit()
