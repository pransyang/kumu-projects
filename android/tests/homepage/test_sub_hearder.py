from android.page_object.homepage_object.homepage_object import homepage
import pytest




class TestSideMenu(homepage):
    def test_login(self):
        self.dashboard()

    def test_newbies(self):
        self.sub_newbies()

    def test_solo(self):
        self.sub_solo()

    def test_cohost(self):
        self.sub_co_host()

    def test_audio(self):
        self.sub_audio()

    def test_team(self):
        self.sub_team()

    def test_all(self):
        self.sub_all()

    def test_for_you(self):
        self.sub_for_you()

    def test_notif(self):
        self.notification()

    def quit(self):
        self.driver.quit()
