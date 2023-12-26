from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver = ('C:\chrome_driver\chromedriver.exe')
driver = webdriver.Chrome(chrome_driver)
# driver.get('https://www.onliner.by/')
chrome_driver = webdriver.Chrome()


from selenium.webdriver.common.keys import Keys
# chrome_driver = 'C:\chrome_driver\chromedriver.exe'
chrome_service = Service(executable_path=chrome_driver)

# service = Service(executable_path='C:\chrome_driver\chromedriver.exe')
options = Options()
options.add_argument('start-maximized')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(service=chrome_service, options=options)
# driver.maximize_window()


# def first_test(driver):
#     driver.get('https://www.onliner.by/')
#     # card_desktop  = driver.find_element(By.ID, 'widget-1-1')
#     # card_desktop.click()
#     # mobile_phone = driver.find_element(By.NAME, 'SSD')
#     # mobile_phone.click()
#     swiper_left = driver.find_element(By.CLASS_NAME, "swiper-button-next")
#     swiper_left.click()
#     b_main = driver.find_element(By.CLASS_NAME, "b-main-page-tabs__list")
#     print(b_main.text)
#     # sleep(3)
#     # url = driver.current_url
#     # title = driver.title
#     assert 'ПОМОГАЕМ ВЫБРАТЬ НАШИ СОЦСЕТИ' in b_main.text
#     # print(url, title)

def second_test(driver):
    driver.get('https://itexus.com/')
    # contact_us = driver.find_element(By.PARTIAL_LINK_TEXT, 'Contact Us')
    # contact_us.click()
    email_field = driver.find_element(By.CSS_SELECTOR, 'input[class="control-default nameValidate"]')
    email_field.send_keys('some text')
    email_field.send_keys(Keys.ENTER)
    alert_block = driver.find_element(By.XPATH, '//div/input[@title="Please enter valid email address"]')
    assert alert_block.text == "Please enter valid email address"



# driver.quit()