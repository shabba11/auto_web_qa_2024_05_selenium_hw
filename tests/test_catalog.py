from selenium.webdriver.common.by import By
from page_objects.catalog_page import CatalogPage
from page_objects.base_page import BasePage


url_desktops = '/desktops'


class TestCatalog:
    def test_catalog_button_list(self, browser):
        CatalogPage(browser)
        BasePage(browser).get_element((By.ID, "button-list"))

    def test_catalog_button_grid(self, browser):
        CatalogPage(browser)
        BasePage(browser).get_element((By.ID, "button-grid"))

    def test_catalog_check_navbar(self, browser):
        CatalogPage(browser)
        BasePage(browser).get_element((By.ID, "narbar-menu"))

    def test_catalog_input_sort(self, browser):
        CatalogPage(browser)
        BasePage(browser).get_element((By.ID, "input-sort"))

    def test_catalog_input_limit(self, browser):
        CatalogPage(browser)
        BasePage(browser).get_element((By.ID, "input-limit"))

    def test_catalog_change_price(self, browser):
        CatalogPage(browser)

        products = BasePage(browser).get_elements((By.CSS_SELECTOR, 'div.col.mb-3'))

        old_prices = []
        for product in products:
            old_prices.append(product.find_element(by=By.CLASS_NAME, value="price-new").text)

        BasePage(browser).click((By.CSS_SELECTOR, "div.dropdown"))
        BasePage(browser).click((By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a'))

        new_products = BasePage(browser).get_elements((By.CSS_SELECTOR, 'div.col.mb-3'))

        for num, new_product in enumerate(new_products):
            new_price = new_product.find_element(by=By.CLASS_NAME, value="price-new").text
            assert old_prices[num] != new_price
            assert new_price[-1] == '€'
