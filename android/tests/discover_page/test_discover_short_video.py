from android.page_object.discover_page.discover_page_object import discover_page 


class TestDiscoverPage(discover_page): 
    def test_discover(self):
        self.dashboard()
        self.discover_step() 
        self.driver.quit()

    
    
