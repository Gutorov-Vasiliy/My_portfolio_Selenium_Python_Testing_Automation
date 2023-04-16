import logging
import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base_driver import Base_Page
from utilities.utilites_site import Utils

class Tools_Page_Practice_Form(Base_Page):
    log = Utils.logging_site(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Кнопка Forms
    BUTTON_DYNAMIC_FORMS = "//div[normalize-space()='Forms']//span"

    def get_tab_dynamic_forms(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_DYNAMIC_FORMS)

    def click_to_tab_dynamic_forms(self):
        self.get_tab_dynamic_forms().click()
        #time.sleep(1)

    # Кнопка Practice Form в разделе Forms
    BUTTON_DYNAMIC_PRACTICE_FORM = "//span[normalize-space()='Practice Form']"

    def get_button_practice_form(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_DYNAMIC_PRACTICE_FORM)

    def click_to_button_practice_form(self):
        self.get_button_practice_form().click()
        #time.sleep(1)


    # Поле firstName в разделе Practice Form
    BUTTON_FIRST_NAME = "//input[@id='firstName']"

    def get_button_first_name(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_FIRST_NAME)

    def click_to_button_first_name(self, first_name):
        self.get_button_first_name().send_keys(first_name)
        #time.sleep(1)


    # Поле lastName в разделе Practice Form
    BUTTON_LAST_NAME = "//input[@id='lastName']"

    def get_button_last_name(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_LAST_NAME)

    def click_to_button_last_name(self, last_name):
        self.get_button_last_name().send_keys(last_name)
        #time.sleep(1)


    # Поле userEmail в разделе Practice Form
    BUTTON_USER_MAIL = "//input[@id='userEmail']"

    def get_button_user_email(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_USER_MAIL)

    def click_to_button_user_mail(self, user_mail):
        self.get_button_user_email().send_keys(user_mail)
        #time.sleep(1)


    # Кнопка MALE в разделе Practice Form
    BUTTON_MALE = "//label[@for='gender-radio-1']"

    def get_button_male(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_MALE)

    def click_to_button_male(self):
        self.get_button_male().click()
        #time.sleep(0.5)

    # Кнопка FEMALE в разделе Practice Form
    BUTTON_FEMALE = "//input[@id='gender-radio-2']"

    def get_button_female(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_MALE)

    def click_to_button_female(self):
        self.get_button_female().click()
        #time.sleep(0.5)

    # Кнопка OTHER в разделе Practice Form
    BUTTON_OTHER = "//input[@id='gender-radio-3'][@value='Other']"

    def get_button_other(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_OTHER)

    def click_to_button_other(self):
        self.get_button_other().click()
        #time.sleep(0.5)

    # Строка number_phone в разделе Practice Form
    BUTTON_USER_NUMBER = "//input[@id='userNumber']"

    def get_string_number_phone(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_USER_NUMBER)

    def click_to_button_user_number(self, user_number):
        self.get_string_number_phone().send_keys(user_number)
        #time.sleep(0.5)


    # Кнопка DATE_OF_BIRTH в разделе Practice Form
    BUTTON_DATE_OF_BIRTH_INPUT = "//input[@id='dateOfBirthInput']"

    def get_button_date_of_birth_input(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_DATE_OF_BIRTH_INPUT)

    def click_to_date_of_birth_input(self):
        self.get_button_date_of_birth_input().click()
        #time.sleep(0.5)

    # Select Month в разделе Practice Form
    BUTTON_MONTH_SELECT = "//select[@class='react-datepicker__month-select']"

    def get_button_month_select(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_MONTH_SELECT)

    def click_to_month_select(self, month):
        dd_multi_month = Select(self.get_button_month_select())
        dd_multi_month.select_by_visible_text(month)
        #time.sleep(0.5)

    # Select Year в разделе Practice Form
    BUTTON_YEAR_SELECT = "//select[@class='react-datepicker__year-select']"

    def get_button_year_select(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_YEAR_SELECT)



    def click_to_year_select(self, year):
        dd_multi = Select(self.get_button_year_select())
        dd_multi.select_by_visible_text(year)
        #time.sleep(1)

    # Клик в пустое место
    CLICK_TO_CLEAR_PLACE = "//div[@class='main-header']"

    def click_to_clear_place(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CLICK_TO_CLEAR_PLACE)

    # Выбор для из календаря в разделе Practice Form
    ALL_DATE = "//div[@role='listbox']//div[contains(text(),'')]"
    def get_input_date(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATE)

    def enter_departure_date(self, departure_date):
        all_dates = self.get_input_date().find_elements(By.XPATH, self.ALL_DATE)
        #time.sleep(0.5)
        for date in all_dates:
            if date.get_attribute("aria-label") == departure_date:
                #time.sleep(0.5)
                date.click()
                break
        self.click_to_clear_place().click()
        #time.sleep(1)


    # Поле Subjects в разделе Practice Form
    BUTTON_SUBJECTS = "//input[@id='subjectsInput']"

    def get_button_subjects(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_SUBJECTS)

    def click_to_subjects(self, subjects):
        self.get_button_subjects().click()
        self.get_button_subjects().send_keys(subjects)
        self.get_button_subjects().send_keys(Keys.ENTER)
        #time.sleep(1)

    # Кнопка Sports в разделе Practice Form
    BUTTON_SPORTS = "// label[@for ='hobbies-checkbox-1']"

    def get_button_sports(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_SPORTS)

    def click_to_sports(self):
        self.get_button_sports().click()
        #time.sleep(1)


    # Кнопка Reading в разделе Practice Form
    BUTTON_READING = "//label[@for='hobbies-checkbox-2']"

    def get_button_reading(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_READING)

    def click_to_button_reading(self):
        self.get_button_reading().click()
        #time.sleep(1)


    # Кнопка Music в разделе Practice Form
    BUTTON_MUSIC = "//label[@for='hobbies-checkbox-3']"

    def get_button_music(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_MUSIC)

    def click_to_button_music(self):
        self.get_button_music().click()
        #time.sleep(1)


    # Кнопка Select picture в разделе Web Tables
    BUTTON_SELECT_A_FILE = "//input[@class='form-control-file']"

    def get_button_select_picture(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_SELECT_A_FILE)

    def click_to_button_select_a_file(self):
        self.get_button_select_picture().send_keys("C:\\Users\\user\\PycharmProjects\\Test_Site\\testdata\\photo.jpeg")
        #time.sleep(0.5)



    # Поле Current Address в разделе Practice Form
    BUTTON_CURRENT_ADDRESS = "//textarea[@id='currentAddress']"

    def get_button_current_address(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_CURRENT_ADDRESS)

    def click_to_current_address(self, current_address):
        self.get_button_current_address().click()
        #time.sleep(0.5)
        self.get_button_current_address().send_keys(current_address)
        #time.sleep(0.5)


    # Размер окна в разделе Practice Form
    BUTTON_WINDOW_CURRENT_ADDRESS = "//textarea[@id='currentAddress']"

    def get_button_window_current_address(self):
        return self.wait_until_visibility_of_element_located(By.XPATH, self.BUTTON_WINDOW_CURRENT_ADDRESS)

    def click_to_window_current_address(self, xoffset, yoffset, xoffset_x, xoffset_y, source=None):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_button_window_current_address())
        time.sleep(1)
        move_mouse = actions.move_by_offset(xoffset, yoffset)
        time.sleep(1)
        move_mouse.drag_and_drop_by_offset(source, xoffset_x, xoffset_y)
        time.sleep(1)











