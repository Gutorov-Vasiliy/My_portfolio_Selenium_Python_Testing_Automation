import time
import pytest
import softest
from base.base_driver import Base_Page
from pages.laungh_page import Launch_Page
from pages.tools_page_broken_links import Tools_Page_Broken_links
from pages.tools_page_links import Tools_Page_Links
from utilities.utilites_site import Utils


@pytest.mark.usefixtures("setup")
class Test_Base_Page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.bd = Base_Page(self.driver)
        self.lp = Launch_Page(self.driver)
        self.ut = Utils()
        self.tpl = Tools_Page_Links(self.driver)
        self.tpbl = Tools_Page_Broken_links(self.driver)

    def test_links(self):
        self.bd.scroll_page_to_down_page()
        self.lp.click_to_button_elements()
        self.bd.scroll_page_to_down_page()
        self.tpbl.click_to_button_tag_broken_links()

        self.tpbl.get_valid_image()

        self.tpbl.get_broken_image()

        self.tpbl.click_to_button_click_here_for_valid_link()
        self.tpbl.get_incscription_valid_link()
        self.bd.scroll_page_to_down_page()
        self.lp.click_to_button_elements()
        self.bd.scroll_page_to_down_page()
        self.tpbl.click_to_button_tag_broken_links()

        self.tpbl.click_to_button_click_here_for_broken_link()
        self.tpbl.get_incscription_status_code_500()



