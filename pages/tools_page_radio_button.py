import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import Base_Page
from utilities.utilites_site import Utils

class Tools_Page_RADIO_BUTTON(Base_Page):
    log = Utils.logging_site(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Кнопка Radio Button в разделе Elements
    BUTTON_RADIO_BUTTON = "//span[normalize-space()='Radio Button']"
    def get_tab_radio_button (self):
        #time.sleep(0.5)
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_RADIO_BUTTON)

    def click_to_button_tag_radio_button(self):
        self.get_tab_radio_button().click()
        #time.sleep(0.5)

    # Кнопка Yes в разделе Radio Button
    BUTTON_YES = "//label[@for='yesRadio']"
    def get_button_yes (self):
        #time.sleep(0.5)
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_YES)

    def click_to_button_yes(self):
        self.get_button_yes().click()
        #time.sleep(0.5)

    # Кнопка Impressive в разделе Radio Button
    BUTTON_IMPRESSIVE = "//label[@for='impressiveRadio']"
    def get_button_impressive (self):
        #time.sleep(0.5)
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_IMPRESSIVE)

    def click_to_button_impressive(self):
        self.get_button_impressive().click()
        #time.sleep(0.5)

    # Кнопка No в разделе Radio Button
    BUTTON_NO = "//div[@class='custom-control disabled custom-radio custom-control-inline']"
    def get_button_no(self):
        #time.sleep(0.5)
        return self.wait_until_visibility_of_element_located(By.XPATH, self.BUTTON_NO)

    def check_button_for_non_clickability(self, check_button_no):
        button_no = self.get_button_no().find_elements(By.XPATH, self.BUTTON_NO)
        for button in button_no:
            if button.get_attribute("class") == check_button_no:
                pass
        #time.sleep(0.5)


    # Проверка строки на значение Yes
    CHECK_STRING_YES = "//span[contains(text(),'Yes')]"
    def get_check_string_yes (self):
        #time.sleep(0.5)
        return self.wait_until_visibility_of_element_located(By.XPATH, self.CHECK_STRING_YES)

    # Проверка строки на значение Impressive
    CHECK_STRING_IMPRESSIVE = "//span[contains(text(),'Impressive')]"
    def get_check_string_impressive (self):
        #time.sleep(0.5)
        return self.wait_until_visibility_of_element_located(By.XPATH, self.CHECK_STRING_IMPRESSIVE)