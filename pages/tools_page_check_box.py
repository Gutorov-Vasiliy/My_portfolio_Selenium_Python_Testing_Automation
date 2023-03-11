import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import Base_Page
from utilities.utilites_site import Utils


class Tools_Page_Check_Box(Base_Page):
    log = Utils.logging_site(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Кнопка Check Box в разделе Elements
    BUTTON_CHECK_BOX = "//span[normalize-space()='Check Box']"

    def get_tab_check_box(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_CHECK_BOX)

    def click_to_button_tag_text_box(self):
        self.get_tab_check_box().click()
        #time.sleep(0.5)


    # Стрелочка Home в Check Box в разделе Elements
    BUTTON_TEXT_BOX = "//button[@title='Toggle']"
    def get_button_arrow_home (self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TEXT_BOX)

    def click_to_button_arrow_home(self):
        self.get_button_arrow_home().click()
        #time.sleep(0.5)

    # Узел Home в Check Box в разделе Elements
    BUTTON_TICK_HOME = "//span[@class='rct-checkbox']//*[name()='svg']"

    def get_button_tick_home(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME)

    def click_to_button_tick_home(self):
        self.get_button_tick_home().click()
        #time.sleep(0.5)


    #Стрелочка в Desktop в Home в Check box
    BUTTON_TICK_HOME_DESKTOP = "//li[@class='rct-node rct-node-parent rct-node-expanded']//li[1]//span[1]//button[1]"

    def get_button_tick_home_desktop(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DESKTOP)

    def click_to_button_tick_home_desktop(self):
        self.get_button_tick_home_desktop().click()
        #time.sleep(0.5)

    #Утел Notes в Desktop в Home
    BUTTON_TICK_HOME_DESKTOP_NOTES = "//label[@for='tree-node-notes']"

    def get_button_tick_home_desktop_notes(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DESKTOP_NOTES)

    def click_to_button_tick_home_desktop_notes(self):
        self.get_button_tick_home_desktop_notes().click()
        #time.sleep(0.5)

    # Утел Commands в Desktop в Home
    BUTTON_TICK_HOME_DESKTOP_COMMENDS = "//label[@for='tree-node-commands']"

    def get_button_tick_home_desktop_commands(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DESKTOP_COMMENDS)

    def click_to_button_tick_home_desktop_commands(self):
        self.get_button_tick_home_desktop_commands().click()
        #time.sleep(0.5)

    # Стрелочка Documents в Home
    BUTTON_TICK_HOME_DOCUMENTS = "//li[2]//span[1]//button[1]"

    def get_button_tick_home_documents(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DOCUMENTS)

    def click_to_button_tick_home_documents(self):
        self.get_button_tick_home_documents().click()
        #time.sleep(0.5)

    # Стрелочка Documents в Home
    BUTTON_TICK_HOME_DOCUMENTS_WORK_SPACE = "//body//div[@id='app']//li[@class='rct-node rct-node-parent rct-node-expanded']//li[@class='rct-node rct-node-parent rct-node-expanded']//li[1]//span[1]//button[1]"

    def get_button_tick_home_documents_work_space(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DOCUMENTS_WORK_SPACE)

    def click_to_button_tick_home_documents_work_space(self):
        self.get_button_tick_home_documents_work_space().click()
        #time.sleep(0.5)

    # Узел React в Work_Spece в Documents в Home
    BUTTON_TICK_HOME_DOCUMENTS_WORK_SPACE_REACT = "//label[@for='tree-node-react']"

    def get_button_tick_home_documents_work_space_react(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DOCUMENTS_WORK_SPACE_REACT)

    def click_to_button_tick_home_documents_work_space_react(self):
        self.get_button_tick_home_documents_work_space_react().click()
        #time.sleep(0.5)

    # Узел Angular в Work_Spece в Documents в Home
    BUTTON_TICK_HOME_DOCUMENTS_WORK_SPACE_ANGULAR = "//label[@for='tree-node-angular']"

    def get_button_tick_home_documents_work_space_angular(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DOCUMENTS_WORK_SPACE_ANGULAR)

    def click_to_button_tick_home_documents_work_space_angular(self):
        self.get_button_tick_home_documents_work_space_angular().click()
        #time.sleep(0.5)

    # Узел Veu в Work_Spece в Documents в Home
    BUTTON_TICK_HOME_DOCUMENTS_WORK_SPACE_VEU = "//label[@for='tree-node-veu']"

    def get_button_tick_home_documents_work_space_veu(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DOCUMENTS_WORK_SPACE_VEU)

    def click_to_button_tick_home_documents_work_space_veu(self):
        self.get_button_tick_home_documents_work_space_veu().click()
        #time.sleep(0.5)

    # Стрелочка Documents в Home
    BUTTON_TICK_HOME_DOCUMENTS_OFFICE = "//body//div[@id='app']//li[@class='rct-node rct-node-parent rct-node-expanded']//li[@class='rct-node rct-node-parent rct-node-expanded']//li[2]//span[1]//button[1]"

    def get_button_tick_home_documents_office(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DOCUMENTS_OFFICE)

    def click_to_button_tick_home_documents_office(self):
        self.get_button_tick_home_documents_office().click()
        #time.sleep(0.5)


    # Узел Public в Office в Documents в Home
    BUTTON_TICK_HOME_DOCUMENTS_OFFICE_PUBLIC = "//label[@for='tree-node-public']"

    def get_button_tick_home_documents_office_public(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DOCUMENTS_OFFICE_PUBLIC)

    def click_to_button_tick_home_documents_office_public(self):
        self.get_button_tick_home_documents_office_public().click()
        #time.sleep(0.5)

    # Узел Private в Office в Documents в Home
    BUTTON_TICK_HOME_DOCUMENTS_OFFICE_PRIVATE = "//label[@for='tree-node-private']"

    def get_button_tick_home_documents_office_private(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DOCUMENTS_OFFICE_PRIVATE)

    def click_to_button_tick_home_documents_office_private(self):
        self.get_button_tick_home_documents_office_private().click()
        #time.sleep(0.5)

    # Узел Classified в Office в Documents в Home
    BUTTON_TICK_HOME_DOCUMENTS_OFFICE_CLASSIFIED = "//label[@for='tree-node-classified']"

    def get_button_tick_home_documents_office_classified(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DOCUMENTS_OFFICE_CLASSIFIED)

    def click_to_button_tick_home_documents_office_classified(self):
        self.get_button_tick_home_documents_office_classified().click()
        #time.sleep(0.5)

    # Узел General в Office в Documents в Home
    BUTTON_TICK_HOME_DOCUMENTS_OFFICE_GENERAL = "//label[@for='tree-node-general']"

    def get_button_tick_home_documents_office_general(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DOCUMENTS_OFFICE_GENERAL)

    def click_to_button_tick_home_documents_office_general(self):
        self.get_button_tick_home_documents_office_general().click()
        #time.sleep(0.5)


    # Стрелочка Downloades в Home
    BUTTON_TICK_HOME_DOWNLOADES = "//li[3]//span[1]//button[1]"

    def get_button_tick_home_downloades(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DOWNLOADES)

    def click_to_button_tick_home_downloades(self):
        self.get_button_tick_home_downloades().click()
        #time.sleep(0.5)

    # Узел Word File.doc Downloades в Home
    BUTTON_TICK_HOME_DOWNLOADES_WORD_FILE = "//label[@for='tree-node-wordFile']"

    def get_button_tick_home_downloades_word_file(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DOWNLOADES_WORD_FILE)

    def click_to_button_tick_home_downloades_word_file(self):
        self.get_button_tick_home_downloades_word_file().click()
        #time.sleep(0.5)

    # Узел Word File.doc Downloades в Home
    BUTTON_TICK_HOME_DOWNLOADES_EXCEL_FILE = "//label[@for='tree-node-excelFile']"

    def get_button_tick_home_downloades_excel_file(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_TICK_HOME_DOWNLOADES_EXCEL_FILE)

    def click_to_button_tick_home_downloades_excel_file(self):
        self.get_button_tick_home_downloades_excel_file().click()
        #time.sleep(0.5)

    # Строка вывода home нажатой галочки
    RESULT_TICK_HOME ="//span[normalize-space()='home']"
    def get_result_tick_home(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_HOME)

    # Строка вывода desktop нажатой галочки
    RESULT_TICK_DESKTOP ="//span[normalize-space()='desktop']"
    def get_result_tick_desktop(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_DESKTOP)

    # Строка вывода notes нажатой галочки
    RESULT_TICK_NOTES ="//span[normalize-space()='notes']"
    def get_result_tick_notes(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_NOTES)

    # Строка вывода commands нажатой галочки
    RESULT_TICK_COMMANDS ="//span[normalize-space()='commands']"
    def get_result_tick_commands(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_COMMANDS)

    # Строка вывода documents нажатой галочки
    RESULT_TICK_DOCUMENTS ="//span[normalize-space()='documents']"
    def get_result_tick_documents(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_DOCUMENTS)

    # Строка вывода workspace нажатой галочки
    RESULT_TICK_WORKSPACE ="//span[normalize-space()='workspace']"
    def get_result_tick_workspace(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_WORKSPACE)

    # Строка вывода react нажатой галочки
    RESULT_TICK_REACT ="//span[normalize-space()='react']"
    def get_result_tick_react(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_REACT)

    # Строка вывода angular нажатой галочки
    RESULT_TICK_ANGULAR ="//span[normalize-space()='angular']"
    def get_result_tick_angular(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_ANGULAR)

    # Строка вывода veu нажатой галочки
    RESULT_TICK_VEU ="//span[normalize-space()='veu']"
    def get_result_tick_veu(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_VEU)

    # Строка вывода office нажатой галочки
    RESULT_TICK_OFFICE ="//span[normalize-space()='office']"
    def get_result_tick_office(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_OFFICE)

    # Строка вывода public нажатой галочки
    RESULT_TICK_PUBLIC ="//span[normalize-space()='public']"
    def get_result_tick_public(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_PUBLIC)

    # Строка вывода private нажатой галочки
    RESULT_TICK_PRIVATE ="//span[normalize-space()='private']"
    def get_result_tick_private(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_PRIVATE)

    # Строка вывода classified нажатой галочки
    RESULT_TICK_CLASSIFIED ="//span[normalize-space()='classified']"
    def get_result_tick_classified(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_CLASSIFIED)

    # Строка вывода general нажатой галочки
    RESULT_TICK_GENERAL ="//span[normalize-space()='general']"
    def get_result_tick_general(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_GENERAL)

    # Строка вывода downloads нажатой галочки
    RESULT_TICK_DOWNLOADS ="//span[normalize-space()='downloads']"
    def get_result_tick_downloads(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_DOWNLOADS)

    # Строка вывода wordFile нажатой галочки
    RESULT_TICK_WORD_FILE ="//span[normalize-space()='wordFile']"
    def get_result_tick_word_file(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_WORD_FILE)

    # Строка вывода excelFile нажатой галочки
    RESULT_TICK_EXCEL_FILE ="//span[normalize-space()='excelFile']"
    def get_result_tick_excel_file(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.RESULT_TICK_EXCEL_FILE)


    # Плюсик для открытия всего дерево Home
    BUTTON_PLUS_TREE_HOME = "//button[@title='Expand all']"

    def get_button_plus_home(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_PLUS_TREE_HOME)

    def click_to_button_plus_home(self):
        self.get_button_plus_home().click()
        #time.sleep(0.5)


    # Минус для закрытия всего дерево Home
    BUTTON_MINUS_TREE_HOME = "//button[@title='Collapse all']"

    def get_button_minus_home(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.BUTTON_PLUS_TREE_HOME)

    def click_to_button_minus_home(self):
        self.get_button_plus_home().click()
        #time.sleep(0.5)


    # Проверка элемента private на невидимость на странице
    INVISIBILITY_ELEMENT_PRIVATE = "//span[normalize-space()='private']"
    def get_invisibility_element_private(self):
        return self.wait_until_invisibility_of_element_located(By.XPATH, self.INVISIBILITY_ELEMENT_PRIVATE)
