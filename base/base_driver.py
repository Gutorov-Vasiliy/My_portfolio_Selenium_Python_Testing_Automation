import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class Base_Page():
    def __init__(self, driver):
        self.driver = driver


    # Перелиствание (скролл) станицы веб сайт до самого низа
    def scroll_page_to_down_page(self):
        time.sleep(0.5)
        last_height = self.driver.execute_script\
            ("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        while True:
            time.sleep(0.5)
            self.driver.execute_script \
                ("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
            new_height = self.driver.execute_script\
                ("return document.body.scrollHeight")
            time.sleep(0.5)
            if new_height == last_height:
                break
            last_height = new_height

    def switching_between_browser_tabs(self, window):
        time.sleep(0.5)
        return self.driver.switch_to.window(self.driver.window_handles[window])


    def scroll_to_element(self, button):
        actions = ActionChains(self.driver)
        elements = self.wait_until_visibility_of_element_located(By.XPATH, button)
        actions.move_to_element(elements).perform()
        time.sleep(0.5)


    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements


    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_until_visibility_of_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element_located = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return element_located

    def wait_until_text_to_be_present_in_element_valuee(self, locator_type, locator, text_):
        wait = WebDriverWait(self.driver, 20)
        text_in_element = wait.until(EC.text_to_be_present_in_element_value((locator_type, locator), text_))
        return text_in_element


    def wait_until_invisibility_of_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        element_invisibility = wait.until(EC.invisibility_of_element_located((locator_type, locator)))
        return element_invisibility


    def write_file_from_pc(self,locator_type, locator, path):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator))).send_keys(path)
        return element

    def switch_to_window(self, window):
        all_window = self.driver.switch_to.window(self.driver.window_handles[window])
        return all_window

