from pytest_bdd import feature, scenario, given, when, then
from ..pages.home_page import HomePage
from ..pages.authentication import AuthPage



@scenario('login.feature', 'Login field exists')
def test_login_field():
    pass

@given('I am on main page')
def open_main_page(driver):
    # driver.get('http://automationpractice.com')
    home_page = HomePage(driver)
    home_page.open()

@when('I click login button')
def click_login_button(driver):
    HomePage(driver).open_sign_in()

@then('I see login field')
def check_login_field(driver):
    assert AuthPage(driver).is_displayed_email_field()