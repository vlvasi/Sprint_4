from selenium.webdriver.common.by import By


class Locators:
    # Вопрос "Сколько это стоит? И как оплатить?"
    COST_FIELD = (By.XPATH, '//*[@id = "accordion__heading-0"]')
    # Ответ на вопрос "Сколько это стоит? И как оплатить?"
    COST_FIELD_ANSWER = (By.XPATH, '//*[contains(text(), "Сутки — 400 рублей. Оплата курьеру — наличными или картой")]')
    # Вопрос "Хочу сразу несколько самокатов! Так можно?"
    SEVERAL_SCOOTERS = (By.XPATH, '//*[@id="accordion__heading-1"]')
    # Ответ на вопрос "Хочу сразу несколько самокатов! Так можно?"
    SEVERAL_SCOOTERS_ANSWER = (By.XPATH, '//*[contains(text(), "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.")]')
    # Вопрос "Как рассчитывается время аренды?"
    DRIVING_TIME = (By.XPATH, '//*[@id="accordion__heading-2"]')
    # Ответ на вопрос "Как рассчитывается время аренды?"
    DRIVING_TIME_ANSWER = (By.XPATH, '//*[contains(text(), "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]')
    # Вопрос "Можно ли заказать самокат прямо на сегодня?"
    ORDER_TODAY = (By.XPATH, '//*[@id="accordion__heading-3"]')
    # Ответ на вопрос "Можно ли заказать самокат прямо на сегодня?"
    ORDER_TODAY_ANSWER = (By.XPATH, '//*[contains(text(), "Только начиная с завтрашнего дня. Но скоро станем расторопнее."]')
    # Вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    EXTEND_RETURN_ORDER = (By.XPATH, '//*[@id="accordion__heading-4"]')
    # Ответ на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    EXTEND_RETURN_ORDER_ANSWER = (By.XPATH, '//*[contains(text(),"Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]')
    #  Вопрос "Вы привозите зарядку вместе с самокатом?"
    CHARGER_WITH_SCOOTER = (By.XPATH, '//*[@id="accordion__heading-5"]')
    # Ответ на вопрос "Вы привозите зарядку вместе с самокатом?"
    CHARGER_WITH_SCOOTER = (By.XPATH, '//*[contains(text(),"Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."]')
    #  Вопрос "Можно ли отменить заказ?"
    CANCEL_THE_ORDER = (By.XPATH, '//*[@id="accordion__heading-6"]')
    # Ответ на вопрос "Можно ли отменить заказ?"
    CANCEL_THE_ORDER_ANSWER = (By.XPATH, '//*[contains(text(),"Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]')
    #  Вопрос "Я жизу за МКАДом, привезёте?"
    CUSTOMER_IS_BEYOND_THE_MKAD = (By.XPATH, '//*[@id="accordion__heading-7"]')
    # Ответ на вопрос "Я жизу за МКАДом, привезёте?"
    CUSTOMER_IS_BEYOND_THE_MKAD_ANSWER = (By.XPATH, '//*[contains(text(),"Да, обязательно. Всем самокатов! И Москве, и Московской области."]')
    # Кнопка Заказать в верхней части экрана
    ORDER_BUTTON_ON_TOP = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    # Поле Имя
    NAME = (By.XPATH, "//label[text() = 'Имя']/parent::div/input")
    # Поле Фамилия
    SURNAME = (By.XPATH, '//label[text() = "Фамилия"]/parent::div/input')
    # Поле Адрес: куда привезти
    ADRESS = (By.XPATH, '//label[text() = "Адрес: куда привезти заказ"]/parent::div/input')
    # Поле Станция метро
    METRO_STATION = (By.XPATH, '//label[text() = "Станция метро"]/parent::div/input')
    # Поле Телефон: на него позвонит курьер
    NUMBER = (By.XPATH, '//label[text() = "Телефон: на него позвонит курьер"]/parent::div/input')
    #  Кнопка Далее
    NEXT_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    # Поле Когда привезти самокат
    DELIVERY_DATE = (By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN react-datepicker-ignore-onclickoutside"]')
    # Поле Срок аренды
    DELIVERY_TIME = (By.XPATH, '//div[@class="Dropdown-control"]')
    # Поле Цвет самоката
    SCOOTER_COLOUR_BLACK = (By.ID, 'black')
    # Кнопка Заказать на экране Про аренду
    ORDER_BUTTON_ON_RENT_SCREEN = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    # Поп-ап "Хотите оформить заказ?"
    POP_UP_PLACE_AN_ORDER = (By.XPATH, '//div[@class = "Order_ModalHeader__3FDaJ"]')
    # Кнопка "ДА" на поп-апе
    YES_BUTTON = (By.XPATH, '//*[contains(text(),"Да"]/parent::div/button')
    # Поп-ап "Заказ оформлен"
    THE_ORDER_HAS_BEEN_PLACED = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')
    # Кнопка Просмотреть заказ на поп-апе
    VIEW_ORDER_BUTTON = (By.XPATH, '//*[contains(text(),"Посмотреть статус"]/parent::div/button')
    # Логотип Самоката
    SCOOTER_IMG = (By.XPATH, '//img[@src="/assets/scooter.svg"]')
    # Кнопка Заказать в верхней части экрана
    ORDER_BUTTON_DOWN_BELOW = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]/parent::div/button')

