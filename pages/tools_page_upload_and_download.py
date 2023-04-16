import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_driver import Base_Page
from utilities.utilites_site import Utils


class Tools_Page_Upload_And_Download(Base_Page):
    log = Utils.logging_site(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Кнопка UPLOAD_AND_DOWNLOAD в разделе Upload and Download
    BUTTON_UPLOAD_AND_DOWNLOAD = "//span[normalize-space()='Upload and Download']"

    def get_button_upload_and_download(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_UPLOAD_AND_DOWNLOAD)

    def click_to_upload_and_download(self):
        self.get_button_upload_and_download().click()
        #time.sleep(0.5)


    # Кнопка download в разделе Upload and Download
    BUTTON_DOWNLOAD = "//a[@id='downloadButton']"

    def get_button_download(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_DOWNLOAD)

    def click_to_button_download(self):
        self.get_button_download().click()
        #time.sleep(0.5)


    # Кнопка Select a file в разделе Web Tables
    BUTTON_SELECT_A_FILE = "//input[@id='uploadFile']"

    def get_button_select_a_file(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_SELECT_A_FILE)

    def click_to_button_select_a_file(self):
        self.get_button_select_a_file().click()
        #time.sleep(0.5)

    def select_file_from_pc(self):
        self.write_file_from_pc(By.XPATH, self.BUTTON_SELECT_A_FILE, "C:/Users/user/PycharmProjects/Test_Site/testdata/photo.jpeg")

