from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.administration_page import AdministrationPage as AP
from selenium.webdriver.common.action_chains import ActionChains


def add_product(browser):
    """Добавление нового продукта

    :param browser: Объект браузера
    """
    BasePage(browser).get_element((By.ID, 'menu-catalog')).click()
    BasePage(browser).get_element((By.XPATH, '//*[@id="collapse-1"]/li[2]')).click()
    BasePage(browser).get_element((By.XPATH, '//*[@id="content"]/div[1]/div/div/a')).click()
    BasePage(browser).input_value((By.ID, 'input-name-1'), texts='Test_Product')
    BasePage(browser).click((By.ID, 'input-meta-title-1'))
    BasePage(browser).input_value((By.ID, 'input-meta-title-1'), texts='Test_Title')
    BasePage(browser).get_element((By.XPATH, '//*[@id="form-product"]/ul/li[2]/a')).click()
    BasePage(browser).input_value((By.ID, 'input-model'), texts='TestModel')
    BasePage(browser).get_element((By.XPATH, '//*[@id="form-product"]/ul/li[11]/a')).click()
    BasePage(browser).input_value((By.ID, 'input-keyword-0-1'), texts='Test')
    BasePage(browser).get_element((By.XPATH, '//*[@id="content"]/div[1]/div/div/button')).click()
    BasePage(browser).get_element((By.XPATH, '//*[@id="collapse-1"]/li[2]/a')).click()


class TestAdministration:

    def test_administration_locate_username(self, browser):
        AP(browser)
        BasePage(browser).get_element((By.ID, "input-username"))

    def test_administration_locate_password(self, browser):
        AP(browser)
        BasePage(browser).get_element((By.ID, "input-password"))

    def test_administration_locate_button_password(self, browser):
        AP(browser)
        BasePage(browser).get_element((By.CSS_SELECTOR, "button.btn.btn-primary"))

    def test_administration_locate_card_header(self, browser):
        AP(browser)
        BasePage(browser).get_element((By.CLASS_NAME, "card-header"))

    def test_administration_login_and_logout(self, browser, login_administration):
        BasePage(browser).get_element((By.CSS_SELECTOR, "i.fa-solid.fa-sign-out")).click()

        assert browser.current_url == "http://localhost/administration/index.php?route=common/login"

    def test_administration_add_new_product(self, browser, login_administration):
        add_product(browser=browser)

        BasePage(browser).click((By.XPATH, '//*[@id="form-product"]/div[2]/div[1]/ul/li[4]/a'))
        product = BasePage(
            browser).get_elements((By.CSS_SELECTOR, 'table.table.table-bordered.table-hover > tbody > tr'))[-1]
        product_name = product.find_element(by=By.CSS_SELECTOR, value='td.text-start').text

        assert product_name == 'Test_Product\nEnabled'

    def test_administration_delete_product(self, browser, login_administration):
        add_product(browser=browser)

        BasePage(browser).click((By.XPATH, '//*[@id="form-product"]/div[2]/div[1]/ul/li[4]/a'))
        product = BasePage(
            browser).get_elements((By.CSS_SELECTOR, 'table.table.table-bordered.table-hover > tbody > tr'))[-1]
        BasePage(product).get_element((By.CLASS_NAME, 'form-check-input')).click()
        ActionChains(browser).move_to_element(
            browser.find_elements(By.XPATH, '//*[@id="content"]/div[1]/div/div/button')[-1]).click().perform()
        alert = browser.switch_to.alert
        alert.accept()

        product = BasePage(
            browser).get_elements((By.CSS_SELECTOR, 'table.table.table-bordered.table-hover > tbody > tr'))[-1]
        product_name = product.find_element(by=By.CSS_SELECTOR, value='td.text-start').text

        assert product_name != 'Test_Product\nEnabled'
