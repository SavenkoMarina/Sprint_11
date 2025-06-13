from allure import step
import data.urls
from locators.login_page_locators import LoginPageLocators

from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators



class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_url(data.urls.CREATE_ACCOUNT_URL)
        self.wait_for_load_element(RegisterPageLocators.HEADER)

    @step('Заполнение полей формы регистрации')
    def fill_registration_form(self, name, surname, username, email, password):
        self.input_to_element(RegisterPageLocators.NAME, name)
        self.input_to_element(RegisterPageLocators.SURNAME, surname)
        self.input_to_element(RegisterPageLocators.USER_NAME, username)
        self.input_to_element(RegisterPageLocators.EMAIL, email)
        self.input_to_element(RegisterPageLocators.PASSWORD, password)

    @step('Кликнуть по кнопке "Создать аккаунт"')
    def click_to_create_account_btn(self):
        self.wait_for_clickable_element(RegisterPageLocators.CREATE_BTN)
        self.click_element(RegisterPageLocators.CREATE_BTN)

    def is_login_form_loaded(self):
        self.wait_for_load_element(LoginPageLocators.LOGIN_BTN)
        return True