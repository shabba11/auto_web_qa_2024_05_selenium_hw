from selenium.webdriver.common.by import By
from page_objects.cart_page import CartPage
from page_objects.main_page import MainPage
from page_objects.base_page import BasePage
from page_objects.alert_element import AlertSuccessElement


class TestMainPage:
    def test_main_page_cart(self, browser):
        BasePage(browser).get_element((By.ID, "header-cart"))

    def test_main_page_dropdown_toggle(self, browser):
        BasePage(browser).get_element((By.CLASS_NAME, "dropdown-toggle"))

    def test_main_page_navbar(self, browser):
        BasePage(browser).get_element((By.ID, "narbar-menu"))

    def test_main_page_carousel(self, browser):
        BasePage(browser).get_element((By.ID, "carousel-banner-0"))

    def test_main_page_carousel_banner_sponsors(self, browser):
        BasePage(browser).get_element((By.ID, "carousel-banner-1"))

    def test_main_page_add_to_cart(self, browser):
        product_name = MainPage(browser).get_featured_product_name()
        MainPage(browser).click_featured_product_add_to_card()
        AlertSuccessElement(browser).shopping_cart.click()
        product_name_in_cart = CartPage(browser).get_cart_product_name()

        assert product_name == product_name_in_cart

    def test_main_page_change_price(self, browser):
        products = BasePage(browser).get_elements((By.CLASS_NAME, 'product-thumb'))

        old_prices = []
        for product in products:
            old_prices.append(product.find_element(by=By.CLASS_NAME, value="price-new").text)

        BasePage(browser).get_element((By.CSS_SELECTOR, "div.dropdown")).click()
        BasePage(browser).get_element((By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a')).click()

        new_products = BasePage(browser).get_elements((By.CLASS_NAME, 'product-thumb'))

        for num, new_product in enumerate(new_products):
            new_price = new_product.find_element(by=By.CLASS_NAME, value="price-new").text
            assert old_prices[num] != new_price
            assert new_price[-1] == '€'
