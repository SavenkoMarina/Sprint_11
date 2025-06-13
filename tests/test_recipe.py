from itertools import count

from allure import title
from pages.login_page import LoginPage
from pages.recipe_page import RecipePage


class TestRecipe:
    @title("Тест создания рецепта")
    def test_create_recipe(self, driver, user):
        login_page = LoginPage(driver)
        login_page.signin(user['email'], user['password'])

        recipe_page = RecipePage(driver)
        recipe_page.click_to_create_recipe()

        name = '2 avocado'
        ingredient = 'авокадо'
        count = 2
        time = 2
        description = 'two delicious avocado'
        pic = './data/pic.png'

        recipe_page.create_recipe(name, ingredient, count, time, description, pic)

        assert recipe_page.is_recipe_card_loaded(name)
        assert recipe_page.is_title_correct(name)

