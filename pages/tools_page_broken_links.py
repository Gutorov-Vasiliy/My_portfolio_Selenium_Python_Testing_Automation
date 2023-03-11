import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import Base_Page
from utilities.utilites_site import Utils
from selenium.webdriver import ActionChains

class Tools_Page_Broken_links (Base_Page):
    log = Utils.logging_site(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Кнопка Broken Links - Images в разделе Elements
    BUTTON_BROKEN_LINKS_IMAGES = "//span[normalize-space()='Broken Links - Images']"

    def get_tab_broken_links_images(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_BROKEN_LINKS_IMAGES)

    def click_to_button_tag_broken_links(self):
        self.get_tab_broken_links_images().click()
        time.sleep(0.5)


    # Проверка иконки Valid image в разделе Broken links
    VALID_IMAGE = "//div/div//img[@src='/images/Toolsqa.jpg']"
    def get_valid_image(self):
        return self.wait_until_visibility_of_element_located(By.XPATH, self.VALID_IMAGE)

    # Проверка иконки Broke image в разделе Broken links
    BROKEN_IMAGE = "//div/div//img[@src='/images/Toolsqa_1.jpg']"
    def get_broken_image(self):
        return self.wait_until_visibility_of_element_located(By.XPATH, self.BROKEN_IMAGE)


    # Кнопка Click Here for Valid Link в разделе Broken links
    BUTTON_CLICK_HERE_FOR_VALID_LINK = "//a[normalize-space()='Click Here for Valid Link']"
    def get_button_click_here_for_valid_link(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_CLICK_HERE_FOR_VALID_LINK)

    def click_to_button_click_here_for_valid_link(self):
        self.get_button_click_here_for_valid_link().click()
        time.sleep(0.5)

    # Проверка надписи после нажатия кнопки Not Found
    CHECK_IMAGE_SELENIUM_ONLINE_TRAINING = "//img[@alt='Selenium Online Training']"
    def get_incscription_valid_link(self):
        return self.wait_until_visibility_of_element_located(By.XPATH, self.CHECK_IMAGE_SELENIUM_ONLINE_TRAINING)


    # Кнопка Click Here for Broken Link в разделе Broken links
    BUTTON_CLICK_HERE_FOR_BROKEN_LINK = "//a[normalize-space()='Click Here for Broken Link']"
    def get_button_click_here_for_broken_link(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_CLICK_HERE_FOR_BROKEN_LINK)

    def click_to_button_click_here_for_broken_link(self):
        self.get_button_click_here_for_broken_link().click()
        time.sleep(0.5)

    # Проверка статус кода 500 после нажатия кнопки Click Here for Broken Link
    STATUS_CODE_500= "//p[contains(text(),'This page returned a 500 status code.')]"
    def get_incscription_status_code_500(self):
        return self.wait_until_visibility_of_element_located(By.XPATH, self.STATUS_CODE_500)