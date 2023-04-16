import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import Base_Page
from utilities.utilites_site import Utils
from selenium.webdriver import ActionChains

class Tools_Page_Browser_Windows(Base_Page):
    log = Utils.logging_site(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Тег Alerts, Frame & Windows
    BUTTON_ALERTS_FRAME_WINDOWS = "//div[normalize-space()='Alerts, Frame & Windows']"
    def get_button_alerts_frame_windows(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_ALERTS_FRAME_WINDOWS)

    # Кнопка new_tab в разделе Browser Windows
    def click_to_button_alerts_frame_windows(self):
        self.get_button_alerts_frame_windows().click()
        time.sleep(0.5)


    # Кнопка Browser Windows в разделе Alerts, Frame & Windows
    BUTTON_BROWSER_WINDOWS = "//span[normalize-space()='Browser Windows']"
    def get_button_browser_windows(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_BROWSER_WINDOWS)

    # Кнопка new_tab в разделе Browser Windows
    def click_to_button_browser_windows(self):
        self.get_button_browser_windows().click()
        time.sleep(0.5)


    # Кнопка Buttons в разделе Elements
    BUTTON_NEW_TAB = "//button[@id='tabButton']"
    def get_button_new_tab(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_NEW_TAB)

    # Кнопка Buttons в разделе Elements
    TEXT_NEW_TAB = "(//h1[normalize-space()='This is a sample page'])"
    def get_text_button_new_tab(self):
        return self.wait_until_visibility_of_element_located(By.XPATH, self.TEXT_NEW_TAB)

    # Кнопка new_tab в разделе Browser Windows
    def click_to_button_new_tab(self, window_1, window_2):
        self.get_button_new_tab().click()
        #time.sleep(0.5)
        self.switch_to_window(window_1)
        #time.sleep(0.5)
        self.get_text_button_new_tab()
        #time.sleep(0.5)
        self.switch_to_window(window_2)
        #time.sleep(0.5)


    # Кнопка New Window в разделе Elements
    BUTTON_NEW_WINDOW = "//button[@id='windowButton']"
    def get_button_new_window(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_NEW_WINDOW)

    # Текст New Window в разделе Elements
    TEXT_NEW_WINDOW = "//h1[@id='sampleHeading']"
    def get_text_button_new_window(self):
        return self.wait_until_visibility_of_element_located(By.XPATH, self.TEXT_NEW_WINDOW)

    # Ссылка на новое окно
    def get_link_new_window(self):
        link_new = "https://demoqa.com/sample"
        return link_new

    # Ссылка на новое окно
    def get_link_old_window(self):
        link_old = "https://demoqa.com/browser-windows"
        return link_old

    # Кнопка new_window в разделе Browser Windows
    def click_to_button_new_window(self, old_window):
        self.get_button_new_window().click()
        time.sleep(5)
        self.driver.switch_to.new_window("window")
        time.sleep(5)
        self.driver.get(self.get_link_new_window)
        time.sleep(5)
        self.get_text_button_new_window()
        time.sleep(5)
        self.switch_to_window(old_window)
        time.sleep(5)











