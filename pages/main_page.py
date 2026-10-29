import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators
from urls import Urls


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_page(Urls.MAIN_PAGE_URL)

    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_page_to_load(self):
        self.wait_for_element_hide(Locators.OVERLAY, timeout=20)
        
    @allure.step("Нажать на кнопку 'Конструктор' в шапке страницы")
    def click_constructor_button(self):
        self.wait_for_page_to_load()
        self.wait_and_click(Locators.CONSTRUCTOR_BUTTON)

    @allure.step("Нажать на кнопку 'Лента Заказов' в шапке страницы")
    def click_order_feed_button(self):
        self.wait_for_page_to_load()
        self.wait_and_click(Locators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть по ингредиенту 'Краторная булка'")
    def click_on_bun_card(self):
        self.wait_for_overlay_close()
        self.scroll_to_element(Locators.BUN_CARD)
        self.wait_and_click(Locators.BUN_CARD)

    @allure.step("Дождаться отображения модального окна")
    def wait_for_modal_visible(self):
        self.wait_for_element_visible(Locators.MODAL_WINDOW)

    @allure.step("Проверить, что модальное окно открыто")
    def check_is_modal_opened(self):
        return self.check_element_is_displayed(Locators.MODAL_WINDOW)

    @allure.step("Получить название булки в модальном окне")
    def get_bun_name_in_modal(self):
        return self.get_text_of_element(Locators.MODAL_INGREDIENT_NAME)    

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click_on_element(Locators.MODAL_CLOSE_BUTTON)     

    @allure.step("Проверить, что модальное окно закрыто")
    def check_is_modal_closed(self):
        return self.wait_for_element_hide(Locators.MODAL_WINDOW)

    @allure.step("Подождать, пока оверлей исчезнет")
    def wait_for_overlay_close(self):
        self.wait_for_element_hide(Locators.OVERLAY)

    @allure.step("Получить количество в счетчике ингредиента")
    def get_ingredient_counter(self):
        count = int(self.get_text_of_element(Locators.BUN_COUNTER))
        return count

    @allure.step("Добавить булку в корзину")
    def drag_bun_to_constructor_zone(self):
        self.wait_for_element_visible(Locators.BUN_CARD)
        self.wait_for_element_visible(Locators.CONSTRUCTOR_ZONE)
        self.drag_and_drop_js(Locators.BUN_CARD, Locators.CONSTRUCTOR_ZONE)
        self.wait_for_element_visible(Locators.BUN_IN_BASKET)    

    @allure.step("Оформить заказ")
    def create_order(self):
        self.wait_for_element_hide(Locators.OVERLAY_ANIMATION)
        self.click_on_element(Locators.ORDER_BUTTON)

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.wait_for_element_hide(Locators.OVERLAY_ANIMATION)
        self.wait_for_overlay_close()
        self.wait_for_element_visible(Locators.ORDER_ID)
        self.click_on_element(Locators.MODAL_CLOSE_BUTTON)  
    
    @allure.step("Получить номер заказа в модальном окне")
    def get_order_id(self):
        self.wait_for_overlay_close()
        order_id = int(self.get_text_of_element(Locators.ORDER_ID))
        return order_id
    