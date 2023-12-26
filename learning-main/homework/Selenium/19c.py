from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver = 'C:\chrome_driver\chromedriver.exe'
chrome_service = Service(executable_path=chrome_driver)
options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(service=chrome_service, options=options)


def second_test(driver):
    driver.get('https://itexus.com/')
    # Добавьте ваш код внутри функции


second_test(driver)
