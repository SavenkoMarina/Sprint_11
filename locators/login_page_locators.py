from selenium.webdriver.common.by import By


class LoginPageLocators:
    HEADER = (By.XPATH, '//h1[contains(text(), "Войти на сайт")]')
    CREATE_ACCOUNT_BTN = (By.XPATH, '//a[contains(text(), "Создать аккаунт")]')
    LOGIN_BTN = (By.XPATH, '//button[contains(text(), "Войти")]')
    EMAIL = (By.XPATH, '//input[@name="email"]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')