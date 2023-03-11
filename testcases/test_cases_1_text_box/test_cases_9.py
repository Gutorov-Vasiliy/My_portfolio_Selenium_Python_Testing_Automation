import pytest
import softest

from base.base_driver import Base_Page
from pages.laungh_page import Launch_Page
from pages.tools_page_text_box import Tools_Page_Text_Box
from utilities.utilites_site import Utils


@pytest.mark.usefixtures("setup")
class Test_Base_Page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.bd = Base_Page(self.driver)
        self.lp = Launch_Page(self.driver)
        self.tl = Tools_Page_Text_Box(self.driver)
        self.ut = Utils()

    def test_launch(self):
        self.bd.scroll_page_to_down_page()
        self.lp.click_to_button_elements()
        self.tl.click_to_button_tag_text_box()
        self.bd.scroll_page_to_down_page()
        self.tl.enter_depart_from_location("Gutorov Vasiliy", "gutorov.vasia@yandex.ru", "Vitebsk", "Minsk")
        self.tl.click_to_button_submit()

    # Проверка имени зарегистрированного пользователя
        all_results_registration_name = self.tl.get_result_registration_name()
        self.ut.assert_result_registration(all_results_registration_name, "Name:"+"Gutorov Vasiliy")

    # Проверка емаил зарегистрированного пользователя
        all_results_registration_email = self.tl.get_result_registration_email()
        self.ut.assert_result_registration(all_results_registration_email, "Email:" + "gutorov.vasia@yandex.ru")

    # Проверка точки отправления товара
        all_results_registration_current_address = self.tl.get_result_registration_current_address()
        self.ut.assert_result_registration(all_results_registration_current_address, "Current Address :" + "Vitebsk")

    # Проверка точки прибытия товара
        all_results_registration_permanent_address = self.tl.get_result_registration_permanent_address()
        self.ut.assert_result_registration(all_results_registration_permanent_address, "Permananet Address :" + "Minsk")




