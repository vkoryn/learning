from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
driver.implicitly_wait(10)

# def second_test(driver):
#     driver.get('https://itexus.com/')
#     contact_us = driver.find_element(By.PARTIAL_LINK_TEXT, 'Contact Us')
#     contact_us.click()
#     email_field = driver.find_element(By.CSS_SELECTOR, 'input[class="control-default nameValidate"]')
#     email_field.send_keys('some text')
#     # email_field.clear()
#     # email_field.send_keys(Keys.ENTER)
#     # nda = driver.find_element(By.XPATH, '//div/label[@for="nda"]')
#     # nda.click()
#     send_message = driver.find_element(By.XPATH, '//div/h3[@data-tab-id="1"]')
#     send_message.click()
#     contact_us_color = contact_us.value_of_css_property('itx-color-accent')
#     assert contact_us == '#2CAA4D'
#     # alert_block = driver.find_element(By.XPATH, '//div/input[@title="Please enter valid email address"]')
#     # assert alert_block.text == "Please enter valid email address"

# def green_button(driver):
#     driver.get('https://itexus.com/')
#     green_button = driver.find_element(By.CLASS_NAME, 'itx-btn_lg')
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located()
#     )
#     print(green_button.is_displayed())
#     assert green_button.is_displayed()
#     driver.quit()
#
# def check_select(driver):
#     select=Select(driver.find_element(By.ID, 'faq-1'))

def get_cookies(driver):
    driver.get('https://itexus.com/')
    cookies = driver.get_cookies()
    print(cookies)


# second_test(driver=driver)
# green_button(driver=driver)
# check_select(driver=driver)
get_cookies(driver=driver)

