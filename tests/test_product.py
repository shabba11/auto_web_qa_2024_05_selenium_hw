from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.product_page import ProductPage

import allure


url_apple_cinema = '/apple-cinema'


@allure.epic('Проверка страницы продукта')
class TestProduct:
    @allure.title("Проверка Радио кнопки")
    def test_product_input_radio(self, browser):
        ProductPage(browser)

        with allure.step("Поиск выбора размера"):
            BasePage(browser).get_element((By.ID, "input-option-218"))

    @allure.title("Проверка ввода текста в окне 'Text'")
    def test_product_input_text(self, browser):
        ProductPage(browser)

        with allure.step("Поиск окна 'Text'"):
            BasePage(browser).get_element((By.ID, "input-option-208"))

    @allure.title("Проверка выпадающего списка со цветом")
    def test_product_input_select(self, browser):
        ProductPage(browser)

        with allure.step("Поиск выпадающего списка со цветом продукта"):
            BasePage(browser).get_element((By.ID, "input-option-217"))

    @allure.title("Проверка ввода текста в окне 'Text Area'")
    def test_product_input_text_area(self, browser):
        ProductPage(browser)

        with allure.step("Поиск окна 'Text Area'"):
            BasePage(browser).get_element((By.ID, "input-option-209"))

    @allure.title("Проверка кнопки загрузки файла")
    def test_product_button_upload(self, browser):
        ProductPage(browser)

        with allure.step("Поиск кнопки загрузки файла"):
            BasePage(browser).get_element((By.ID, "button-upload-222"))
