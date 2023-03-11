import logging
import time
from selenium.webdriver.common.by import By

from base.base_driver import Base_Page
from utilities.utilites_site import Utils


class Launch_Page(Base_Page):
    log = Utils.logging_site(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Кнопка TOOLS QA в шапке главной(загрузочной) странице сайта
    BUTTON_TOOLS_QA = "// img[ @ src = '/images/Toolsqa.jpg']"
    def get_button_tools_qa(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TOOLS_QA)

    def click_to_button_tools_qa(self):
        self.get_button_tools_qa().click()
        #time.sleep(0.5)

    # Кнопка Selenuim Certification Training  в шапке главной(загрузочной) странице сайта
    BUTTON_SELENIUM_CERTIFICATION_TRAINING = "//img[@src='/images/Toolsqa.jpg']"

    def get_button_selenuim_certification_training(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_SELENIUM_CERTIFICATION_TRAINING)

    def click_to_button_selenuim_certification_training(self):
        self.get_button_tools_qa().click()
        #time.sleep(0.5)

    # Кнопка Elements на главной(загрузочной) странице сайта
    BUTTON_ELEMENTS = "//h5[normalize-space()='Elements']"

    def get_button_elements(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_ELEMENTS)

    def click_to_button_elements(self):
        self.get_button_elements().click()
        #time.sleep(0.5)

    # Кнопка Forms на главной(загрузочной) странице сайта
    BUTTON_FORMS = "//h5[normalize-space()='Forms']"

    def get_button_forms(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_FORMS)

    def click_to_button_forms(self):
        self.get_button_forms().click()
        #time.sleep(0.5)



    # Кнопка Alerts, Frame & Windows на главной(загрузочной) странице сайта
    BUTTON_ALERTS_FRAME_AND_WINDOWS = "//h5[normalize-space()='Alerts, Frame & Windows']"

    def get_button_alerts_frame_and_windows(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_ALERTS_FRAME_AND_WINDOWS)

    def click_to_button_alerts_frame_and_windows(self):
        self.get_button_alerts_frame_and_windows().click()
        #time.sleep(0.5)


    # Кнопка WIDGETS на главной(загрузочной) странице сайта
    BUTTON_WIDGETS = "//h5[normalize-space()='Widgets']"

    def get_button_widgets(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_WIDGETS)

    def click_to_button_widgets(self):
        self.get_button_widgets().click()
        #time.sleep(0.5)


    # Кнопка Interactions на главной(загрузочной) странице сайта
    BUTTON_INTERACTIONS = "//h5[normalize-space()='Interactions']"

    def get_button_interactions(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_INTERACTIONS)

    def click_to_button_interactions(self):
        self.get_button_interactions().click()
        #time.sleep(0.5)


    # Кнопка Book Store Application на главной(загрузочной) странице сайта
    BUTTON_BOOK_STORE_APPLICATION = "//h5[normalize-space()='Book Store Application']"

    def get_button_book_store_application(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_BOOK_STORE_APPLICATION)

    def click_to_button_book_store_application(self):
        self.get_button_book_store_application().click()
        #time.sleep(0.5)