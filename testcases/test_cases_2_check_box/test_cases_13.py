import pytest
import softest
from base.base_driver import Base_Page
from pages.laungh_page import Launch_Page
from pages.tools_page_check_box import Tools_Page_Check_Box



@pytest.mark.usefixtures("setup")

class Test_Base_Page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.bd = Base_Page(self.driver)
        self.lp = Launch_Page(self.driver)
        self.tpcb = Tools_Page_Check_Box(self.driver)

    def test_launch(self):
        self.bd.scroll_page_to_down_page()
        self.lp.click_to_button_elements()
        self.tpcb.click_to_button_tag_text_box()

        self.bd.scroll_page_to_down_page()
        self.tpcb.click_to_button_plus_home()
        self.tpcb.get_button_tick_home()
        self.tpcb.click_to_button_minus_home()
        self.tpcb.get_invisibility_element_private()

