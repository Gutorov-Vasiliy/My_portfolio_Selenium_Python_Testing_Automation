import time
import pytest
import softest
from base.base_driver import Base_Page
from pages.laungh_page import Launch_Page
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

    def test_links(self):
        self.bd.scroll_page_to_down_page()
        self.lp.click_to_button_elements()
        self.bd.scroll_page_to_down_page()

        self.tpl.click_to_button_links()
        self.tpl.click_to_button_home()

        self.tpl.switching_between_browser_tabs(1)
        self.lp.click_to_button_tools_qa()

        self.tpl.switching_between_browser_tabs(0)
        self.tpl.click_to_button_home9Cbfw()

        self.tpl.switching_between_browser_tabs(2)
        self.lp.click_to_button_tools_qa()

        self.tpl.switching_between_browser_tabs(0)

        self.bd.scroll_page_to_down_page()
        self.tpl.click_to_button_created()
        self.tpl.get_incscription_created()

        self.bd.scroll_page_to_down_page()
        self.tpl.click_to_button_no_content()
        self.tpl.get_incscription_no_content()

        self.bd.scroll_page_to_down_page()
        self.tpl.click_to_button_moved()
        self.tpl.get_incscription_moved()

        self.bd.scroll_page_to_down_page()
        self.tpl.click_to_button_bad_request()
        self.tpl.get_incscription_bad_request()

        self.bd.scroll_page_to_down_page()
        self.tpl.click_to_button_unauthorized()
        self.tpl.get_incscription_unauthorized()

        self.bd.scroll_page_to_down_page()
        self.tpl.click_to_button_forbidden()
        self.tpl.get_incscription_forbidden()

        self.bd.scroll_page_to_down_page()
        self.tpl.click_to_button_not_found()
        self.tpl.get_incscription_not_found()

