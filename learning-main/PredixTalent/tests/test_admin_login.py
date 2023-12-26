import unittest
from ..utils.webdriver_manager import create_chrome_driver
from ..pages.admin_page import AdminPage
from ..pages.login_page import LoginPage
import time


class TestAdminLogin(unittest.TestCase):

    def setUp(self):
        self.driver = create_chrome_driver()
        self.driver.get('https://st-admin.talentpredix.com/')
        self.login_page = LoginPage(self.driver)
        self.admin_page = AdminPage(self.driver)

    def test_admin_login_and_check_content_cms_button(self):
        self.login_page.login('igor.bogachek@itexus.com', '1qAZXSw2!')
        self.assertTrue(self.admin_page.is_content_cms_button_present())

    def tearDown(self):
        time.sleep(6)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()



