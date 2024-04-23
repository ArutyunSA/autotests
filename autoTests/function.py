#===============================Функции для использования в тестировнии=================================================
import time
import pytest
import testit
from path import *
from coloram import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


#===================================Методы для взаимодействия со страницей==============================================
class ContractsPage:
    def __init__(self, browser):
        self.browser = browser

    #===================================Функция для клика по элементу===================================================
    def click_element(self, element):
        self.browser.find_element(*element).click()

    #======================================Функция для очистки поля=====================================================
    def clear_element(self, element):
        input_element = self.browser.find_element(*element)
        input_element.send_keys(Keys.CONTROL, 'a')
        input_element.send_keys(Keys.DELETE)

    #===================Функция для имитации очистки поля длительным нажатием клавиши DELETE============================
    def clear_delete(self, element):
        input_element = self.browser.find_element(*element)
        input_element.send_keys(Keys.BACK_SPACE * 50)

    #===================Функция для ввода текста в поле где text это текст который мы вводим============================
    def send_keys(self, element, text):
        input_element = self.browser.find_element(*element)
        input_element.send_keys(text)

    #============================Функция для просмотра текста который хранит элемент====================================
    def text(self, element):
        text_element = self.browser.find_element(*element)
        return text_element.text

    #============================Функция для просмотра значения которое хранит элемент==================================
    def atribut(self, element):
        text_element = self.browser.find_element(*element)
        return text_element.get_attribute('value')

    #====================================Функция для снятия фокуса с поля ввода=========================================
    def tab(self, element):
        input_element = self.browser.find_element(*element)
        input_element.send_keys(Keys.TAB)

    #==================================Функция для проверки доступности элемента========================================
    def enabled(self, element):
        input_element = self.browser.find_element(*element)
        return input_element.is_enabled()

    #================================Функция для проверки НЕ доступности элемента=======================================
    def disabled(self, element):
        input_element = self.browser.find_element(*element)
        return input_element.get_attribute("disabled") in ["true", "disabled"]

    #===============================Функция проверки отсутствия элемента на странице====================================
    def element_absent(self, element):
        elements = self.browser.find_elements(*element)
        return len(elements) == 0

    #========================================Функция проверки подсветки поля============================================
    def backColor(self, element):
        input_element = self.browser.find_element(*element)
        return input_element.value_of_css_property('background-color')

    #=======================================Функция проверки подсветки текста===========================================
    def textColor(self, element):
        input_element = self.browser.find_element(*element)
        return input_element.value_of_css_property('color')

    #======================================Функция для выделения текста в поле==========================================
    def contrlA(self, element):
        input_element = self.browser.find_element(*element)
        input_element.send_keys(Keys.CONTROL, 'a')

    #=================================Функция для перемещения курсора в начало строки===================================
    def home(self, element):
        input_element = self.browser.find_element(*element)
        input_element.send_keys(Keys.HOME)

    #========Функция поиска и выбора дня в календаре (вызывая заменить day на день хоторый хотим выбрать (Число))=======
    def searchDay(self, element, day):
        input_element = self.browser.find_elements(*element)
        # found_day указывает, был ли найден указанный день в календаре. Если день найден, то переменная found_day становится True, и цикл завершается
        found_day = False
        for input in input_element:
            if input.text == day:
                input.click()
                found_day = True
                true_step('ОР: Поле заполнено датой из календаря')
                break

        if not found_day:
            false_step(f"Ошибка: Не удалось найти указанный день {day} в календаре")

    #======================================Функция проверки статуса в гриде=============================================
    def getStateGrid(self, ST_element, BT_element, state):
        count = 0
        result = False
        while count < 20:
            ST = self.browser.find_elements(*ST_element)
            BT = self.browser.find_element(*BT_element)
            if len(ST) == 0:
                BT.click()
                count += 1

            elif len(ST) != 0:
                for elem in ST:
                    if elem.text == state:
                        result = True
                        true_step(f"ОР: - Элемент отображается в списке со статусом {state}")
                        break
                break
        if count == 20 and not result:
            false_step(f"Ошибка: Элемент со статусом {state} не найден после 15 кликов.")

    #=================================Функция для выбора элемента с нужным статусом в гриде=============================
    def clickStateGrid(self, ST_element, BT_element, state):
        count = 0
        result = False
        while count < 20:
            ST = self.browser.find_elements(*ST_element)
            BT = self.browser.find_element(*BT_element)
            if len(ST) == 0:
                BT.click()
                count += 1
            elif len(ST) != 0:
                for elem in ST:
                    if elem.text == state:
                        result = True
                        elem.click()
                        break
                break
        if count == 20 and not result:
            false_step(f"Ошибка: Элемент со статусом {state} не найден после 15 кликов.")

    #==========================Функция проверки отсутствия элемента в гриде=============================================
    def getNullGrid(self, ST_element, BT_element, state):
        count = 0
        result = False
        while count < 15:
            ST = self.browser.find_elements(*ST_element)
            BT = self.browser.find_element(*BT_element)
            if len(ST) == 0:
                BT.click()
                count += 1

            elif len(ST) != 0:
                for elem in ST:
                    if elem.text == state:
                        result = True
                        false_step(f"Ошибка: - Элемент отображается в списке со статусом {state}")
                        break
                break
        if count == 15 and not result:
            true_step(f"ОР: Элемент со статусом {state} не создан и не отображается в списке")

    #Прокручивает страницу вверх до тех пор, пока не будет найден указанный элемент.
    def scroll_to_element(self, element):
        scroll_step = 200  # Шаг прокрутки страницы
        max_attempts = 10  # Максимальное количество попыток скролла
        for _ in range(max_attempts):
            self.browser.execute_script("window.scrollTo(0, 0);")
            try:
                WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(element))
                break
            except TimeoutException:
                self.browser.execute_script(f"window.scrollBy(0, -{scroll_step});")
        self.browser.execute_script("window.scrollTo(0, 0);")




