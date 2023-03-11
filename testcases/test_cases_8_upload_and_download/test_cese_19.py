import time
import pytest
import softest
from base.base_driver import Base_Page
from pages.laungh_page import Launch_Page
from pages.tools_page_broken_links import Tools_Page_Broken_links
from pages.tools_page_links import Tools_Page_Links
from pages.tools_page_upload_and_download import Tools_Page_Upload_And_Download
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
        self.tpuad = Tools_Page_Upload_And_Download(self.driver)


    def test_links(self):
        self.bd.scroll_page_to_down_page()
        self.lp.click_to_button_elements()
        self.bd.scroll_page_to_down_page()

        self.tpuad.click_to_upload_and_download()
        time.sleep(3)
        #self.tpuad.click_to_button_download()
        time.sleep(5)
        self.tpuad.select_file_from_pc()
        time.sleep(5)
