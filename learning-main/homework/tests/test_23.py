import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException

chrome_driver = 'C:\chrome_driver\chromedriver.exe'
chrome_service = Service(executable_path=chrome_driver)

def test_login(driver):
    driver.get('url_example')
    driver.find_element(By.CSS_SELECTOR, 'a[class="login"]').click()
    login_field = driver.find_element(By.ID, 'email')
    assert login_field.is_displayed()






def test_password(driver):
    driver.get('url_example')
    driver.find_element(By.CSS_SELECTOR, 'a[class="login"]').click()
    password_field = driver.find_element(By.ID, 'passwd')
    assert password_field.is_displayed()

