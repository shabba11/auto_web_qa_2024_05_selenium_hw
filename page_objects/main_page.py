import time

from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class MainPage(BasePage):
    FEATURED_PRODUCT_NAME = By.CLASS_NAME, 'product-thumb'
    FEATURED_PRODUCT_ADD_TO_CART = By.CSS_SELECTOR, 'i.fa-solid.fa-shopping-cart'

    def get_featured_product_name(self, index=0):
        product = self.get_elements(self.FEATURED_PRODUCT_NAME)[index]
        return product.find_element(by=By.CSS_SELECTOR, value='div.description > h4 > a').text

    def click_featured_product_add_to_card(self, index=0):
        product = (self.get_elements(self.FEATURED_PRODUCT_NAME)[index])
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        product.find_element(by=By.CSS_SELECTOR, value='i.fa-solid.fa-shopping-cart').click()
