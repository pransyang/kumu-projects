import time
import pytest
from android.page_object.livestreams.cohost_livestream import CohostLivestream
from android.page_object.livestreams.livestream_page import CreateLivestream
from api_actions.api_methods import LivestreamApi, LoginActionApi
from android.page_object.livestreams.send_gits import SendGifts


@pytest.mark.usefixtures("host_account")
class TestSendGift(LivestreamApi, LoginActionApi, SendGifts, CreateLivestream, CohostLivestream):
    def test_send_gift(self, host_account):
        self.creds = self.create_livestream(host_account, 1)
        self.login_account(account="franz", account_type="dev_alt")
        self.dashboard()
        self.select_livestream_account(search_account="test_franz101")
        ex_headers = self.creds[0]
        c_id = self.creds[1]
        print(c_id)
        self.click_send_gift_btn()
        self.verify_gifts_banner()
        self.select_gift()
        self.click_give_btn()
        time.sleep(10)
        self.exit_livestream()
        self.end_livestream(ex_headers, c_id)
        self.back_to_homepage()
