from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, "a[href='/']") # кнопка "Конструктор" в шапке
    ORDER_FEED_BUTTON = (By.CSS_SELECTOR, "a[href='/feed']") # кнопка "Лента Заказов" в шапке

    # ==========================================
    INGREDIENTS_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']") # заголовок блока с ингредиентами
    CONSTRUCTOR_ZONE = (By.CSS_SELECTOR, "ul[class*='BurgerConstructor_basket__list']") # зона конструктора
    BUN_IN_BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]//span[contains(text(), 'Краторная булка N-200i')]") # Краторная булка в корзине
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]") # кнопка оформления заказа

    # ==========================================
    BUN_CARD = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')][.//p[text()='Краторная булка N-200i']]") # карточка Краторной булки
    BUN_COUNTER = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')][.//p[text()='Краторная булка N-200i']]//p[contains(@class, 'counter_counter__num')]") # счетчик Краторной булки (цифра внутри карточки)

    # ==========================================
    MODAL_WINDOW = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div") # модальное окно ингредиента
    MODAL_INGREDIENT_NAME = (By.XPATH, "//section[.//h2[text()='Детали ингредиента']]//p[contains(text(), 'Краторная булка N-200i')]") # название ингредиента в модальном окне
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//button//*[name()='path']")
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")  # оверлей за модальным окном
    OVERLAY_ANIMATION = (By.XPATH, "//img[@alt ='loading animation']")
    ORDER_ID = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title') and contains(@class, 'text_type_digits-large')]")  # номер заказа в модальном окне

    # ==========================================
