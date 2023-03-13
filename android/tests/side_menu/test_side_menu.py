from android.page_object.side_menu_object.side_menu_page import SideMenuPage
import pytest


class TestSideMenu(SideMenuPage):
    @pytest.mark.cohost
    def test_campaign(self):
        self.dashboard()
        self.campaign()
