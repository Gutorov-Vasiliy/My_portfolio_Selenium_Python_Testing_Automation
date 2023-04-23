import time
import allure
import pytest
import softest
from base.base_driver import Base_Page
from pages.laungh_page import Launch_Page
from pages.tools_page_practice_form import Tools_Page_Practice_Form



@pytest.mark.usefixtures("setup")
class Test_Base_Page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.bd = Base_Page(self.driver)
        self.lp = Launch_Page(self.driver)
        self.tppf = Tools_Page_Practice_Form(self.driver)

    @allure.title("test_case_21/Person form")
    def test_cases_21(self):
        self.bd.scroll_page_to_down_page()
        self.lp.click_to_button_elements()
        self.bd.scroll_page_to_down_page()

        self.tppf.click_to_tab_dynamic_forms()
        self.tppf.click_to_button_practice_form()
        self.bd.scroll_page_to_down_page()

        #self.tppf.()
        self.tppf.click_to_button_first_name("Vasiliy")

        self.tppf.click_to_button_last_name("Gutorov")

        self.tppf.click_to_button_user_mail("gutorov.vasia@mail.ru")

        self.tppf.click_to_button_male()

        self.tppf.click_to_button_user_number("+375291111111")

        self.tppf.click_to_date_of_birth_input()
        self.tppf.click_to_month_select("October")
        self.tppf.click_to_year_select("1996")
        self.tppf.enter_departure_date("Choose Monday, October 7th, 1996")

        self.tppf.click_to_subjects("Math")

        self.tppf.click_to_sports()
        self.tppf.click_to_button_reading()
        self.tppf.click_to_button_music()

        self.bd.scroll_page_to_down_page()

        self.tppf.click_to_button_select_a_file()

        self.tppf.click_to_current_address("Minsk")
        time.sleep(5)



