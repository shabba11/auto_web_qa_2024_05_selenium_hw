from selenium.webdriver.common.by import By
from page_objects.cart_page import CartPage
from page_objects.main_page import MainPage
from page_objects.base_page import BasePage
from page_objects.alert_element import AlertSuccessElement

import allure


@allure.epic("Проверка главной страницы")
class TestMainPage:
    @allure.title("Отображение кнопки Корзины")
    def test_main_page_cart(self, browser):
        with allure.step("Поиск кнопки Корзины"):
            BasePage(browser).get_element((By.ID, "header-cart"))

    @allure.title("Отображение списка Валют")
    def test_main_page_dropdown_toggle(self, browser):
        with allure.step("Поиск выпадающего списка с валютами"):
            BasePage(browser).get_element((By.CLASS_NAME, "dropdown-toggle"))

    @allure.title("Отображение категорий товаров")
    def test_main_page_navbar(self, browser):
        with allure.step("Поиск категорий товаров"):
            BasePage(browser).get_element((By.ID, "narbar-menu"))

    @allure.title("Отображение товаров карусели")
    def test_main_page_carousel(self, browser):
        with allure.step("Поиск карусели товаров"):
            BasePage(browser).get_element((By.ID, "carousel-banner-0"))

    @allure.title("Отображение спонсоров")
    def test_main_page_carousel_banner_sponsors(self, browser):
        with allure.step("Поиск карусели спонсоров"):
            BasePage(browser).get_element((By.ID, "carousel-banner-1"))

    @allure.title("Добавление продукта в корзину")
    def test_main_page_add_to_cart(self, browser):
        product_name = MainPage(browser).get_featured_product_name()

        with allure.step("Добавление продукта в корзину"):
            MainPage(browser).click_featured_product_add_to_card()

            with allure.step("Нажатие на ссылку корзины"):
                AlertSuccessElement(browser).shopping_cart.click()

        with allure.step("Проверка добавленного продукта в корзине"):
            product_name_in_cart = CartPage(browser).get_cart_product_name()
            assert product_name == product_name_in_cart

    @allure.title("Смена валюты на главной странице")
    def test_main_page_change_price(self, browser):
        with allure.step("Поиск продуктов"):
            products = BasePage(browser).get_elements((By.CLASS_NAME, 'product-thumb'))

            with allure.step("Фиксирование цен на текущей валюте"):
                old_prices = []
                for product in products:
                    old_prices.append(product.find_element(by=By.CLASS_NAME, value="price-new").text)

        with allure.step("Смена валюты"):
            BasePage(browser).get_element((By.CSS_SELECTOR, "div.dropdown")).click()
            BasePage(browser).get_element((By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a')).click()

        with allure.step("Поиск продуктов"):
            new_products = BasePage(browser).get_elements((By.CLASS_NAME, 'product-thumb'))

        with allure.step("Проверка смены валюты в продуктах"):
            for num, new_product in enumerate(new_products):
                new_price = new_product.find_element(by=By.CLASS_NAME, value="price-new").text
                assert old_prices[num] != new_price
                assert new_price[-1] == '€'
