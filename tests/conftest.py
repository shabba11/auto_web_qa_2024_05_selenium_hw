import datetime
import json

import pytest
import os
import logging
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page_objects.administration_page import AdministrationPage as AP
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from page_objects.registration_page import RegistrationPage as RP


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--base-url", default="http://localhost:80")
    parser.addoption("--opencart-username", default="user")
    parser.addoption("--opencart-password", default="bitnami")
    parser.addoption("--log_level", action="store", default="INFO")


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
    url = request.config.getoption("--base-url")
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser == "chrome":
        service = Service()
        driver = webdriver.Chrome(service=service)
    elif browser == "yandex":
        options = webdriver.ChromeOptions()
        service = Service(executable_path=os.path.join(drivers, "yandexdriver"))
        options.binary_location = "/usr/bin/yandex-browser"
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception("Driver not supported")

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON)

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    def fin():
        driver.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    driver.maximize_window()

    driver.get(url)

    yield driver

    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            name="page_source",
            body=driver.page_source,
            attachment_type=allure.attachment_type.HTML
        )

    driver.quit()


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
