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

    def test_registration_new_user(self, browser, user_registration):
        user_registration(firstname="Test", lastname="Test", e_mail="test1234@test.com", password="12345678Test")
