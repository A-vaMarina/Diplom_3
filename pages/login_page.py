import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from urls import Urls

class LoginPage(BasePage):
    @allure.step("Открыть страницу авторизации")
    def open_login_page(self):
        self.open_page(Urls.LOGIN_URL)   
    
    @allure.step("Авторизовать пользователя")
    def login(self, email, password):
        self.send_keys_to_element(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys_to_element(LoginPageLocators.PASSWORD_INPUT, password)
        self.wait_for_element_hide(MainPageLocators.OVERLAY_ANIMATION)
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)
