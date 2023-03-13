import time
import pytest

from android.page_object.livestreams.group_livestream_page import GroupLivestreamPage


# @pytest.mark.usefixtures('setup')
class TestCreateGroupLivestream(GroupLivestreamPage):
    @pytest.mark.cohost
    def test_group_livestream_2seats(self):
        self.dashboard()
        # seat = 1
        self.livestream_setup(1)

    def test_group_livestream_4seats(self):
        # seat = 2
        self.livestream_setup(2)

    def test_group_livestream_6seatsA(self):
        # seat = 3
        self.livestream_setup(3)

    def test_group_livestream_6seatB(self):
        # seat = 4
        self.livestream_setup(4)

    def test_group_livestream_9seats(self):
        # seat = 5
        self.livestream_setup(5)

    def end_test(self):
        self.driver.quit()
