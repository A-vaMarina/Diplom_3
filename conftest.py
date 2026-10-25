import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from urls import Urls
from helpers import register_new_user
from auth_methods import AuthMethods


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
            # В headless Firefox вьюпорт по умолчанию крошечный,
            # maximize_window() там не работает — задаем размер явно.
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    driver.maximize_window()
    yield driver
    driver.quit()


# ---------------- API: пользователь ----------------
@pytest.fixture
def cleanup_user():
    """Копит токены и удаляет пользователей после теста."""
    tokens = []
    yield tokens
    for token in filter(None, tokens):
        AuthMethods.delete_user(token)

@pytest.fixture
def registered_user(cleanup_user):
    """Создает пользователя через API и отдает его данные + accessToken."""
    user = register_new_user()
    cleanup_user.append(user["accessToken"])
    return user

@pytest.fixture
def authorized_user(registered_user):
    """Логинит пользователя через API и отдает accessToken от логина."""
    payload = {
        "email": registered_user["email"],
        "password": registered_user["password"],
    }
    response = AuthMethods.login_user(payload)
    assert response.status_code == 200, (
        f"Не удалось авторизовать пользователя: "
        f"{response.status_code} {response.text}"
    )
    return response.json()["accessToken"]


# ---------------- UI: драйвер с залогиненным пользователем ----------------
@allure.step("Подготовить браузер с залогиненным пользователем")
@pytest.fixture
def authorized_driver(driver, authorized_user):
    """
    Отдает драйвер, в котором уже залогинен пользователь, созданный через API.
    Пользователь удаляется автоматически (cleanup_user).
    """
    driver.get(Urls.BASE_URL)
    driver.execute_script(
        f"window.localStorage.setItem('accessToken', '{authorized_user}');"
    )
    driver.refresh()
    yield driver
    