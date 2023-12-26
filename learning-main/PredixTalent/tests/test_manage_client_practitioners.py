import unittest
from allure import feature, step
from ..utils.webdriver_manager import create_chrome_driver
from ..pages.admin_page import AdminPage
from ..pages.login_page import LoginPage
import time



@feature('Manage client practitioners')
class TestManageClientPractitioners(unittest.TestCase):

    def setUp(self):
        self.driver = create_chrome_driver()
        self.driver.get('https://st-admin.talentpredix.com/')
        self.login_page = LoginPage(self.driver)
        self.admin_page = AdminPage(self.driver)

    @step('Login as admin')
    def test_manage_client_practitioners(self):
        self.login_page.login('igor.bogachek@itexus.com', '1qAZXSw2!')
        self.admin_page.navigate_to_manage_client_practitioner()
        self.admin_page.edit_client_practitioner_organization('Igor Bogacheck', 'TEST')
        organization_value = self.admin_page.get_organizaton_value_for_practitioner('Igor Bogacheck')
        self.assertEqual(organization_value, 'TEST', f"Organization value is not as expected: {organization_value}")


    def tearDown(self):
        time.sleep(6)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main




