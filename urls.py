class Urls:

    BASE_URL = "https://qa-stellarburgers.education-services.ru"
    
    MAIN_PAGE_URL = f"{BASE_URL}/"            # Главная страница
    ORDER_FEED_URL = f"{BASE_URL}/feed"       # Лента заказов
    LOGIN_URL = f"{BASE_URL}/login"           # Страница авторизации

    # ---------- API-эндпоинты ----------
    REGISTER_USER_URL = f"{BASE_URL}/api/auth/register"   # POST регистрация пользователя
    LOGIN_USER_URL = f"{BASE_URL}/api/auth/login"         # POST логин пользователя
    USER_URL = f"{BASE_URL}/api/auth/user"                # DELETE удаление пользователя
    