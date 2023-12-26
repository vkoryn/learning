from .base_page import BasePage
from selenium.webdriver.common.by import By

email_field = (By.ID, 'email')
passwd = (By.ID, 'passwd')


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def email_field(self):
        return self.find_element(email_field)

    @property
    def passwd_field(self):
        return self.find_element(passwd)

    def is_displayed_email_field(self):
        return self.email_field.is_displayed()

