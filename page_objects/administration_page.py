import allure

from page_objects.base_page import BasePage


class AdministrationPage(BasePage):
    URL_ADMINISTRATION = "/administration"

    with allure.step("Открытие админской страницы"):
        def __init__(self, browser):
            self.browser = browser.get(browser.current_url + self.URL_ADMINISTRATION)

