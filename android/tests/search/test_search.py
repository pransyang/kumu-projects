from android.page_object.search_object.search_page import Search
import pytest


class TestSearch(Search):
    def test_login(self):
        self.dashboard()

    def test_search_tab(self):
        self.search_page()
        self.driver.quit()
