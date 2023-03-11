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

        self.tpcb.click_to_button_arrow_home()

        self.tpcb.click_to_button_tick_home_desktop()
        self.tpcb.click_to_button_tick_home_desktop_notes()
        self.tpcb.click_to_button_tick_home_desktop_commands()

        self.tpcb.click_to_button_tick_home_documents()
        self.tpcb.click_to_button_tick_home_documents_work_space()
        self.tpcb.click_to_button_tick_home_documents_work_space_react()
        self.tpcb.click_to_button_tick_home_documents_work_space_angular()
        self.tpcb.click_to_button_tick_home_documents_work_space_veu()

        self.tpcb.click_to_button_tick_home_documents_office()
        self.tpcb.click_to_button_tick_home_documents_office_public()
        self.tpcb.click_to_button_tick_home_documents_office_private()
        self.tpcb.click_to_button_tick_home_documents_office_classified()
        self.tpcb.click_to_button_tick_home_documents_office_general()

        self.tpcb.click_to_button_tick_home_downloades()
        self.tpcb.click_to_button_tick_home_downloades_word_file()
        self.tpcb.click_to_button_tick_home_downloades_excel_file()

        #Проверка нажатых галочек
        self.tpcb.get_result_tick_home()
        self.tpcb.get_result_tick_desktop()
        self.tpcb.get_result_tick_notes()
        self.tpcb.get_result_tick_commands()
        self.tpcb.get_result_tick_documents()
        self.tpcb.get_result_tick_workspace()
        self.tpcb.get_result_tick_react()
        self.tpcb.get_result_tick_angular()
        self.tpcb.get_result_tick_veu()
        self.tpcb.get_result_tick_office()
        self.tpcb.get_result_tick_public()
        self.tpcb.get_result_tick_private()
        self.tpcb.get_result_tick_classified()
        self.tpcb.get_result_tick_general()
        self.tpcb.get_result_tick_downloads()
        self.tpcb.get_result_tick_word_file()
        self.tpcb.get_result_tick_excel_file()



