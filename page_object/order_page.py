from locators.base_page_locators import BaseLocators
from locators.order_page_locators import OrderPageLocators
from page_object.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import allure


class PageOrder(BasePage):

    @allure.step("Тап на кнопку 'Заказать' в шапке главной страницы")
    def click_order_button_on_top(self):
        self.driver.find_element(*OrderPageLocators.header_order_button).click()

    @allure.step("Тап на кнопку 'Заказать' внизу главной страницы")
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.footer_order_button).click()

    @allure.step("Выбор метро на странице заказа самоката")
    def select_metro(self, value):
        metro_value = self.driver.find_element(*OrderPageLocators.select_metro_field)
        metro_value.send_keys(value)
        metro_value.send_keys(Keys.ARROW_DOWN)
        metro_value.send_keys(Keys.RETURN)

    @allure.step("Выбор срока использования самоката")
    def set_day(self, term):
        self.driver.find_element(*OrderPageLocators.dropdown_input).click()
        self.driver.find_elements(*OrderPageLocators.dropdown_items)[term].click()

    @allure.step("Выбор цвета самоката")
    def check_scooter_color(self, color):
        color_checkboxes = self.driver.find_elements(*OrderPageLocators.scooter_colors)
        for chekbox in color_checkboxes:
            if color == chekbox.get_attribute("for"):
                chekbox.click()
                break

    @allure.step("Получение текста для сравнения к ожидаемому результату")
    def get_success_message(self):
        return self.driver.find_element(*OrderPageLocators.order_success_title).text.split("\n")[0]

    @allure.step("Тап на логотип самоката")
    def click_scooter_logo(self):
        self.click_element(OrderPageLocators.scooter_logo)

    @allure.step("Тап на логотип яндекса")
    def click_yandex_logo(self):
        self.click_element(OrderPageLocators.yandex_logo)

    @allure.step("Получение текста главной страницы Яндекс.Самокат для сравнения к ожидаемому")
    def get_scooter_main_page_text(self):
        return self.driver.find_element(*BaseLocators.MAIN_PAGE).text.split("\n")[0]

    @allure.step("Принимаем куки")
    def page_initialization(self):
        self.wait_element(BaseLocators.MAIN_PAGE)
        self.accept_cookie(OrderPageLocators.cookie_button)

    def set_user_info(self, name, second_name, address, metro, phone):
        self.wait_element(OrderPageLocators.order_page)
        self.send_key(OrderPageLocators.name_field, name)
        self.send_key(OrderPageLocators.second_name_field, second_name)
        self.send_key(OrderPageLocators.address_field, address)
        self.select_metro(metro)
        self.send_key(OrderPageLocators.phone_field, phone)
        self.click_element(OrderPageLocators.next_button)

    def set_order_info(self, order_date, term, scooter_color, comment):
        self.send_key(OrderPageLocators.date_field, order_date)
        self.send_key(OrderPageLocators.date_field, Keys.RETURN)
        self.set_day(term)
        self.check_scooter_color(scooter_color)
        self.send_key(OrderPageLocators.comment_field, comment)
        self.click_element(OrderPageLocators.order_button)
        self.wait_element(OrderPageLocators.confirm_modal)
        self.click_element(OrderPageLocators.confirm_button)