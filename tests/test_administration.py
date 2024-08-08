from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAdministration:

    def test_administration_locate_username(self, browser, url_administration):
        browser.get(url_administration)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "input-username")))

    def test_administration_locate_password(self, browser, url_administration):
        browser.get(url_administration)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "input-password")))

    def test_administration_locate_button_password(self, browser, url_administration):
        browser.get(url_administration)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "button.btn.btn-primary")))

    def test_administration_locate_card_header(self, browser, url_administration):
        browser.get(url_administration)
        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((
            By.CLASS_NAME, "card-header")))

    def test_administration_login_and_logout(self, browser, url_administration, login_administration):
        browser.get(url_administration)

        username = browser.find_element(value="input-username")
        username.send_keys(login_administration['login'])

        password = browser.find_element(value="input-password")
        password.send_keys(login_administration['password'])

        browser.find_element(by=By.CSS_SELECTOR, value="button.btn.btn-primary").click()

        WebDriverWait(driver=browser, timeout=1).until(EC.visibility_of_element_located((By.ID, "nav-profile")))

        browser.find_element(by=By.CSS_SELECTOR, value="i.fa-solid.fa-sign-out").click()

        assert browser.current_url == "http://localhost/administration/index.php?route=common/login"
