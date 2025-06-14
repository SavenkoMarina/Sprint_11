import os

import pytest

from selenium import webdriver

from helpers import generate_random_string, generate_email
from pages.registration_page import RegistrationPage


@pytest.fixture
def driver():
    path = os.environ.get("REMOTE_BROWSER_PATH")
    if path:
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote(command_executor=path, options=options)
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def user(driver):
    reg_page = RegistrationPage(driver)

    name = generate_random_string(5)
    surname = generate_random_string(5)
    username = generate_random_string(6)
    email = generate_email()
    password = generate_random_string(10)

    reg_page.fill_registration_form(name, surname, username, email, password)
    reg_page.click_to_create_account_btn()

    return {
        "email": email,
        "password": password
    }

