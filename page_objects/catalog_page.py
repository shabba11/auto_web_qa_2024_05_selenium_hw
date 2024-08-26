from page_objects.base_page import BasePage

import allure


class CatalogPage(BasePage):
    URL_DESKTOPS = "/desktops"

    with allure.step("Открытие страницы каталога"):
        def __init__(self, browser):
            self.browser = browser.get(browser.current_url + '/en-gb/catalog' + self.URL_DESKTOPS)
