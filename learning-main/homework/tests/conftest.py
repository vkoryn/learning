import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope='function')
def driver():
    # print('\nbefore test\n')
    options = Options()
    # options.add_argument('start-maximized')
    chrome_driver = 'C:\chrome_driver\chromedriver.exe'
    chrome_service = Service(executable_path=chrome_driver)
    driver = webdriver.Chrome(service=chrome_service, options=options)
    options.add_argument('start-maximized')
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def print_text():
    # print('\nbefore test1\n')
    yield None
    # print('\nafter test1\n')