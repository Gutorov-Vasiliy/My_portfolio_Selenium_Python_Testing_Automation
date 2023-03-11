import logging
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_driver import Base_Page
from utilities.utilites_site import Utils


class Tools_Page_Web_Tables(Base_Page):
    log = Utils.logging_site(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Кнопка add New Record в разделе Web Tables
    BUTTON_WEB_TABLES = "//span[normalize-space()='Web Tables']"

    def get_button_tab_web_tables(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_WEB_TABLES)

    def click_to_button_tab_web_tables(self):
        self.get_button_tab_web_tables().click()
        #time.sleep(0.5)


    # Кнопка add New Record в разделе Web Tables
    BUTTON_ADD_NEW_RECORD = "//button[@id='addNewRecordButton']"

    def get_button_add_new_record(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_ADD_NEW_RECORD)

    def click_to_button_add_new_record(self):
        self.get_button_add_new_record().click()
        #time.sleep(0.5)

    # Строка поиска по таблице
    STRING_SEARCH_IN_TABLE = "//input[@id='searchBox']"

    def get_string_search_in_table(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.STRING_SEARCH_IN_TABLE)

    def click_and_writing_in_string_in_table(self, search_in_table):
        self.get_string_search_in_table().click()
        #time.sleep(0.5)
        self.get_string_search_in_table().send_keys(search_in_table)
        #time.sleep(0.5)

    # Кнопка поиск input-group-append результатов
    BUTTON_SEARCH_RESULTS = "//div[@class='input-group-append']"

    def get_button_search_results(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_SEARCH_RESULTS)

    def click_to_button_search_results(self):
        self.get_button_search_results().click()
        #time.sleep(0.5)


    # Кнопка инзменения информации профиля сотрудника
    BUTTON_EDIT_RECORD_BY_NAME = "//div[@class='rt-tr-group']"
    def get_button_edit_by_name(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_EDIT_RECORD_BY_NAME)

    # Кнопка инзменения информации профиля сотрудника
    BUTTON_EDIT_RECORD = "//span[@title='Edit']"
    def get_button_edit(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_EDIT_RECORD)

    def click_to_button_edit(self, check_button_no, plase_in_table):
        buttons_edit = self.get_button_edit_by_name().find_elements(By.XPATH, self.BUTTON_EDIT_RECORD_BY_NAME)
        edits = self.get_button_edit().find_elements(By.XPATH, self.BUTTON_EDIT_RECORD)
        for button in buttons_edit:
            if button.text == check_button_no:
                for edit in edits:
                    if edit.get_attribute("id") == plase_in_table:
                        edit.click()
                    print(button.text, edit.text)
        #time.sleep(0.5)


    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    def get_going_to_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)
    def get_going_to_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

    def enter_going_to_location(self, going_to_location):
        self.get_going_to_field().click()
        self.log.info("Clicked on going to")
        #time.sleep(1.5)
        self.get_going_to_field().send_keys(going_to_location)
        self.log.info("Typed test into going to field successfully")
        #time.sleep(1.5)
        search_results = self.get_going_to_results()
        for results in search_results:
            if going_to_location in results.text:
                results.click()
                break