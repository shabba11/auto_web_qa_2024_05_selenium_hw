from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.product_page import ProductPage


url_apple_cinema = '/apple-cinema'


class TestProduct:
    def test_product_input_radio(self, browser):
        ProductPage(browser)
        BasePage(browser).get_element((By.ID, "input-option-218"))

    def test_product_input_text(self, browser):
        ProductPage(browser)
        BasePage(browser).get_element((By.ID, "input-option-208"))

    def test_product_input_select(self, browser):
        ProductPage(browser)
        BasePage(browser).get_element((By.ID, "input-option-217"))

    def test_product_input_text_area(self, browser):
        ProductPage(browser)
        BasePage(browser).get_element((By.ID, "input-option-209"))

    def test_product_button_upload(self, browser):
        ProductPage(browser)
        BasePage(browser).get_element((By.ID, "button-upload-222"))
