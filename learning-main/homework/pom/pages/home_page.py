# from base_page import BasePage
from ..pages.base_page import BasePage
# from locators import home_page_locators as loc
from ..pages.locators.home_page_locators import home_page_locators as loc

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def sign_in_button(self):
        return self.find_element(loc.sign_in_button)

    def open(self):
        self.driver.get('test_site')

    def open_sign_in(self):
        self.find_element(loc.sign_in_button).click()
