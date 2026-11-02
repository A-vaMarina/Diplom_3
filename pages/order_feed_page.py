import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Locators


class OrderFeedPage(BasePage):

    @allure.step("Дождаться загрузки страницы 'Лента заказов'")
    def wait_for_order_page_loaded(self):
        self.wait_for_url_contains("/feed")
        self.wait_for_element_visible(Locators.ORDER_TITLE) 

    @allure.step("Подождать исчезновения оверлея")
    def wait_for_overlay_close(self):
        self.wait_for_element_hide(Locators.OVERLAY, timeout=15)

    @allure.step("Получить количество заказов 'Выполнено за всё время'")
    def get_total_orders_count(self):
        self.wait_for_overlay_close()
        self.scroll_to_element(Locators.TOTAL_ORDERS)
        return int(self.get_text_of_element(Locators.TOTAL_ORDERS))

    @allure.step("Получить количество заказов 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        self.wait_for_overlay_close()
        self.scroll_to_element(Locators.TODAY_ORDERS)
        return int(self.get_text_of_element(Locators.TODAY_ORDERS))

    @allure.step("Получить список номеров заказов в разделе 'В работе'")
    def get_in_progress_order_numbers(self):
        self.wait_for_overlay_close()
        self.scroll_to_element(Locators.IN_PROGRESS_ORDERS)
        self.wait_for_element_visible(Locators.IN_PROGRESS_ORDERS)
        elements = self.driver.find_elements(*Locators.IN_PROGRESS_ORDERS)
        return [int(el.text.strip()) for el in elements if el.text.strip().isdigit()]

    @allure.step("Подождать появления заказов в разделе 'В работе'")
    def wait_for_orders_in_progress(self):
        self.wait_for_attribute(Locators.IN_PROGRESS_ORDERS, 'class', 'text_type_digits-default', timeout=10)
