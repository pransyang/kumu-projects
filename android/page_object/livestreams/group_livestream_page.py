import time
from android.helpers.element_actions import Actions
from android.helpers.locators import KumuLocators
from selenium.common.exceptions import NoSuchElementException
from android.page_object.livestreams.livestream_page import CreateLivestream
from android.page_object.login_page import LoginProcedure


class Group(KumuLocators, Actions):
    def group_livestream(self):
        self.wait_click(self.livestream_group)
        print("User selected group livestream")

    def select_cohost_seat(self, max_seat):
        self.clickElement(self.livestream_cohost)
        seat = self.cohost_seat(max_seat)
        self.clickElement(seat)
        self.driver.swipe(1000, 2000, 56, 1530)
        self.clickElement(self.cohost_save)
        self.clickElement(self.livestream_go_live)
        print("User selected a seat")

    def cohost_seat(self, max_seat):
        seat = None
        if max_seat == 1:
            seat = self.cohost_seats_2
        elif max_seat == 2:
            seat = self.cohost_seats_4
        elif max_seat == 3:
            seat = self.cohost_seats_6A
        elif max_seat == 4:
            seat = self.cohost_seats_6B
        elif max_seat == 5:
            seat = self.cohost_seats_9
        else:
            print("seat is not valid ")
        print(f"seat ::  {seat}")
        return seat

    def verify_cohost_livestream_started(self):
        livestream_cointainer = self.wait_visible(self.cohost_livestream_container)
        assert livestream_cointainer is True, "Livestream Container is not visible!!"


class GroupLivestreamPage(CreateLivestream, LoginProcedure, Group):
    def dashboard(self):
        self.login_account(account="franz", account_type="dev_main")
        time.sleep(3)
        self.close_dashboard_adds()
        self.accept_terms()
        time.sleep(3)
        self.verify_tour_popup()
        self.verify_live_tab()

    def livestream_setup(self, max_seat):
        print(max_seat)
        self.tap_karlito_logo()
        self.select_post_or_live(option="livestream")
        # time.sleep(5)
        if max_seat == 1:
            self.allow_camera_popup()
            self.allow_mic_popup()
        self.livestream_tutorial()
        self.group_livestream()
        self.select_cohost_seat(max_seat)
        self.verify_cohost_livestream_started()
        self.close_livestream()
        # self.driver.quit()
