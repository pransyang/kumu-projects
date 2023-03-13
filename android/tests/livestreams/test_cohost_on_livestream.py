import pytest

from android.page_object.livestreams.livestream_page import CreateLivestream
from api_actions.api_methods import LivestreamApi, LoginActionApi
from android.page_object.livestreams.cohost_livestream import CohostLivestream


@pytest.mark.usefixtures("host_account")
class TestCohostOnLivestream(LivestreamApi, LoginActionApi, CohostLivestream, CreateLivestream):
    def test_cohost_livestream_2seat(self, host_account):
        self.creds = self.create_livestream(host_account, 101)
        self.login_account(account="franz", account_type="dev_alt")
        self.dashboard()
        self.select_livestream_account(search_account="test_franz101")
        ex_headers = self.creds[0]
        c_id = self.creds[1]
        print(c_id)
        self.click_cohost_btn()
        self.verify_cohost()
        self.end_cohost()
        self.exit_livestream()
        self.end_livestream(ex_headers, c_id)
        self.back_to_homepage()

    def test_cohost_livestream_4seat(self, host_account):
        self.creds = self.create_livestream(host_account, 4)
        self.select_livestream_account(search_account="test_franz101")
        ex_headers = self.creds[0]
        c_id = self.creds[1]
        self.click_cohost_btn()
        self.verify_cohost()
        self.end_cohost()
        self.exit_livestream()
        self.end_livestream(ex_headers, c_id)
        self.back_to_homepage()

    #
    def test_cohost_livestream_6seatA(self, host_account):
        self.creds = self.create_livestream(host_account, 61)
        self.select_livestream_account(search_account="test_franz101")
        ex_headers = self.creds[0]
        c_id = self.creds[1]
        self.click_cohost_btn()
        self.verify_cohost()
        self.end_cohost()
        self.exit_livestream()
        self.end_livestream(ex_headers, c_id)
        self.back_to_homepage()

    def test_cohost_livestream_6seatB(self, host_account):
        self.creds = self.create_livestream(host_account, 62)
        self.select_livestream_account(search_account="test_franz101")
        ex_headers = self.creds[0]
        c_id = self.creds[1]
        self.click_cohost_btn()
        self.verify_cohost()
        self.end_cohost()
        self.exit_livestream()
        self.end_livestream(ex_headers, c_id)
        self.back_to_homepage()

    def test_cohost_livestream_9(self, host_account):
        self.creds = self.create_livestream(host_account, 9)
        self.select_livestream_account(search_account="test_franz101")
        ex_headers = self.creds[0]
        c_id = self.creds[1]
        self.click_cohost_btn()
        self.verify_cohost()
        self.end_cohost()
        self.exit_livestream()
        self.end_livestream(ex_headers, c_id)
        self.back_to_homepage()
