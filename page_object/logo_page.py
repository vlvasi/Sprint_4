from locators.base_page_locators import BaseLocators
from page_object.base_page import BasePage
import allure


class PageLogoYandex(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переключение на новый таб")
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ожидание прогрузки главной страницы Дзен(Яндекс)")
    def wait_yandex_page(self):
        self.wait_element(BaseLocators.YANDEX_SEARCH_BLOCK)

    @allure.step("Получение название поля поиска")
    def get_yandex_search_label(self):
        return self.driver.find_element(*BaseLocators.YANDEX_SEARCH_BLOCK).get_attribute("aria-label")
