import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page_objects.administration_page import AdministrationPage as AP
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--base-url", default="http://localhost:80")
    parser.addoption("--opencart-username", default="user")
    parser.addoption("--opencart-password", default="bitnami")


@pytest.fixture
def browser(request):
    url = request.config.getoption("--base-url")
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")

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

    request.addfinalizer(driver.quit)

    driver.maximize_window()

    driver.get(url)

    return driver


@pytest.fixture(scope="function")
def login_administration(request, browser):
    AP(browser)

    username = BasePage(browser).get_element((By.ID, "input-username"))
    username.send_keys(request.config.getoption("--opencart-username"))

    password = BasePage(browser).get_element((By.ID, "input-password"))
    password.send_keys(request.config.getoption("--opencart-password"))

    BasePage(browser).get_element((By.CSS_SELECTOR, "button.btn.btn-primary")).click()

    BasePage(browser).get_element((By.ID, "nav-profile"))
