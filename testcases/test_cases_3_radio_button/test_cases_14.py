import pytest
import softest
from base.base_driver import Base_Page
from pages.laungh_page import Launch_Page
from pages.tools_page_radio_button import Tools_Page_RADIO_BUTTON


@pytest.mark.usefixtures("setup")

class Test_Base_Page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.bd = Base_Page(self.driver)
        self.lp = Launch_Page(self.driver)
        self.tprb = Tools_Page_RADIO_BUTTON(self.driver)


    def test_launch(self):
        self.bd.scroll_page_to_down_page()
        self.lp.click_to_button_elements()
        self.tprb.click_to_button_tag_radio_button()
        self.tprb.click_to_button_yes()
        self.tprb.get_check_string_yes()
        self.tprb.click_to_button_impressive()
        self.tprb.get_check_string_impressive()
        self.tprb.check_button_for_non_clickability("custom-control-input disabled")
