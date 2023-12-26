from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def create_chrome_driver():
    chrome_driver_path = 'C:\chrome_driver\chromedriver.exe'
    chrome_service = Service(executable_path=chrome_driver_path)
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(service=chrome_service, options=options)
    driver.implicitly_wait(3)
    return driver
