from selenium.webdriver.common.by import By


class RegisterPageLocators:
    HEADER = (By.XPATH, '//h1[contains(text(), "Регистрация")]')
    NAME = (By.XPATH, '//input[@name="first_name"]')
    SURNAME = (By.XPATH, '//input[@name="last_name"]')
    USER_NAME = (By.XPATH, '//input[@name="username"]')
    EMAIL = (By.XPATH, '//input[@name="email"]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')
    CREATE_BTN = (By.XPATH, '//button[contains(text(), "Создать аккаунт")]')
