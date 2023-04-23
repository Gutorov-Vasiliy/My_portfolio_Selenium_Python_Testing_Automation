import time
import allure
import pytest
import softest
from base.base_driver import Base_Page
from pages.laungh_page import Launch_Page
from pages.tools_page_browser_windows import Tools_Page_Browser_Windows




@pytest.mark.usefixtures("setup")
class Test_Base_Page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.bd = Base_Page(self.driver)
        self.lp = Launch_Page(self.driver)
        self.tpbw = Tools_Page_Browser_Windows (self.driver)


    def test_cases_22(self):
        self.bd.scroll_page_to_down_page()
        self.lp.click_to_button_elements()
        self.bd.scroll_page_to_down_page()


        self.tpbw.click_to_button_alerts_frame_windows()
        time.sleep(1)
        self.tpbw.click_to_button_browser_windows()
        time.sleep(1)
        self.tpbw.click_to_button_new_tab(1, 0)
        time.sleep(1)
