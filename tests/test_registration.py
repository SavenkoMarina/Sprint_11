from allure import title
from data import urls
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from helpers import (
    generate_email,
    generate_random_string
)


class TestRegistration:
    @title("Переход по клику на 'Создание аккаунта'")
    def test_click_to_registration(self, driver):
        login_page = LoginPage(driver)
        login_page.click_create_account()

        assert driver.current_url == urls.CREATE_ACCOUNT_URL

    @title("Тест регистрации пользователя")
    def test_account_registration(self, driver):
        reg_page = RegistrationPage(driver)

        name = generate_random_string(5)
        surname = generate_random_string(5)
        username = generate_random_string(6)
        email = generate_email()
        password = generate_random_string(10)

        reg_page.fill_registration_form(name, surname, username, email, password)
        reg_page.click_to_create_account_btn()

        assert reg_page.is_login_form_loaded()
        assert driver.current_url == urls.LOGIN_URL

