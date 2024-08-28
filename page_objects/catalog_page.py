from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    URL_DESKTOPS = "/desktops"

    def __init__(self, browser):
        self.browser = browser.get(browser.current_url + '/en-gb/catalog' + self.URL_DESKTOPS)
