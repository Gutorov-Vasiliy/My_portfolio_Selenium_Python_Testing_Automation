import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import Base_Page
from utilities.utilites_site import Utils

class Tools_Page_Dynamic_Properties(Base_Page):
    log = Utils.logging_site(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Кнопка Dynamic Properties в разделе Elements
    BUTTON_DYNAMIC_PROPERTIES = "//span[normalize-space()='Dynamic Properties']"

    def get_tab_dynamic_properties(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_DYNAMIC_PROPERTIES)

    def click_to_button_dynamic_properties(self):
        self.get_tab_dynamic_properties().click()
        time.sleep(0.5)


    # Кнопка will_enable_5_seconds в разделе Dynamic Properties
    BUTTON_WILL_ENABLE_5_SECONDS = "//button[@id='enableAfter']"

    def get_button_will_enable_5_seconds(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_WILL_ENABLE_5_SECONDS)

    def click_to_button_will_enable_5_seconds(self):
        self.get_button_will_enable_5_seconds().click()
        time.sleep(0.5)

    # Кнопка Color Change в разделе Dynamic Properties
    BUTTON_COLOR_CHANGE = "//button[@id='enableAfter']"

    def get_button_color_change(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_COLOR_CHANGE)

    def click_to_button_color_change(self):
        self.get_button_color_change().click()
        time.sleep(0.5)

    # Кнопка Visible After 5 Seconds в разделе Dynamic Properties
    BUTTON_VISIBLE_AFTER_5_SECONDS = "//button[@id='visibleAfter']"

    def get_button_visible_after_5_seconds(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_COLOR_CHANGE)

    def click_to_button_visible_after_5_seconds(self):
        self.get_button_visible_after_5_seconds().click()
        time.sleep(0.5)