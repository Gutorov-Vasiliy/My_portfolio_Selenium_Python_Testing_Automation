import pytest
import softest
from pages.laungh_page import Launch_Page


@pytest.mark.usefixtures("setup")
class Test_Base_Page(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Launch_Page(self.driver)


    def test_launch(self):
        self.lp.click_to_button_selenuim_certification_training()


