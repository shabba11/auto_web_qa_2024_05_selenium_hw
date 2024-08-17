from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class CartPage(BasePage):
    PRODUCT_IN_CART = By.XPATH, '//*[@id="shopping-cart"]/div/table/tbody'
    PRODUCT_NAME = By.CSS_SELECTOR, 'text-start.text-wrap'

    def get_cart_product_name(self, index=0):
        product = self.get_elements(self.PRODUCT_IN_CART)[index]
        return product.find_element(by=By.CSS_SELECTOR, value='td.text-start.text-wrap > a').text
