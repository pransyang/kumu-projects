# import time
#
# import pytest
#
# from android.page_object.sample_app_POM import SampleAppPOM
#
#
# @pytest.mark.skip
# class TestSampleApp(SampleAppPOM):
#     # Test case for the BrowserStack sample Android app.
#     # If you have uploaded your app, update the test case here.
#     def test_sample_app(self):
#         self.click_search()
#         self.search_word()
#         time.sleep(5)
#         assert (len(self.search_result()) > 0)
#
#         # Invoke driver.quit() after the test is done to indicate that the test is completed.
#         self.driver.quit()
