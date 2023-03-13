import time
import pytest

from android.page_object.livestreams.livestream_page import CreateLivestream
from android.page_object.login_page import LoginProcedure


@pytest.mark.usefixtures('setup')
class TestCreateSoloLivestream(LoginProcedure, CreateLivestream):
    @pytest.mark.cohost
    def test_create_solo_livestream(self):
        self.login_account(account="franz", account_type="dev_main")
        time.sleep(3)
        self.close_dashboard_adds()
        self.accept_terms()
        # self.driver.start_recording_screen()
        time.sleep(3)
        self.verify_tour_popup()
        time.sleep(3)
        self.verify_live_tab()
        self.tap_karlito_logo()
        self.select_post_or_live(option="livestream")
        time.sleep(5)
        self.allow_camera_popup()
        self.allow_mic_popup()
        self.livestream_tutorial()
        self.solo_livestream()
        time.sleep(6)
        self.verify_solo_livestream_started()
        self.close_livestream()
        self.driver.quit()
        # # self.stop_local()
