from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'email-input')
        self.password_input = (By.ID, 'password')
        self.signin_button = (By.XPATH, '/html/body/section/div[1]/div/div/div[1]/form/div[3]/button')

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signin_button).click()
