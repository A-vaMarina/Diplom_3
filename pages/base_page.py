import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента {locator}")
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Подождать, пока элемент {locator} станет кликабельным")
    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Кликнуть по элементу {locator}")
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Дождаться кликабельности и кликнуть по элементу {locator}")
    def wait_and_click(self, locator, timeout=10):
        self.wait_for_element_clickable(locator, timeout).click()

    @allure.step("Получить текст элемента {locator}")
    def get_text_of_element(self, locator, timeout=10):
        return self.wait_for_element_visible(locator, timeout).text

    @allure.step("Проверить, что элемент {locator} отображается")
    def is_element_visible(self, locator, timeout=5):
        return self.wait_for_element_visible(locator, timeout).is_displayed()

    @allure.step("Подождать, пока элемент {locator} скроется")
    def wait_for_element_hide(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Открыть страницу {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Получить URL текущей страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Скролл до элемента {locator}")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Перетащить элемент {source_locator} в {target_locator} через JS")
    def drag_and_drop_js(self, source_locator, target_locator):
        """
        Реализация Drag-and-Drop через JS-события.
        Спасает от багов Firefox, где ActionChains работает нестабильно.
        """
        source = self.wait_for_element_visible(source_locator)
        target = self.wait_for_element_visible(target_locator)

        # Выполняем цепочку событий HTML5 DnD
        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];
            
            const dataTransfer = new DataTransfer();
            
            const dragStartEvent = new DragEvent('dragstart', {bubbles: true, cancelable: true, dataTransfer: dataTransfer});
            const dragOverEvent = new DragEvent('dragover', {bubbles: true, cancelable: true, dataTransfer: dataTransfer});
            const dropEvent = new DragEvent('drop', {bubbles: true, cancelable: true, dataTransfer: dataTransfer});
            const dragEndEvent = new DragEvent('dragend', {bubbles: true, cancelable: true, dataTransfer: dataTransfer});
            
            source.dispatchEvent(dragStartEvent);
            target.dispatchEvent(dragOverEvent);
            target.dispatchEvent(dropEvent);
            source.dispatchEvent(dragEndEvent);
        """, source, target)
        