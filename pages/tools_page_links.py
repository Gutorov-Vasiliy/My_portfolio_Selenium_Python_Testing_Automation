import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import Base_Page
from utilities.utilites_site import Utils

class Tools_Page_Links(Base_Page):
    log = Utils.logging_site(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Кнопка Links в разделе Elements
    BUTTON_TAB_LINKS = "//span[normalize-space()='Links']"
    def get_tab_links(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TAB_LINKS)
    def click_to_button_links(self):
        self.get_tab_links().click()
        time.sleep(0.5)

    # Кнопка Home в разделе Links
    BUTTON_HOME = "//a[@id='simpleLink']"
    def get_button_home(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_HOME)
    def click_to_button_home(self):
        self.get_button_home().click()
        time.sleep(0.5)

    # Кнопка Home9Cbfw в разделе Links
    BUTTON_HOME9Cbfw = "//a[@id='dynamicLink']"
    def get_button_home9Cbfw(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_HOME9Cbfw)
    def click_to_button_home9Cbfw(self):
        self.get_button_home9Cbfw().click()
        time.sleep(0.5)

    # Кнопка Created в разделе Links
    BUTTON_CREATED = "//a[@id='created']"
    def get_button_created(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_CREATED)
    def click_to_button_created(self):
        self.get_button_created().click()
        time.sleep(0.5)

    # Проверка надписи после нажатия кнопки Created
    INCSCRIPTION_CHECK_CREATED  = "//b[contains(text(),'201') or contains(text(),'Created')]"
    def get_incscription_created(self):
        return self.wait_until_visibility_of_element_located(By.XPATH, self.INCSCRIPTION_CHECK_CREATED)


    # Кнопка No Created в разделе Links
    BUTTON_NO_CONTENT = "//a[@id='no-content']"
    def get_button_no_content(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_NO_CONTENT)
    def click_to_button_no_content(self):
        self.get_button_no_content().click()
        time.sleep(0.5)

    # Проверка надписи после нажатия кнопки No Created
    INCSCRIPTION_CHECK_NO_CONTENT = "//b[contains(text(),'204') or contains(text(),'No Content')]"
    def get_incscription_no_content(self):
        return self.wait_until_visibility_of_element_located(By.XPATH, self.INCSCRIPTION_CHECK_NO_CONTENT)

    # Кнопка Moved в разделе Links
    BUTTON_MOVED = "//a[@id='moved']"
    def get_button_moved(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_MOVED)
    def click_to_button_moved(self):
        self.get_button_moved().click()
        time.sleep(0.5)

    # Проверка надписи после нажатия кнопки Moved Permanently
    INCSCRIPTION_CHECK_MOVED = "//b[contains(text(),'301') or contains(text(),'Moved Permanently')]"
    def get_incscription_moved(self):
        return self.wait_until_visibility_of_element_located(By.XPATH, self.INCSCRIPTION_CHECK_MOVED)


    # Кнопка Bad request в разделе Links
    BUTTON_BAD_REQUEST = "//a[@id='bad-request']"
    def get_button_bad_request(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_BAD_REQUEST)
    def click_to_button_bad_request(self):
        self.get_button_bad_request().click()
        time.sleep(0.5)

    # Проверка надписи после нажатия кнопки Bad request
    INCSCRIPTION_CHECK_BAD_REQUEST = "//b[contains(text(),'400') or contains(text(),'Bad Request')]"
    def get_incscription_bad_request(self):
        return self.wait_until_visibility_of_element_located(By.XPATH, self.INCSCRIPTION_CHECK_BAD_REQUEST)


    # Кнопка Unauthorized в разделе Links
    BUTTON_UNAURHORIZED = "//a[@id='unauthorized']"
    def get_button_unauthorized(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_UNAURHORIZED)
    def click_to_button_unauthorized(self):
        self.get_button_unauthorized().click()
        time.sleep(0.5)

    # Проверка надписи после нажатия кнопки Unauthorized
    INCSCRIPTION_CHECK_UNAURHORIZED = "//b[contains(text(),'401') or contains(text(),'Unauthorized')]"
    def get_incscription_unauthorized(self):
        return self.wait_until_visibility_of_element_located(By.XPATH, self.INCSCRIPTION_CHECK_UNAURHORIZED)

    # Кнопка Forbidden в разделе Links
    BUTTON_FORBIDDEN = "//a[@id='forbidden']"
    def get_button_forbidden(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_FORBIDDEN)
    def click_to_button_forbidden(self):
        self.get_button_forbidden().click()
        time.sleep(0.5)

    # Проверка надписи после нажатия кнопки Unauthorized
    INCSCRIPTION_CHECK_FORBIDDEN = "//b[contains(text(),'403') or contains(text(),'Forbidden')]"
    def get_incscription_forbidden(self):
        return self.wait_until_visibility_of_element_located(By.XPATH, self.INCSCRIPTION_CHECK_FORBIDDEN)


    # Кнопка Not Found в разделе Links
    BUTTON_NOT_FOUND = "//a[@id='invalid-url']"
    def get_button_not_found(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_NOT_FOUND)
    def click_to_button_not_found(self):
        self.get_button_not_found().click()
        time.sleep(0.5)

    # Проверка надписи после нажатия кнопки Not Found
    INCSCRIPTION_CHECK_NOT_FOUND = "//b[contains(text(),'404') or contains(text(),'Not Found')]"
    def get_incscription_not_found(self):
        return self.wait_until_visibility_of_element_located(By.XPATH, self.INCSCRIPTION_CHECK_NOT_FOUND)

