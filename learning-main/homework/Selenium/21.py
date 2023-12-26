from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
chrome_driver = 'C:\chrome_driver\chromedriver.exe'
chrome_service = Service(executable_path=chrome_driver)
options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(service=chrome_service, options=options)
options.add_argument('start-maximized')
from selenium.webdriver.common.keys import Keys

def tabs(driver):
    driver.get('https://the-internet.herokuapp.com/windows')
    link = driver.find_element(By.LINK_TEXT, 'Click Here')
    link.click()
    # print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])
    new_element = driver.find_element(By.TAG_NAME, 'h3')
    print(new_element.text)
    sleep(3)
    driver.close()
    sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    new_element = driver.find_element(By.TAG_NAME, 'h3')
    print(new_element.text)

tabs(driver)
driver.quit()