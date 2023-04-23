import allure
import pytest
import softest
from base.base_driver import Base_Page
from pages.laungh_page import Launch_Page
from pages.tools_page_buttons import Tools_Page_Buttons
from utilities.utilites_site import Utils


@pytest.mark.usefixtures("setup")
class Test_Base_Page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.bd = Base_Page(self.driver)
        self.lp = Launch_Page(self.driver)
        self.tpb = Tools_Page_Buttons(self.driver)


    def test_cases_16(self):
        self.bd.scroll_page_to_down_page()
        self.lp.click_to_button_elements()
        self.bd.scroll_page_to_down_page()
        self.tpb.click_to_button_tag_buttons()
        self.tpb.click_to_button_double_click()
        self.tpb.click_to_button_right_click()
        self.tpb.click_to_button_click_me()


        #Проверка на всплывающую надвись после нажатия double click
        self.tpb.get_result_after_button_double_click_me()
        self.tpb.get_result_after_button_right_click_me()
        self.tpb.get_result_after_button_click_me()
