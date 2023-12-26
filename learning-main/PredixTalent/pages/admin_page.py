from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:

    def __init__(self, driver):
        self.driver = driver
        self.content_cms_button = (By.XPATH,
            '/html/body/app-root/div/lib-side-menu-layout/div/div[1]/lib-side-menu/div/a[9]')

    def is_content_cms_button_present(self):
        return self.driver.find_element(*self.content_cms_button).is_displayed()

    def navigate_to_manage_client_practitioner(self):
        clients_button = (By.XPATH,
                          '/html/body/app-root/div/lib-side-menu-layout/div/div[1]/lib-side-menu/div/a[2]')
        practitioners_button = (By.XPATH,
                                '/html/body/app-root/div/lib-side-menu-layout/div/div[2]/ng-component/div/div/ng-component/div[2]/div[2]/ng-component/div/div[1]/a[2]')

        self.driver.find_element(*clients_button).click()

        self.driver.find_element(*practitioners_button).click()

    def edit_client_practitioner_organization(self, practitioner_name, new_organization):
        practitioner_locator = (By.XPATH,
                                '/html/body/app-root/div/lib-side-menu-layout/div/div[2]/ng-component/div/div/ng-component/div[2]/div[2]/ng-component/div/div[2]/app-practitioners-list/div/div[3]/lib-table/div/table/tbody/tr[4]/td[2]/lib-dynamic-node/app-practitioner-name-node/button')
        practitioner_element = WebDriverWait(self.driver,  10).until(EC.visibility_of_element_located(practitioner_locator))

        practitioner_element.click()

        dropdown_locator = (By.XPATH,
                            '/html/body/app-root/div/lib-side-menu-layout/div/div[2]/ng-component/div/div/ng-component/ng-component/app-put-practitioner/div/form/lib-custom-select[2]/div/div/ng-select')
        dropdown_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(dropdown_locator))

        dropdown_element.click()

        organization_option_locator = (By.XPATH,
                                       '/html/body/app-root/div/lib-side-menu-layout/div/div[2]/ng-component/div/div/ng-component/ng-component/app-put-practitioner/div/form/lib-custom-select[2]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[3]')
        organization_option_element = WebDriverWait(self.driver,  10).until(EC.visibility_of_element_located(organization_option_locator))

        organization_option_element.click()

        save_button_locator = (By.XPATH,
                               '/html/body/app-root/div/lib-side-menu-layout/div/div[2]/ng-component/div/div/ng-component/ng-component/app-put-practitioner/div/div[2]/button[1]')
        save_button_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(save_button_locator))

        save_button_element.click()

    def get_organizaton_value_for_practitioner(self, practitioner_name):
       organization_column_locator = (By.XPATH,
                                      '/html/body/app-root/div/lib-side-menu-layout/div/div[2]/ng-component/div/div/ng-component/div[2]/div[2]/ng-component/div/div[2]/app-practitioners-list/div/div[3]/lib-table/div/table/tbody/tr[4]/td[7]/lib-dynamic-node/div')
       organization_column_value = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(organization_column_locator)).text

       return organization_column_value








