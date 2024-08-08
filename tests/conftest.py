import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--base-url", default="http://localhost:80")
    parser.addoption("--url-catalog", default="http://localhost:80/en-gb/catalog")
    parser.addoption("--url-product", default="http://localhost:80/en-gb/product")
    parser.addoption("--url-administration", default="http://localhost:80/administration")
    parser.addoption("--url-registration", default="http://localhost:80/index.php?route=account/register")
    parser.addoption("--opencart-username", default="user")
    parser.addoption("--opencart-password", default="bitnami")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture(scope="session")
def url_catalog(request):
    return request.config.getoption("--url-catalog")


@pytest.fixture(scope="session")
def url_product(request):
    return request.config.getoption("--url-product")


@pytest.fixture(scope="function")
def login_administration(request):
    return {'login': request.config.getoption("--opencart-username"),
            'password': request.config.getoption("--opencart-password")}


@pytest.fixture(scope="session")
def url_administration(request):
    return request.config.getoption("--url-administration")


@pytest.fixture(scope="session")
def url_registration(request):
    return request.config.getoption("--url-registration")


@pytest.fixture
def browser(request):
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

    return driver
