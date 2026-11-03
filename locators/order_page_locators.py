from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_TITLE = (By.XPATH, "//h1[text()='Лента заказов']") # заголовок страницы заказов
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")  # счётчик «Выполнено за всё время»
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")  # счётчик «Выполнено за сегодня»

    # ==========================================
    IN_PROGRESS_ORDERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li") # номер заказа в разделе «В работе»
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")  # оверлей за модальным окном
