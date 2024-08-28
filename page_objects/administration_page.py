from page_objects.base_page import BasePage


class AdministrationPage(BasePage):
    URL_ADMINISTRATION = "/administration"

    def __init__(self, browser):
        self.browser = browser.get(browser.current_url + self.URL_ADMINISTRATION)

