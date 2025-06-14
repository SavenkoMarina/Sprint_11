from allure import step
import data.urls

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.register_page_locators import RegisterPageLocators
from locators.recipe_page_locators import RecipePageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_url(data.urls.LOGIN_URL)
        self.wait_for_load_element(LoginPageLocators.HEADER)

    @step('Клик по кнопке "Создать аккаунт"')
    def click_create_account(self):
        self.wait_for_clickable_element(LoginPageLocators.CREATE_ACCOUNT_BTN)
        self.click_element(LoginPageLocators.CREATE_ACCOUNT_BTN)
        self.wait_for_load_element(RegisterPageLocators.HEADER)


    @step('Авторизация')
    def signin(self, email, password):
        self.input_to_element(LoginPageLocators.EMAIL, email)
        self.input_to_element(LoginPageLocators.PASSWORD, password)
        self.click_element(LoginPageLocators.LOGIN_BTN)
        self.wait_for_load_element(RecipePageLocators.HEADER)

    def is_logout_btn_loaded(self):
        self.wait_for_clickable_element(RecipePageLocators.LOGOUT_BTN)
        return True



