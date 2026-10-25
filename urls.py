class Urls:
    # ---------- Общее ----------
    BASE_URL = "https://stellarburgers.education-services.ru"

    # ---------- UI-страницы ----------
    ORDER_FEED_URL = f"{BASE_URL}/feed"       # Лента заказов
    CONSTRUCTOR_URL = f"{BASE_URL}/"          # Конструктор

    # ---------- API-эндпоинты ----------
    REGISTER_USER_URL = f"{BASE_URL}/api/auth/register"   # POST регистрация пользователя
    LOGIN_USER_URL = f"{BASE_URL}/api/auth/login"         # POST логин пользователя
    USER_URL = f"{BASE_URL}/api/auth/user"                # DELETE удаление пользователя
    