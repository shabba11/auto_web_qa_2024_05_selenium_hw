from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.administration_page import AdministrationPage as AP
from selenium.webdriver.common.action_chains import ActionChains

import allure


def add_product(browser):
    """Добавление нового продукта

    :param browser: Объект браузера
    """
    with allure.step("Нажатие выпадающего списка 'Catalog'"):
        BasePage(browser).get_element((By.ID, 'menu-catalog')).click()

    with allure.step("Нажатие кнопки 'Products'"):
        BasePage(browser).get_element((By.XPATH, '//*[@id="collapse-1"]/li[2]')).click()

    with allure.step("Нажатие кнопки 'Add new'"):
        BasePage(browser).get_element((By.XPATH, '//*[@id="content"]/div[1]/div/div/a')).click()

    with allure.step("Ввод Product Name"):
        BasePage(browser).input_value((By.ID, 'input-name-1'), texts='Test_Product')

    with allure.step("Ввод 'Meta Tag Title'"):
        BasePage(browser).click((By.ID, 'input-meta-title-1'))
        BasePage(browser).input_value((By.ID, 'input-meta-title-1'), texts='Test_Title')

    with allure.step("Нажатие кнопки Data"):
        BasePage(browser).get_element((By.XPATH, '//*[@id="form-product"]/ul/li[2]/a')).click()

    with allure.step("Ввод 'Model' продукта"):
        BasePage(browser).input_value((By.ID, 'input-model'), texts='TestModel')

    with allure.step("Нажатие кнопки SEO и ввод Keyword"):
        BasePage(browser).get_element((By.XPATH, '//*[@id="form-product"]/ul/li[11]/a')).click()
        BasePage(browser).input_value((By.ID, 'input-keyword-0-1'), texts='Test')

    with allure.step("Нажатие кнопки Save и переход на страницу Products"):
        BasePage(browser).get_element((By.XPATH, '//*[@id="content"]/div[1]/div/div/button')).click()
        BasePage(browser).get_element((By.XPATH, '//*[@id="collapse-1"]/li[2]/a')).click()


@allure.epic('Проверка админской страницы')
class TestAdministration:

    @allure.title("Отображение поля 'Username'")
    def test_administration_locate_username(self, browser):
        AP(browser)

        with allure.step("Поиск поля ввода 'Username'"):
            BasePage(browser).get_element((By.ID, "input-username"))

    @allure.title("Отображение поля 'Password'")
    def test_administration_locate_password(self, browser):
        AP(browser)

        with allure.step("Поиск поля ввода 'Password'"):
            BasePage(browser).get_element((By.ID, "input-password"))

    @allure.title("Отображение кнопки 'Login'")
    def test_administration_locate_button_login(self, browser):
        AP(browser)

        with allure.step("Поиск кнопки 'Login'"):
            BasePage(browser).get_element((By.CSS_SELECTOR, "button.btn.btn-primary"))

    @allure.title("Отображение Card-header")
    def test_administration_locate_card_header(self, browser):
        AP(browser)

        with allure.step("Поиск заголовка Card-header"):
            BasePage(browser).get_element((By.CLASS_NAME, "card-header"))

    @allure.title("Проверка авторизации и деавторизации пользователя")
    def test_administration_login_and_logout(self, browser, login_administration):
        with allure.step("Нажатие кнопки разлогирование пользователя"):
            BasePage(browser).get_element((By.CSS_SELECTOR, "i.fa-solid.fa-sign-out")).click()

        with allure.step("Проверка разлогирования пользователя"):
            assert browser.current_url == "http://localhost/administration/index.php?route=common/login"

    @allure.title("Добавление нового продукта")
    def test_administration_add_new_product(self, browser, login_administration):
        add_product(browser=browser)

        with allure.step("Поиск добавленного продукта"):
            BasePage(browser).click((By.XPATH, '//*[@id="form-product"]/div[2]/div[1]/ul/li[4]/a'))
            product = BasePage(
                browser).get_elements((By.CSS_SELECTOR, 'table.table.table-bordered.table-hover > tbody > tr'))[-1]
            product_name = product.find_element(by=By.CSS_SELECTOR, value='td.text-start').text

        with allure.step("Проверка совпадения добавленного продукта с ожидаемым"):
            assert product_name == 'Test_Product\nEnabled'

    @allure.title("Удаление продукта")
    def test_administration_delete_product(self, browser, login_administration):
        add_product(browser=browser)

        with allure.step("Поиск продукта и удаление"):
            BasePage(browser).click((By.XPATH, '//*[@id="form-product"]/div[2]/div[1]/ul/li[4]/a'))
            product = BasePage(
                browser).get_elements((By.CSS_SELECTOR, 'table.table.table-bordered.table-hover > tbody > tr'))[-1]
            product.find_element(by=By.CLASS_NAME, value='form-check-input').click()
            ActionChains(browser).move_to_element(
                browser.find_elements(By.XPATH, '//*[@id="content"]/div[1]/div/div/button')[-1]).click().perform()
            alert = browser.switch_to.alert
            alert.accept()

        with allure.step("Поиск последнего добавленного продукта"):
            product = BasePage(
                browser).get_elements((By.CSS_SELECTOR, 'table.table.table-bordered.table-hover > tbody > tr'))[-1]
            product_name = product.find_element(by=By.CSS_SELECTOR, value='td.text-start').text

        with allure.step("Проверка последнего добавленного продукта"):
            assert product_name != 'Test_Product\nEnabled'
