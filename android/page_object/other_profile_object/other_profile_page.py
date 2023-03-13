from android.page_object.dashboard_page import DashboardPage
from android.page_object.login_page import LoginProcedure


class OtherProfilePage(DashboardPage, LoginProcedure):
    def view_post(self):
        self.wait_click(self.post_content)

    def like_post(self):
        btn_like = self.wait_displayed(self.post_like)
        assert btn_like is True, "Like button is not enabled"
        self.wait_click(self.post_like)

    def comment(self, comment_data):
        btn_comment = self.wait_displayed(self.comment_button)
        assert btn_comment is True, "Comment button is not enabled"
        self.wait_click(self.comment_button)
        self.wait_send_keys(self.post_comment_input_box, comment_data)
        self.wait_click(self.post_timeline_button)
        self.driver.press_keycode(4)

    def back_feed_page(self):
        self.wait_click(self.post_close_view_button)
