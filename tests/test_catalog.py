from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url_desktops = '/desktops'


class TestCatalog:
    def test_catalog_button_list(self, browser, url_catalog):
        browser.get(url_catalog + url_desktops)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "button-list")))

    def test_catalog_button_grid(self, browser, url_catalog):
        browser.get(url_catalog + url_desktops)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "button-grid")))

    def test_catalog_check_navbar(self, browser, url_catalog):
        browser.get(url_catalog + url_desktops)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "narbar-menu")))

    def test_catalog_input_sort(self, browser, url_catalog):
        browser.get(url_catalog + url_desktops)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "input-sort")))

    def test_catalog_input_limit(self, browser, url_catalog):
        browser.get(url_catalog + url_desktops)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "input-limit")))

    def test_catalog_change_price(self, browser, url_catalog):
        browser.get(url_catalog + url_desktops)

        products = browser.find_elements(by=By.CSS_SELECTOR, value='div.col.mb-3')

        old_prices = []
        for product in products:
            old_prices.append(product.find_element(by=By.CLASS_NAME, value="price-new").text)

        browser.find_element(by=By.CSS_SELECTOR, value="div.dropdown").click()
        browser.find_element(by=By.XPATH, value='//*[@id="form-currency"]/div/ul/li[1]/a').click()

        new_products = browser.find_elements(by=By.CSS_SELECTOR, value='div.col.mb-3')

        for num, new_product in enumerate(new_products):
            new_price = new_product.find_element(by=By.CLASS_NAME, value="price-new").text
            assert old_prices[num] != new_price
            assert new_price[-1] == '€'
