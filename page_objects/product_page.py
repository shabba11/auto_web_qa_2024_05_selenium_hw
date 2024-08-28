from page_objects.base_page import BasePage


class ProductPage(BasePage):
    URL_PRODUCT = "/en-gb/product"
    URL_APPLE_CINEMA = '/apple-cinema'

    def __init__(self, browser):
        self.browser = browser.get(browser.current_url + self.URL_PRODUCT + self.URL_APPLE_CINEMA)