import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMainPage:
    def test_main_page_cart(self, browser, base_url):
        browser.get(base_url)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "header-cart")))

    def test_main_page_dropdown_toggle(self, browser, base_url):
        browser.get(base_url)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.CLASS_NAME, "dropdown-toggle")))

    def test_main_page_navbar(self, browser, base_url):
        browser.get(base_url)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "narbar-menu")))

    def test_main_page_carousel(self, browser, base_url):
        browser.get(base_url)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "carousel-banner-0")))

    def test_main_page_carousel_banner_sponsors(self, browser, base_url):
        browser.get(base_url)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "carousel-banner-1")))

    def test_main_page_add_to_cart(self, browser, base_url):
        browser.get(base_url)

        products = browser.find_elements(by=By.CLASS_NAME, value='product-thumb')
        product_name = products[0].find_element(by=By.CSS_SELECTOR, value="a").accessible_name

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2) # не нашел способа, как дождаться загрузки элемента "добавления в корзину"

        products[0].find_element(by=By.CSS_SELECTOR, value="i.fa-solid.fa-shopping-cart").click()

        browser.get(base_url + "/en-gb?route=checkout/cart")

        cart_product = browser.find_element(by=By.XPATH, value='//div/table/tbody/tr/td[2]/a')

        assert product_name == cart_product.accessible_name

    def test_main_page_change_price(self, browser, base_url):
        browser.get(base_url)

        products = browser.find_elements(by=By.CLASS_NAME, value='product-thumb')

        old_prices = []
        for product in products:
            old_prices.append(product.find_element(by=By.CLASS_NAME, value="price-new").text)

        browser.find_element(by=By.CSS_SELECTOR, value="div.dropdown").click()
        browser.find_element(by=By.XPATH, value='//*[@id="form-currency"]/div/ul/li[1]/a').click()

        new_products = browser.find_elements(by=By.CLASS_NAME, value='product-thumb')

        for num, new_product in enumerate(new_products):
            new_price = new_product.find_element(by=By.CLASS_NAME, value="price-new").text
            assert old_prices[num] != new_price
            assert new_price[-1] == '€'
