import time
import pytest
import softest
from base.base_driver import Base_Page
from pages.laungh_page import Launch_Page
from pages.tools_page_web_tables import Tools_Page_Web_Tables



@pytest.mark.usefixtures("setup")

class Test_Base_Page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.bd = Base_Page(self.driver)
        self.lp = Launch_Page(self.driver)
        self.tpwt = Tools_Page_Web_Tables(self.driver)

    def test_loading(self):
        self.bd.scroll_page_to_down_page()
        self.lp.click_to_button_elements()
        self.tpwt.click_to_button_tab_web_tables()
        self.tpwt.click_to_button_edit("Vega", "edit-record-1")
        time.sleep(10)