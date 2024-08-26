from selenium.webdriver.common.by import By
from page_objects.registration_page import RegistrationPage as RP
from page_objects.base_page import BasePage

import allure


@allure.epic('Проверка страницы регистрации пользователя')
class TestRegistration:
    @allure.title("Отображение FirstName")
    def test_registration_input_firstname(self, browser):
        RP(browser)

        with allure.step("Поиск окна ввода FirstName"):
            BasePage(browser).get_element((By.ID, "input-firstname"))

    @allure.title("Отображение LastName")
    def test_registration_input_lastname(self, browser):
        RP(browser)

        with allure.step("Поиск окна ввода LastName"):
            BasePage(browser).get_element((By.ID, "input-lastname"))

    @allure.title("Отображение ввода Email")
    def test_registration_input_email(self, browser):
        RP(browser)

        with allure.step("Поиск окна ввода Email"):
            BasePage(browser).get_element((By.ID, "input-email"))

    @allure.title("Отображение ввода Password")
    def test_registration_input_password(self, browser):
        RP(browser)

        with allure.step("Поиск окна ввода Password"):
            BasePage(browser).get_element((By.ID, "input-password"))

    @allure.title("Отображение кнопки рассылки")
    def test_registration_input_newsletter(self, browser):
        RP(browser)

        with allure.step("Поиск кнопки рассылки"):
            BasePage(browser).get_element((By.ID, "input-newsletter"))

    @allure.title("Регистрация нового пользователя")
    def test_registration_new_user(self, browser, user_registration):
        user_registration(firstname="Test", lastname="Test", e_mail="test1234@test.com", password="12345678Test")
