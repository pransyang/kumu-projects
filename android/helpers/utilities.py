import json
import os

import requests
import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from android.conftest import user, device
user_name = os.environ.get('BS_USER')
access_key = os.environ.get('BS_KEY')
get_device = device.split("_")
device_name = get_device[0]
env = get_device[1]


class SetupDevice:
    @staticmethod
    def get_account():
        caps_file = None
        u_name = user
        print(u_name)
        users = os.listdir("./android/helpers/capabilities")
        # print(f" :: {type(users)}")
        # print(f"{users[0]}")
        index = 0
        while index < len(users):
            # print(f"key : {users[index]}")
            split_filename = users[index].split("_")
            user_file = split_filename[0]
            # print(user_file)
            if user_file == u_name:
                caps_file = users[index]
                # print(caps_file)
                break
            else:
                pass
            index += 1
        print(f"user is caps file {caps_file}")
        return caps_file

    @staticmethod
    def set_capabilites():
        account = SetupDevice.get_account()
        abs_path = os.path.abspath(f"./android/helpers/capabilities/{account}")
        file = open(abs_path)
        caps = json.load(file)
        try:
            desired_caps = caps[device]
        except KeyError:
            print("device name is invalid. please choose from the ff : local_dev, local_prod, appium_dev, "
                  "and appium_prod or add the new set of capabilities to your desired_caps file.")
            raise
        # print(desired_caps)
        # print(device_name)
        # print(user_name)
        # print(access_key)
        if device_name == "appium":
            desired_caps["browserstack.user"] = user_name
            desired_caps["browserstack.key"] = access_key
            desired_caps["browserstack.ke"] = access_key
        print(desired_caps)
        return desired_caps


class KumuBaseClass(SetupDevice):
    # get_device = device.split("_")
    wd = device_name
    if wd == "appium":
        url = f"https://{user_name}:{access_key}@hub-cloud.browserstack.com/wd/hub"
    elif wd == "local":
        url = "http://127.0.0.1:4723/wd/hub"
    # bs_local = Local()
    desired_capabilities = SetupDevice.set_capabilites()

    # Initialize the remote Webdriver using BrowserStack remote URL
    driver = webdriver.Remote(
        command_executor=url,
        desired_capabilities=desired_capabilities)

    # Webdriver shortcut objects
    wait = WebDriverWait(driver, 30)
    short_wait = WebDriverWait(driver, 5)
    clickable = EC.element_to_be_clickable
    visible = EC.visibility_of_element_located
    driver.implicitly_wait(60)
    env = env
    user = user
    device = device_name

    # def start_local(self):
    #     bs_local_args = {"key": self.access_key, "forcelocal": "true"}
    #     self.bs_local.start(**bs_local_args)
    #
    # def stop_local(self):
    #     self.bs_local.stop()

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
