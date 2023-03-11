import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(autouse=True)
def setup(request, browser):
    driver_service_chrome = Service(executable_path="C:\\webbrowser\\chromedriver.exe")
    driver_service_firefox = Service(executable_path="C:\\webbrowser\\firefoxdriver.exe")
    driver_service_edge = Service(executable_path="C:\\webbrowser\\edgedriver.exe")
    if browser == "chrome":
        driver = webdriver.Chrome(service=driver_service_chrome)
    elif browser == "firefox":
        driver = webdriver.Firefox(service=driver_service_firefox)
    elif browser == "edge":
        driver = webdriver.Edge(service=driver_service_edge)
    driver.maximize_window()
    driver.get("https://demoqa.com/")
    time.sleep(0.5)
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


