from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from venv.locators import Locators


class TestListOfQuestions:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru'


    def test_faq_how_much_cost(self, driver):
        driver.find_element(*Locators.COST_FIELD).click()
        find_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(*Locators.COST_FIELD_ANSWER)).text()
        assert find_text

    def test_faq_several_scooters(self, driver):
        driver.find_element(*Locators.SEVERAL_SCOOTERS).click()
        find_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(*Locators.SEVERAL_SCOOTERS_ANSWER)).text()
        assert find_text

    def test_faq_driving_time(self, driver):
        driver.find_element(*Locators.DRIVING_TIME).click()
        find_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(*Locators.DRIVING_TIME_ANSWER)).text()
        assert find_text
    def test_faq_order_today(self, driver):
        driver.find_element(*Locators.ORDER_TODAY).click()
        find_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(*Locators.ORDER_TODAY_ANSWER)).text()
        assert find_text

   def test_faq_extend_or_return(self, driver):
        driver.find_element(*Locators.EXTEND_RETURN_ORDER).click()
        find_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(*Locators.EXTEND_RETURN_ORDER_ANSWER)).text()
        assert find_text

    def test_faq_charger_with_scooter(self, driver):
        driver.find_element(*Locators.CHARGER_WITH_SCOOTER).click()
        find_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(*Locators.CHARGER_WITH_SCOOTER)).text()
        assert find_text

    def test_cancel_the_order(self, driver):
        driver.find_element(*Locators.CANCEL_THE_ORDER).click()
        find_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(*Locators.CANCEL_THE_ORDER_ANSWER)).text()
        assert find_text

    def test_customer_is_beyond_the_MKAD(self, driver):
        driver.find_element(*Locators.CUSTOMER_IS_BEYOND_THE_MKAD).click()
        find_text = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(*Locators.CUSTOMER_IS_BEYOND_THE_MKAD_ANSWER)).text()
        assert find_text

class TestOrderScooter:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru'

    def test_order_button_on_top(self, driver):
        driver.find_element(*Locators.ORDER_BUTTON_ON_TOP).click()
        driver.get('https://qa-scooter.praktikum-services.ru/order')
        driver.find_element(*Locators.NAME).send_keys('Влада')
        driver.find_element(*Locators.SURNAME).send_keys('Васильева')
        driver.find_element(*Locators.ADRESS).send_keys('Кутузовский пр. 57')
        driver.find_element(*Locators.METRO_STATION).send_keys('Пионерская')
        driver.find_element(*Locators.NUMBER).send_keys('+79853335463')
        driver.find_element(*Locators.NEXT_BUTTON).click()
        driver.find_element(*Locators.DELIVERY_DATE).send_keys('28.06.2023')
        driver.find_element(*Locators.DELIVERY_TIME).click('двое суток')
        driver.find_element(*Locators.SCOOTER_COLOUR_BLACK).click()
        driver.find_element(*Locators.ORDER_BUTTON_ON_RENT_SCREEN).click()
        driver.find_element(*Locators.POP_UP_PLACE_AN_ORDER).click(*Locators.YES_BUTTON)
        driver.find_element(*Locators.THE_ORDER_HAS_BEEN_PLACED).click(*Locators.VIEW_ORDER_BUTTON)
        driver.find_element(*Locators.SCOOTER_IMG).click()
        driver.get('https://qa-scooter.praktikum-services.ru/')

    def test_order_button_down_bellow(self, driver):
        driver.find_element(*Locators.ORDER_BUTTON_DOWN_BELOW).click()
        driver.get('https://qa-scooter.praktikum-services.ru/order')
        driver.find_element(*Locators.NAME).send_keys('Влада')
        driver.find_element(*Locators.SURNAME).send_keys('Васильева')
        driver.find_element(*Locators.ADRESS).send_keys('Кутузовский пр. 57')
        driver.find_element(*Locators.METRO_STATION).send_keys('Пионерская')
        driver.find_element(*Locators.NUMBER).send_keys('+79853335463')
        driver.find_element(*Locators.NEXT_BUTTON).click()
        driver.find_element(*Locators.DELIVERY_DATE).send_keys('28.06.2023')
        driver.find_element(*Locators.DELIVERY_TIME).click('двое суток')
        driver.find_element(*Locators.SCOOTER_COLOUR_BLACK).click()
        driver.find_element(*Locators.ORDER_BUTTON_ON_RENT_SCREEN).click()
        driver.find_element(*Locators.POP_UP_PLACE_AN_ORDER).click(*Locators.YES_BUTTON)
        driver.find_element(*Locators.THE_ORDER_HAS_BEEN_PLACED).click(*Locators.VIEW_ORDER_BUTTON)
        driver.find_element(*Locators.SCOOTER_IMG).click()
        driver.get('https://qa-scooter.praktikum-services.ru/')











