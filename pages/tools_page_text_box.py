import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import Base_Page
from utilities.utilites_site import Utils


class Tools_Page_Text_Box(Base_Page):
    log = Utils.logging_site(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Кнопка Text Box в разделе Elements
    BUTTON_TEXT_BOX = "//span[normalize-space()='Text Box']"
    def get_tab_text_box (self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TEXT_BOX)

    def click_to_button_tag_text_box(self):
        self.get_tab_text_box().click()
        #time.sleep(0.5)

    # Во вкладке элемент вводим значение в поле Full Name
    FILD_FULL_NAME = "//input[@id='userName']"
    def get_fild_full_name(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILD_FULL_NAME)

    # Во вкладке элемент вводим значение в поле EMAIL
    FILD_EMAIL = "//input[@id='userEmail']"
    def get_email(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILD_EMAIL)

    # Во вкладке элемент вводим значение в поле EMAIL
    CURRENT_ADDRESS = "//textarea[@id='currentAddress']"
    def get_current_address(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CURRENT_ADDRESS)

    # Во вкладке элемент вводим значение в поле EMAIL
    RERMANENT_ADDRESS = "//textarea[@id='permanentAddress']"
    def get_permanent_address(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.RERMANENT_ADDRESS)

    def enter_depart_from_location(self, full_name, email, current_address, permanent_address):


        self.get_fild_full_name().click()
        #time.sleep(0.5)
        self.get_fild_full_name().send_keys(full_name)
        #time.sleep(0.5)
        self.get_email().click()
        #time.sleep(0.5)
        self.get_email().send_keys(email)
        #time.sleep(0.5)
        self.get_current_address().click()
        #time.sleep(0.5)
        self.get_current_address().send_keys(current_address)
        #time.sleep(0.5)
        self.get_permanent_address().click()
        #time.sleep(0.5)
        self.get_permanent_address().send_keys(permanent_address)
        #time.sleep(0.5)

    # Кнопка Submit в разделе Text Box
    BUTTON_SUBMIT = "//button[@id='submit']"

    def get_button_submit(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_SUBMIT)

    def click_to_button_submit(self):
        self.get_button_submit().click()
        #time.sleep(0.5)

    # Строка вывода имени зарегистрированного пользователя
    RESULT_REGISTRATION_NAME ="//p[@id='name']"
    def get_result_registration_name(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_REGISTRATION_NAME)

    # Строка вывода Email зарегистрированного пользователя
    RESULT_REGISTRATION_EMAIL ="//p[@id='email']"
    def get_result_registration_email(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_REGISTRATION_EMAIL)

    # Строка вывода Current_Address зарегистрированного пользователя
    RESULT_REGISTRATION_CURRENT_ADDRESS ="//p[@id='currentAddress']"
    def get_result_registration_current_address(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_REGISTRATION_CURRENT_ADDRESS)

    # Строка вывода Permanent_Address зарегистрированного пользователя
    RESULT_REGISTRATION_PERMANENT_ADDRESS ="//p[@id='permanentAddress']"
    def get_result_registration_permanent_address(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_REGISTRATION_PERMANENT_ADDRESS)
