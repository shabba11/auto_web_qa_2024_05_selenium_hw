from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url_apple_cinema = '/apple-cinema'


class TestProduct:
    def test_product_input_radio(self, browser, url_product):
        browser.get(url_product + url_apple_cinema)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "input-option-218")))

    def test_product_input_text(self, browser, url_product):
        browser.get(url_product + url_apple_cinema)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "input-option-208")))

    def test_product_input_select(self, browser, url_product):
        browser.get(url_product + url_apple_cinema)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "input-option-217")))

    def test_product_input_text_area(self, browser, url_product):
        browser.get(url_product + url_apple_cinema)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "input-option-209")))

    def test_product_button_upload(self, browser, url_product):
        browser.get(url_product + url_apple_cinema)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "button-upload-222")))
