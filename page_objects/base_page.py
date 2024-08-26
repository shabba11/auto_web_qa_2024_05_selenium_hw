from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__

    def _text_xpath(self, text):
        return f"//*[text()='{text}']"

    def get_element(self, locator, timeout=3):
        self.logger.debug("%s: Getting element: %s" % (self.class_name, str(locator)))
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator, timeout=3):
        self.logger.debug("%s: Getting elements: %s" % (self.class_name, str(locator)))
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        self.logger.debug("%s: Clicking element: %s" % (self.class_name, str(locator)))
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(0.3).click().perform()

    def input_value(self, locator, texts):
        self.logger.debug("%s: Input %s in input %s" % (self.class_name, texts, locator))
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for text in texts:
            self.get_element(locator).send_keys(text)
