from selenium.webdriver.common.by import By
from locators.base_page_locators import BaseLocators
from locators.question_page_locators import QuestionPageLocators
from page_object.base_page import BasePage
import allure


class FaqPage(BasePage):

    @allure.step("Тап на вопрос")
    def click_accordion(self, num):
        self.driver.find_elements(*QuestionPageLocators.question_buttons)[num].click()

    def get_question(self, question_idx):
        return self.driver.find_elements(*QuestionPageLocators.questions)[question_idx].text

    @allure.step("Получение ответа")
    def get_answer(self, num):
        return self.driver.find_elements(*QuestionPageLocators.question_answers)[num].text

    def setup_question(self, question_idx):
        self.wait_element(BaseLocators.MAIN_PAGE)
        self.scroll_down()
        self.wait_element(QuestionPageLocators.questions)
        self.click_accordion(question_idx)
        answer_elem = [By.XPATH, f"//div[@id='accordion__panel-{question_idx}']/p"]
        self.wait_element(answer_elem)