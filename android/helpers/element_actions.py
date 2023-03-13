from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import sys
import os
from android.helpers.utilities import KumuBaseClass
from selenium.webdriver.support.ui import WebDriverWait


class Actions(KumuBaseClass):
    # Webdriver shortcut objects

    def clickElement(self, locator):
        try:
            wait = WebDriverWait(self.driver, 60)
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except NoSuchElementException as element:
            print(element)
            raise

    def sendKeys(self, locator, value):
        wait = WebDriverWait(self.driver, 30)
        try:
            element = wait.until(EC.element_to_be_clickable((locator[0], locator[1])))
            element.clear()
            element.send_keys(value)
        except Exception as ex:
            print(ex)

    def is_visible(self, locator):
        wait = WebDriverWait(self.driver, 30)
        try:
            element = wait.until(EC.visibility_of_element_located((locator[0], locator[1])))
            # assert element.is_displayed(), "Element is not visible"
            print("element is visble")
        except Exception as ex:
            print(ex)
        except NoSuchElementException as no_element:
            print(no_element)

    def status_controller(self, status, reason):
        script = 'browserstack_executor: {"action": "setSessionStatus", ' \
                 '"arguments": {"status":"' + status + '", "reason": "' + reason + '"}} '
        self.driver.execute_script(script)

    def wait_click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def wait_short_click(self, locator):
        self.short_wait.until(EC.element_to_be_clickable(locator)).click()

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_enabled()

    def wait_displayed(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def wait_send_keys(self, locator, keys):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(keys)

    def wait_short_keys(self, locator, keys):
        self.short_wait.until(EC.visibility_of_element_located(locator)).send_keys(keys)

    def wait_short_clear(self, locator):
        self.short_wait.until(EC.visibility_of_element_located(locator)).clear()

    def wait_short_visible(self, locator):
        self.short_wait.until(EC.visibility_of_element_located(locator)).is_enabled()

    def wait_short_displayed(self, locator):
        return self.short_wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def wait_get_text(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator)).get_attribute("text")
