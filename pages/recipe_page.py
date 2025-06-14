import os

from allure import step
from selenium.webdriver.common.by import By

from locators.recipe_page_locators import RecipePageLocators
from pages.base_page import BasePage
from data import urls


class RecipePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.go_to_url(urls.RECIPES_URL)
        self.wait_for_load_element(RecipePageLocators.HEADER)

    @step('Переход на страницу создания рецепта')
    def click_to_create_recipe(self):
        self.wait_for_clickable_element(RecipePageLocators.CREATE_RECIPE_HEAD)
        self.click_element(RecipePageLocators.CREATE_RECIPE_HEAD)
        self.wait_for_load_element(RecipePageLocators.RECIPE_NAME)


    @step('Создание рецепта')
    def create_recipe(self, name, ingredient, count, time, description, pic):
        self.input_to_element(RecipePageLocators.RECIPE_NAME, name)
        self.input_to_element(RecipePageLocators.INGREDIENTS, ingredient)

        self.wait_for_clickable_element(RecipePageLocators.INGREDIENTS_CHOICE)
        self.click_element(RecipePageLocators.INGREDIENTS_CHOICE)

        self.input_to_element(RecipePageLocators.INGREDIENTS_COUNT, count)
        self.click_element(RecipePageLocators.ADD_INGREDIENT)
        self.input_to_element(RecipePageLocators.COOKING_TIME, time)
        self.input_to_element(RecipePageLocators.DESCRIPTION, description)
        self.input_to_element(RecipePageLocators.CHOOSE_PIC, os.path.abspath(pic))

        self.click_element(RecipePageLocators.CREATE_RECIPE_BTN)


    def is_recipe_card_loaded(self, name):
        locator = (By.XPATH, f'//img[@alt="{name}"]')
        self.wait_for_load_element(locator)

        return True


    def is_title_correct(self, name):
        locator = (By.XPATH, f'//h1[contains(text(), "{name}")]')
        self.wait_for_load_element(locator)

        return True




