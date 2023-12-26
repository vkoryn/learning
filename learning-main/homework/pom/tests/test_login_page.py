from ..pages.home_page import HomePage
from ..pages.authentication import AuthPage
import allure

@allure.feature('Authentication')
@allure.story('Login')
def test_login(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Click Sign in button'):
        home_page.open_sign_in()
    auth_page = AuthPage(driver)
    assert auth_page.is_displayed_email_field()

@allure.feature('Authentication')
@allure.story('Registration')
def test_passwd(driver):
    with allure.step('Open Home Page'):
        home_page = HomePage(driver)
        home_page.open()
    with allure.step('Click Sign in button'):
        home_page.sign_in_button.click()
    home_page.open_sign_in()
    auth_page = AuthPage(driver)
    assert auth_page.passwd_field.is_displayed()


