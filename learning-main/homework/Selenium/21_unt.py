import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
chrome_driver = 'C:\chrome_driver\chromedriver.exe'
chrome_service = Service(executable_path=chrome_driver)

class Test21(unittest.TestCase):
    # def __init__():
    #     self.driver = None
    driver = None

    def setUp(self):
        print('\nbefore test\n')
        options = Options()
        # options.add_argument('start-maximized')
        self.driver = webdriver.Chrome(service=chrome_service, options=options)
        options.add_argument('start-maximized')

    def tearDown(self):
        print('\nafter test\n')
        self.driver.quit()

    def test_find_element_on_new_tab(self):
        print('test tabs')
        self.driver.get('https://the-internet.herokuapp.com/windows')
        link = self.driver.find_element(By.LINK_TEXT, 'Click Here')
        link.click()
        # print(driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[1])
        new_element = self.driver.find_element(By.TAG_NAME, 'h3')
        self.assertEqual(new_element.text, 'New Window')
        sleep(3)
        self.driver.close()
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        new_element = self.driver.find_element(By.TAG_NAME, 'h3')
        self.assertEqual(new_element.text, 'Opening a new window')

    @unittest.skipIf(datetime.now().year == 2022, 'skipped in 2022')
    def test_sum(self):
        print('test sum')
        self.assertEqual(2+2, 4)


if __name__ == '__main__':
    unittest.main()