from page_object.faq_page import FaqPage
from data import FaqPageData
import pytest
import allure


@allure.feature("Проверка вопросов на главной странице.")
class TestFaq:

    @allure.title("Проверка ответов в разделе 'Вопросы о важном'")
    @pytest.mark.parametrize('question_idx', [i for i in range(8)])
    def test_questions(self, driver, question_idx):
        question_page = FaqPage(driver)
        question_page.setup_question(question_idx)
        expected_result = FaqPageData.question_and_answers_dict[question_page.get_question(question_idx)]
        actual_result = question_page.get_answer(question_idx)
        assert actual_result == expected_result, f"Текст отличается. Должно быть: {expected_result}"
