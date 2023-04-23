import allure
import pytest
import softest
from base.base_driver import Base_Page
from pages.laungh_page import Launch_Page


@pytest.mark.usefixtures("setup")

class Test_Base_Page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.bd = Base_Page(self.driver)
        self.lp = Launch_Page(self.driver)


    def test_cases_3(self):
        self.bd.scroll_page_to_down_page()
        self.lp.click_to_button_elements()


