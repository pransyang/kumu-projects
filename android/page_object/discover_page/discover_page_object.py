from android.page_object.dashboard_page import DashboardPage
from android.page_object.login_page import LoginProcedure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from appium.webdriver.common.touch_action import TouchAction

import time

class discover(DashboardPage):
    def tap_discover_page(self):
        # discover = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Discover")')
        # discover.click()
        discover = self.wait_displayed(self.discover_page)
        assert discover is True, "Discover button is not displayed"
        self.wait_click(self.discover_page) 

    def tap_confirm_step(self):
        try:
            # game = "im.kumu.ph:id/tv_confirm_step1"
            # confirm = driver.find_element("id", game)
            # if confirm.is_displayed() is True:
            #     confirm.click()
            #     time.sleep(5)
            # else:
            #     pass 

            confirm = self.wait_displayed(self.game)
            if confirm is True:
                self.wait_click(self.game)
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            pass

    def swipe_discover(self):
        print("Device width and height: ", self.driver.get_window_size())
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']

        startx = screenWidth / 2
        endx = screenWidth / 2
        starty = screenHeight * 8 / 9
        endy = screenHeight / 9

        actions = TouchAction(self.driver)
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()


class discover_page(discover, LoginProcedure):
    def dashboard(self):
        self.login_account(account="matt", account_type="prod_main")
        time.sleep(6)
        self.close_dashboard_adds()
        time.sleep(3)
        self.verify_tour_popup()
        time.sleep(3) 

    def discover_step(self):
        self.tap_discover_page()
        time.sleep(3)
        self.tap_confirm_step()
        time.sleep(3)
        self.swipe_discover()
        time.sleep(3)
