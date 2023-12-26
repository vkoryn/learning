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

@pytest.mark.skip
def test_iframe(driver):
    driver.get('url')
    driver.find_element(By.CSS_SELECTOR, 'i[class="icon-eye-open"]').click()
    i_frame = driver.find_element(By.CSS_SELECTOR, 'iframe[class="fancybox-iframe"]')
    driver.switch_to.frame(i_frame)
    button_in_iframe = driver.find_element(By.TAG_NAME, 'button')
    button_in_iframe.click()
    sleep(3)


@pytest.mark.skip
def test_chain(driver):
    driver.get('url')
    cards = driver.find_element(By.CSS_SELECTOR, 'div[class="product-image-container"]')
    first_card = cards[0]
    quick_view = first_card.find_element(By.CSS_SELECTOR, 'a[class="quick-view"]')
    ActionChains(driver).move_to_element(first_card).click(quick_view).perform()
    sleep(5)

@pytest.mark.skip
def test_drag(driver):
    driver.get('https://demoqa.com/droppable')
    left = driver.find_element(By.ID, 'draggable')
    right = driver.find_element(By.ID, 'droppable')
    ActionChains(driver).drag_and_drop(left, right).perform()
    assert 'Dropped' in right.text
    sleep(3)

@pytest.mark.skip
def test_alert(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    first_button = driver.find_element(By.ID, 'alertexamples')
    second_button = driver.find_element(By.ID, 'confirmexample')
    third_button = driver.find_element(By.ID, 'promptexample')
    second_button.click()
    Alert(driver).dismiss()
    confirm = driver.find_element(By.ID, 'confirmreturn').text
    assert confirm == 'false'
    sleep(3)

@pytest.mark.skip
def test_screen(driver):
    driver.get('https://itexus.com/')
    filename = f'zop{datetime.now()}.png'
    try:
        domain_field = driver.find_element(By.ID, 'domain_name')
        domain_field.click()
    except NoSuchElementException as err:
        driver.save_screenshot(filename)
        raise err

def test_scroll(driver):
    sleep(5)
    driver.get('https://itexus.com/')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(5)





