import pytest
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from urls import Urls
from generators import generate_user_data
from pages.login_page import LoginPage


# ---------------- CLI-опции ----------------
def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск браузера без открытия окна",
    )

# ---------------- Драйвер ----------------
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    driver.maximize_window()
    yield driver
    driver.quit()

# ---------------- API: Регистрация и удаление пользователя ----------------
@pytest.fixture
def registered_user():
    payload = generate_user_data()
    response = requests.post(Urls.REGISTER_USER_URL, json=payload)
    
    if response.status_code != 200:
        raise Exception(f"Не удалось зарегистрировать пользователя: {response.status_code} {response.text}")
    
    access_token = response.json().get('accessToken')
    
    yield payload
    
    if access_token:
        requests.delete(Urls.USER_URL, headers={'Authorization': access_token})

# ---------------- UI: Авторизация пользователя ----------------
@pytest.fixture
def authorized_driver(driver, registered_user):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(registered_user["email"], registered_user["password"])
    yield driver
