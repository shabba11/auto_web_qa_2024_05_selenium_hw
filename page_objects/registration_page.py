from page_objects.base_page import BasePage


class RegistrationPage(BasePage):
    URL_REGISTRATION = "/en-gb?route=account/register"

    def __init__(self, browser):
        self.browser = browser.get(browser.current_url + self.URL_REGISTRATION)