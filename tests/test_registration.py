from selenium.webdriver.common.by import By
from page_objects.registration_page import RegistrationPage as RP
from page_objects.base_page import BasePage


class TestRegistration:
    def test_registration_input_firstname(self, browser):
        RP(browser)
        BasePage(browser).get_element((By.ID, "input-firstname"))

    def test_registration_input_lastname(self, browser):
        RP(browser)
        BasePage(browser).get_element((By.ID, "input-lastname"))

    def test_registration_input_email(self, browser):
        RP(browser)
        BasePage(browser).get_element((By.ID, "input-email"))

    def test_registration_input_password(self, browser):
        RP(browser)
        BasePage(browser).get_element((By.ID, "input-password"))

    def test_registration_input_newsletter(self, browser):
        RP(browser)
        BasePage(browser).get_element((By.ID, "input-newsletter"))

    def test_registration_new_user(self, browser):
        RP(browser)

        BasePage(browser).input_value((By.ID, 'input-firstname'), texts='Test')
        BasePage(browser).input_value((By.ID, "input-lastname"), texts='Test')
        BasePage(browser).input_value((By.ID, "input-email"), texts='test@test.com')
        BasePage(browser).input_value((By.ID, "input-password"), texts='test_password')

        BasePage(browser).click((By.XPATH, '//*[@id="form-register"]/div/div/input'))
        BasePage(browser).click((By.XPATH, '//*[@id="form-register"]/div/button'))

        text_success = BasePage(browser).get_element((By.XPATH, '//*[@id="content"]/h1')).text
        assert text_success == 'Your Account Has Been Created!'
