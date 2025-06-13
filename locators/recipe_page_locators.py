from selenium.webdriver.common.by import By


class RecipePageLocators:
    HEADER = (By.XPATH, '//h1[contains(text(), "Рецепты")]')
    LOGOUT_BTN = (By.XPATH, '//a[contains(text(), "Выход")]')
    CREATE_RECIPE_HEAD = (By.XPATH, '//a[contains(text(), "Создать рецепт")]')
    RECIPE_NAME = (By.XPATH, '//input[@class="styles_inputField__3eqTj"]')
    INGREDIENTS = (By.XPATH, '//input[@class="styles_inputField__3eqTj styles_ingredientsInput__1zzql"]')
    INGREDIENTS_CHOICE = (By.XPATH, '//div[@class="styles_container__3ukwm"]/div')
    INGREDIENTS_COUNT = (By.XPATH, '//input[@class="styles_inputField__3eqTj styles_ingredientsAmountValue__2matT"]')
    COOKING_TIME = (By.XPATH, '//div[@class="styles_cookingTime__2vRcp"]/div/label/input')
    DESCRIPTION = (By.XPATH, '//textarea[@class="styles_textareaField__1wfhC"]')
    CREATE_RECIPE_BTN = (By.XPATH, '//button[contains(text(), "Создать рецепт")]')
    ADD_INGREDIENT = (By.XPATH, '//div[contains(text(), "Добавить ингредиент")]')
    CHOOSE_PIC = (By.XPATH, '//input[@class="styles_fileInput__3HjP3"]')


