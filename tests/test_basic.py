import allure

from pages.main_page import MainPage
from urls import Urls


@allure.epic("Stellar Burgers UI")
@allure.feature("Основная функциональность")
class TestBasicFunctionality:

    @allure.story("Переход по клику на 'Конструктор'")
    @allure.title("Клик по кнопке 'Конструктор' ведет на главную страницу")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.ORDER_FEED_URL)
        main_page.wait_for_url_contains("/feed")
        main_page.click_constructor_button()
        assert main_page.get_current_url() == Urls.MAIN_PAGE_URL


    @allure.story("Переход по клику на 'Лента Заказов'")
    @allure.title("Клик по кнопке 'Лента Заказов' ведет в ленту заказов")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page() 
        main_page.click_order_feed_button()
        main_page.wait_for_url_contains("/feed")
        assert "/feed" in main_page.get_current_url()


    @allure.story("Открытие всплывающего окна")
    @allure.title("При клике на ингредиент появляется окно с деталями ингредиента")
    def test_ingredient_modal_opens(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_bun_card()
        main_page.wait_for_modal_visible()
        bun_name_in_modal = main_page.get_bun_name_in_modal()
        assert "Краторная булка N-200i" in bun_name_in_modal


    @allure.story("Закрытие всплывающего окна")
    @allure.title("Всплывающее окно ингредиента закрывается кликом по крестику")
    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_on_bun_card()
        main_page.wait_for_modal_visible()
        main_page.close_modal()
        assert main_page.check_is_modal_closed()

    @allure.story("Проверка счетчика ингредиента")
    @allure.title("Счётчик ингредиента увеличивается при добавлении ингредиента в заказ")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        original_count = main_page.get_ingredient_counter()
        main_page.drag_bun_to_constructor_zone()
        final_count = main_page.get_ingredient_counter()
        assert final_count > original_count
