from allure import title
from data import urls
from pages.login_page import LoginPage


class TestLogin:
    @title("Тест авторизации пользователя")
    def test_login(self, driver, user):
        login_page = LoginPage(driver)
        login_page.signin(user['email'], user['password'])
        assert login_page.is_logout_btn_loaded()
        assert driver.current_url == urls.RECIPES_URL

