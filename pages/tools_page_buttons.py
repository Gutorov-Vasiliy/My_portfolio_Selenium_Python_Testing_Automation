import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import Base_Page
from utilities.utilites_site import Utils
from selenium.webdriver import ActionChains

class Tools_Page_Buttons(Base_Page):
    log = Utils.logging_site(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Кнопка Buttons в разделе Elements
    BUTTON_BUTTONS = "//span[normalize-space()='Buttons']"
    def get_tab_buttons(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_BUTTONS)

    def click_to_button_tag_buttons(self):
        self.get_tab_buttons().click()
        time.sleep(3)


    # Кнопка Double click me в разделе Buttons
    BUTTON_CHECK_DOUBLE_CLICK = "//button[@id='doubleClickBtn']"
    def get_button_double_click(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_CHECK_DOUBLE_CLICK)

    def click_to_button_double_click(self):
        achains = ActionChains(self.driver)
        achains.double_click(self.get_button_double_click()).perform()
        time.sleep(0.5)

    # Проверка вывода текста после нажатии кнопку double click me
    RESULT_AFTER_CLICK_BUTTON_DOUBLE_CLICK_ME = "//p[@id='doubleClickMessage']"

    def get_result_after_button_double_click_me(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_AFTER_CLICK_BUTTON_DOUBLE_CLICK_ME)


    # Кнопка Right click me в разделе Buttons
    BUTTON_CHECK_RIGHT_CLICK = "//button[@id='rightClickBtn']"
    def get_button_right_click(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_CHECK_RIGHT_CLICK)

    def click_to_button_right_click(self):
        achains = ActionChains(self.driver)
        achains.context_click(self.get_button_right_click()).perform()
        time.sleep(0.5)

    # Проверка вывода текста после нажатии кнопку right click me
    RESULT_AFTER_CLICK_BUTTON_RIGHT_CLICK_ME = "//p[@id='rightClickMessage']"

    def get_result_after_button_right_click_me(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_AFTER_CLICK_BUTTON_RIGHT_CLICK_ME)


    # Кнопка Click me в разделе Buttons
    BUTTON_CLICK_ME = "(//button[normalize-space()='Click Me'])"
    def get_button_click_me(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_CLICK_ME)

    def click_to_button_click_me(self):
        self.get_button_click_me().click()
        time.sleep(0.5)

    # Проверка вывода текста после нажатии кнопку right click me
    RESULT_AFTER_CLICK_BUTTON_CLICK_ME = "//p[@id='dynamicClickMessage']"

    def get_result_after_button_click_me(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_AFTER_CLICK_BUTTON_CLICK_ME)
