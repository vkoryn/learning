from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_driver = 'C:\chrome_driver\chromedriver.exe'
chrome_service = Service(executable_path=chrome_driver)
options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(service=chrome_service, options=options)

def open_site(driver):
    driver.get('https://itexus.com/')
    time.sleep(5)

open_site(driver)


driver.quit()

