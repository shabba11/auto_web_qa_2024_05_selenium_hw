import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page_objects.administration_page import AdministrationPage as AP
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from page_objects.registration_page import RegistrationPage as RP
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--base-url", default="http://localhost:8092")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--bv")
    parser.addoption("--local", default=False)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'

@pytest.fixture
def browser(request):
    local = request.config.getoption("--local")
    url = request.config.getoption("--base-url")
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    logs = request.config.getoption("--logs")
    mobile = request.config.getoption("--mobile")

    executor_url = f"http://{executor}:4444/wd/hub"

    if browser == "chrome":
        options = ChromeOptions()
        service = Service()
        if local:
            driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        options = FirefoxOptions()
        if local:
            driver = webdriver.Firefox()
    elif browser == "safari":
        options = SafariOptions()
        if local:
            driver = webdriver.Safari()
    else:
        raise Exception("Driver not supported")

    caps = {
        "browserName": browser,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "name": request.node.name,
            "screenResolution": "1280x2000",
            "enableLog": logs,
            "timeZone": "Europe/Moscow",
            "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]
        },
        "acceptInsecureCerts": True,
    }

    for k, v in caps.items():
        options.set_capability(k, v)

    if not local:
        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )

    if not mobile:
        driver.maximize_window()

    driver.get(url)

    def finalizer():
        driver.quit()

    request.addfinalizer(finalizer)

    return driver


@pytest.fixture(scope="function")
def login_administration(request, browser):
    AP(browser)

    with allure.step("Ввод Username"):
        username = BasePage(browser).get_element((By.ID, "input-username"))
        username.send_keys(request.config.getoption("--opencart-username"))

    with allure.step("Ввод Password"):
        password = BasePage(browser).get_element((By.ID, "input-password"))
        password.send_keys(request.config.getoption("--opencart-password"))

    with allure.step("Нажатие кнопки Login"):
        BasePage(browser).get_element((By.CSS_SELECTOR, "button.btn.btn-primary")).click()

    with allure.step("Проверка открытия страницы пользователя"):
        BasePage(browser).get_element((By.ID, "nav-profile"))


@pytest.fixture(scope="function")
def user_registration(request, browser):
    emails = []

    def registration(firstname, lastname, e_mail, password):
        RP(browser)

        with allure.step("Ввод данных для регистрации"):
            BasePage(browser).input_value((By.ID, 'input-firstname'), texts=firstname)
            BasePage(browser).input_value((By.ID, "input-lastname"), texts=lastname)
            BasePage(browser).input_value((By.ID, "input-email"), texts=e_mail)
            BasePage(browser).input_value((By.ID, "input-password"), texts=password)

        with allure.step("Нажатие кнопки регистрации пользователя"):
            BasePage(browser).click((By.XPATH, '//*[@id="form-register"]/div/div/input'))
            BasePage(browser).click((By.XPATH, '//*[@id="form-register"]/div/button'))

        with allure.step("Проверка успешной регистрации"):
            BasePage(browser).get_element((By.PARTIAL_LINK_TEXT, 'Your Account Has Been Created!'))

        emails.append(e_mail)

    yield registration

    with allure.step("Удаление созданного пользователя"):

        with allure.step("Открытие админской страницы"):
            browser.get(url=request.config.getoption("--base-url") + AP.URL_ADMINISTRATION)

        with allure.step("Ввод логина и пароля"):
            username = BasePage(browser).get_element((By.ID, "input-username"))
            username.send_keys(request.config.getoption("--opencart-username"))

            password = BasePage(browser).get_element((By.ID, "input-password"))
            password.send_keys(request.config.getoption("--opencart-password"))

        with allure.step("Удаление пользователя"):
            BasePage(browser).get_element((By.CSS_SELECTOR, "button.btn.btn-primary")).click()
            BasePage(browser).click((By.XPATH, '//*[@id="menu-customer"]'))
            BasePage(browser).click((By.XPATH, '//*[@id="collapse-5"]/li[1]/a'))

            BasePage(browser).click((By.XPATH, '//*[@id="form-customer"]/div[1]/table/thead/tr/td[1]/input'))
            BasePage(browser).click((By.XPATH, '//*[@id="content"]/div[1]/div/div/button[2]'))

            alert = browser.switch_to.alert
            alert.accept()
