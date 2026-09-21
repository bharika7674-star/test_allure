import allure
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    # Actions
    @allure.step("Enter username")
    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    @allure.step("Click login button")
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

