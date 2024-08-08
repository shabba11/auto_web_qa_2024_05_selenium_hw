from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:
    def test_registration_input_firstname(self, browser, url_registration):
        browser.get(url_registration)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "input-firstname")))

    def test_registration_input_lastname(self, browser, url_registration):
        browser.get(url_registration)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "input-lastname")))

    def test_registration_input_email(self, browser, url_registration):
        browser.get(url_registration)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "input-email")))

    def test_registration_input_password(self, browser, url_registration):
        browser.get(url_registration)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "input-password")))

    def test_registration_input_newsletter(self, browser, url_registration):
        browser.get(url_registration)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "input-newsletter")))
