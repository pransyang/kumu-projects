import time
import pytest

from android.page_object.livestreams.livestream_page import CreateLivestream
from android.page_object.livestreams.record_livestream import RecordLivestream
from android.page_object.livestreams.group_livestream_page import  GroupLivestreamPage


# @pytest.mark.usefixtures('setup')
class TestRecordLivestream(RecordLivestream, GroupLivestreamPage, CreateLivestream):
    # @pytest.mark.cohost
    def test_login(self):
        self.dashboard()

    def test_record_livestream(self):
        self.select_livestream()
        self.click_record_button()
        self.save_recorded_klip()
        # self.exit_livestream()

    def test_comment_livestream(self):
        # self.select_livestream()
        self.post_comment()
        self.exit_livestream()
        self.driver.quit()

