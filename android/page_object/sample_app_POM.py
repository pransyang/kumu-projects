from android.helpers.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SampleAppPOM(Locators):

    def click_search(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.search_wiki)).click()

    def search_word(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.type_search)).send_keys("BrowserStack")

    def search_result(self):
        search_results = self.driver.find_elements_by_class_name("android.widget.TextView")
        return search_results
