import time
from android.helpers.locators import KumuLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class SendGifts(KumuLocators):
    def click_send_gift_btn(self):
        self.driver.tap([(0, 1950), ([1440, 2160])], 100)
        self.driver.tap([(0, 1950), ([1440, 2160])], 100)
        self.driver.tap([(0, 1950), ([1440, 2160])], 100)
        self.driver.tap([(0, 1950), ([1440, 2160])], 100)
        assert self.wait_displayed(self.ls_send_gift) is True, "Send gift icon is not visible"
        self.wait_click(self.ls_send_gift)
        print("Click send send gift icon")

    def verify_gifts_banner(self):
        assert self.wait_displayed(self.ls_gifts_banner) is True, "Gifts Banner is not visible !"
        assert self.wait_displayed(self.ls_gifts_coins_banner) is True, "Coins topup is not visible !"
        assert self.wait_displayed(self.ls_gifts_topup_banner) is True, "Give gift banner is not visible !"
        print("Gifts banner is visible")

    def select_gift(self):
        # halo = self.driver.find_elements("xpath", self.ls_gift)
        self.wait_click(self.halo_halo)

    def click_give_btn(self):
        assert self.wait_visible(self.comment_send_btn) is True, "Send gift icon is not visible"
        self.wait_click(self.comment_send_btn)
        print("Clicked give gift button")
        self.driver.back()
