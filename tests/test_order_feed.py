import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.epic("Stellar Burgers UI")
@allure.feature("Раздел «Лента заказов»")
class TestOrderFeed:

    @allure.story("Счётчик «Выполнено за всё время»")
    @allure.title("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_orders_counter_increases(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        order_page = OrderFeedPage(authorized_driver)

        main_page.click_order_feed_button()
        order_page.wait_for_order_page_loaded()
        count_before = order_page.get_total_orders_count()
        main_page.open_main_page()
        main_page.wait_for_overlay_close()
        main_page.create_order_and_get_id()
        main_page.click_order_feed_button()
        order_page.wait_for_order_page_loaded()
        count_after = order_page.get_total_orders_count()

        assert count_after > count_before, f"Счетчик не увеличился. Было: {count_before}, стало: {count_after}"


    @allure.story("Счётчик «Выполнено за сегодня»")
    @allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increases(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        order_page = OrderFeedPage(authorized_driver)

        main_page.click_order_feed_button()
        order_page.wait_for_order_page_loaded()
        count_before = order_page.get_today_orders_count()
        main_page.open_main_page()
        main_page.wait_for_overlay_close()
        main_page.create_order_and_get_id()
        main_page.click_order_feed_button()
        order_page.wait_for_order_page_loaded()
        count_after = order_page.get_today_orders_count()

        assert count_after > count_before, f"Счетчик не увеличился. Было: {count_before}, стало: {count_after}"


    @allure.story("Раздел «В работе»")
    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_appears_in_progress(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        order_page = OrderFeedPage(authorized_driver)

        order_number = main_page.create_order_and_get_id()
        main_page.click_order_feed_button()
        order_page.wait_for_order_page_loaded()
        order_page.wait_for_orders_in_progress()
        in_progress_orders = order_page.get_in_progress_order_numbers()
        
        assert order_number in in_progress_orders, f"Заказа {order_number} нет в разделе 'В работе'. Список: {in_progress_orders}"
