import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_driver = 'C:\chrome_driver\chromedriver.exe'
chrome_service = Service(executable_path=chrome_driver)


@pytest.mark.skip('not needed')
def test_find_element_on_new_tab(driver, print_text):
    print('test tabs')
    driver.get('https://the-internet.herokuapp.com/windows')
    link = driver.find_element(By.LINK_TEXT, 'Click Here')
    link.click()
    # print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])
    new_element = driver.find_element(By.TAG_NAME, 'h3')
    assert new_element.text == 'New Window'
    sleep(3)
    driver.close()
    sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    new_element = driver.find_element(By.TAG_NAME, 'h3')
    assert new_element.text == 'Opening a new window'

@pytest.mark.parametrize('a, b', [[1, 2]])
def test_sum(a, b, print_text):
    print('sum')
    result = a + b
    assert a+b == result, 'Результат не соответствует ожидаемому'

# @pytest.mark.parametrize('x', [1, 2, 3])
@pytest.mark.skip
def test_diff(x):
    print('diff')
    assert 3-2 == x, 'Результат не соответствует ожидаемому'




