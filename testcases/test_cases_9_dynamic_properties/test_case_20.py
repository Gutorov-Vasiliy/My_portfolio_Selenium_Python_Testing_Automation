import time

import allure
import pytest
import softest
from base.base_driver import Base_Page
from pages.laungh_page import Launch_Page
from pages.tools_page_dynamic_properties import Tools_Page_Dynamic_Properties
from utilities.utilites_site import Utils


@pytest.mark.usefixtures("setup")
class Test_Base_Page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.bd = Base_Page(self.driver)
        self.lp = Launch_Page(self.driver)
        self.ut = Utils()
        self.tpdp = Tools_Page_Dynamic_Properties (self.driver)


    def test_cases_20(self):
        self.bd.scroll_page_to_down_page()
        self.lp.click_to_button_elements()
        self.bd.scroll_page_to_down_page()

        self.tpdp.click_to_button_dynamic_properties()

        self.tpdp.click_to_button_will_enable_5_seconds()
        self.tpdp.click_to_button_color_change()
        self.tpdp.click_to_button_visible_after_5_seconds()
