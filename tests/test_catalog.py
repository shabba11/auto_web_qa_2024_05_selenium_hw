from selenium.webdriver.common.by import By
from page_objects.catalog_page import CatalogPage
from page_objects.base_page import BasePage

import allure


url_desktops = '/desktops'


@allure.epic('Проверка страницы каталога')
class TestCatalog:
    @allure.title("Отображение кнопки 'Список'")
    def test_catalog_button_list(self, browser):
        CatalogPage(browser)

        with allure.step("Поиск кнопки 'Список'"):
            BasePage(browser).get_element((By.ID, "button-list"))

    @allure.title("Отображение кнопки 'Карточки'")
    def test_catalog_button_grid(self, browser):
        CatalogPage(browser)

        with allure.step("Поиск кнопки 'Карточки'"):
            BasePage(browser).get_element((By.ID, "button-grid"))

    @allure.title("Отображение категорий продуктов")
    def test_catalog_check_navbar(self, browser):
        CatalogPage(browser)

        with allure.step("Поиск категорий продуктов"):
            BasePage(browser).get_element((By.ID, "narbar-menu"))

    @allure.title("Отображение сортировки")
    def test_catalog_input_sort(self, browser):
        CatalogPage(browser)

        with allure.step("Поиск выпадающего списка с сортировкой"):
            BasePage(browser).get_element((By.ID, "input-sort"))

    @allure.title("Отображение количества продуктов")
    def test_catalog_input_limit(self, browser):
        CatalogPage(browser)

        with allure.step("Поиск выпадающего списка с отображением кол-ва продуктов"):
            BasePage(browser).get_element((By.ID, "input-limit"))

    @allure.title("Проверка смены валюты")
    def test_catalog_change_price(self, browser):
        CatalogPage(browser)

        with allure.step("Поиск продуктов"):
            products = BasePage(browser).get_elements((By.CSS_SELECTOR, 'div.col.mb-3'))

            with allure.step("Фиксирование цен на текущей валюте"):
                old_prices = []
                for product in products:
                    old_prices.append(product.find_element(by=By.CLASS_NAME, value="price-new").text)

        with allure.step("Смена валюты"):
            BasePage(browser).click((By.CSS_SELECTOR, "div.dropdown"))
            BasePage(browser).click((By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a'))

        with allure.step("Поиск продуктов"):
            new_products = BasePage(browser).get_elements((By.CSS_SELECTOR, 'div.col.mb-3'))

            with allure.step("Проверка смены валюты в продуктах"):
                for num, new_product in enumerate(new_products):
                    new_price = new_product.find_element(by=By.CLASS_NAME, value="price-new").text
                    assert old_prices[num] != new_price
                    assert new_price[-1] == '€'
