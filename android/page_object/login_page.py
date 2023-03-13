import time

import pytest
# from selenium.common import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoSuchElementException, TimeoutException


from android.helpers.locators import KumuLocators
from fixtures.account_and_otp import LoginReq


# @pytest.mark.usefixtures('locators')
class LoginPage(KumuLocators, LoginReq):
    def account_number(self, account, account_type):
        account = self.get_test_account(account, account_type)
        # new_number = account["number"]
        return account

    def tap_on_login_button(self):
        self.wait_click(self.login_button)

    def skip_intro(self):
        try:
            self.wait_short_click(self.intro_skip)
        except (NoSuchElementException, TimeoutException):
            pass

    def input_mobile_number(self, phone_number):
        # self.wait.until(self.visible(self.phone_number)).send_keys(self.phone_number())
        self.sendKeys(self.phone_number_field, phone_number)

    def change_country_code(self):
        self.clickElement(self.country_code_selector)
        self.sendKeys(self.country_code_search, "PH")
        self.clickElement(self.country_code_result)

    def sign_in(self):
        self.clickElement(self.sign_in_button)

    def otp_input(self, phone_number, otp):
        print(f"phone number: {phone_number}")
        # new_num = phone_number['number']
        # magic_mode = phone_number['otp']
        if otp == "None":
            otp_caught = self.get_otp_code(account=phone_number)
        else:
            otp_caught = otp
        print(otp_caught)
        otp_pin = self.split(word=otp_caught)
        # print(otp_pin)
        # print(type(otp_pin))
        time.sleep(5)
        index = 0
        for pin in range(0, 6):
            self.numpad_code(num=int(otp_pin[index]))
            index += 1

    def numpad_code(self, num):
        if num == 0:
            self.driver.press_keycode(144)
        elif num == 1:
            self.driver.press_keycode(145)
        elif num == 2:
            self.driver.press_keycode(146)
        elif num == 3:
            self.driver.press_keycode(147)
        elif num == 4:
            self.driver.press_keycode(148)
        elif num == 5:
            self.driver.press_keycode(149)
        elif num == 6:
            self.driver.press_keycode(150)
        elif num == 7:
            self.driver.press_keycode(151)
        elif num == 8:
            self.driver.press_keycode(152)
        elif num == 9:
            self.driver.press_keycode(153)
        else:
            print("Invalid Number!")


class LoginProcedure(LoginPage):
    def login_account(self, account, account_type):
        time.sleep(5)
        account = self.account_number(account, account_type)
        time.sleep(3)
        self.tap_on_login_button()
        # self.skip_intro()
        print(account)
        number = account['number']
        otp = account['otp']
        print(f"otp {otp}")
        self.input_mobile_number(number)
        self.change_country_code()
        self.sign_in()
        self.otp_input(number, otp)
