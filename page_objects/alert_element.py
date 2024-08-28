import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertSuccessElement:
    SUCCESS_ALERT = By.CSS_SELECTOR, ".alert-success"
    LOGIN_LINK = By.LINK_TEXT, "login"
    SHOPPING_CART_LINK = By.LINK_TEXT, "shopping cart"
    COMPARISON_LINK = By.LINK_TEXT, "product comparison"

    def __init__(self, browser):
        self.browser = browser
        self.alert = WebDriverWait(self.browser, 3).until(
            EC.visibility_of_element_located(self.SUCCESS_ALERT))

    @property
    def shopping_cart(self):
        with allure.step("Поиск таблички с добавление товара в корзину"):
            return self.alert.find_element(*self.SHOPPING_CART_LINK)