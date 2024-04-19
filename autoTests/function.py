#===========================Функции для использования в тестировнии ТАП=================================================
import time
import pytest
import testit
from path import *
from coloram import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver




#===============Функция проверки заполнения обязательных полей формы назначения=========================================
def OB_form_purpose():
    f = ContractsPage(browser)
    all_fields_filled = True

    if f.atribut(FD_drug) == '':
        false_step('Ошибка: Поле "Препарат" не заполнено')
        all_fields_filled = False
    if f.atribut(FD_mnn) == '':
        false_step('Ошибка: Поле "МНН" не заполнено')
        all_fields_filled = False
    if f.atribut(FD_trn) == '':
        false_step('Ошибка: Поле "Торговое" не заполнено')
        all_fields_filled = False
    if f.atribut(FD_dosageform) == '':
        false_step('Ошибка: Поле "Лекарственная форма" не заполнено')
        all_fields_filled = False
    if f.atribut(FD_dose) == '':
        false_step('Ошибка: Поле "Дозировка" не заполнено')
        all_fields_filled = False
    if f.atribut(FD_singleDose) == '':
        false_step('Ошибка: Поле "Разовая доза" не заполнено')
        all_fields_filled = False
    if f.atribut(FD_unit) == '':
        false_step('Ошибка: Поле "Ед. измерения" не заполнено')
        all_fields_filled = False
    if f.atribut(FD_onceADay) == '':
        false_step('Ошибка: Поле "Раз в день" не заполнено')
        all_fields_filled = False
    if f.atribut(FD_countDay) == '':
        false_step('Ошибка: Поле "Количество дней" не заполнено')
        all_fields_filled = False
    if f.atribut(FD_perCourse) == '':
        false_step('Ошибка: Поле "Количество на курс" не заполнено')
        all_fields_filled = False
    if f.atribut(FD_receptionMethod) == '':
        false_step('Ошибка: Поле "Способ введения" не заполнено')
        all_fields_filled = False
    if f.atribut(FD_way) == '':
        false_step('Ошибка: Поле "Путь введени" не заполнено')
        all_fields_filled = False
    if f.atribut(FD_details) == '':
        false_step('Ошибка: Поле "Детализация" не заполнено')
        all_fields_filled = False
    if all_fields_filled:
        true_step('ОР: Обязательные поля заполнены')


#================================Методы для взаимодействия со страницей ТАП=============================================
class ContractsPage:
    def __init__(self, browser):
        self.browser = browser

    #Функция для клика по элементу
    def click_element(self, element):
        self.browser.find_element(*element).click()

    #Функция для очистки поля
    def clear_element(self, element):
        input_element = self.browser.find_element(*element)
        input_element.send_keys(Keys.CONTROL, 'a')
        input_element.send_keys(Keys.DELETE)

    #Функция для ввода текста в поле где text это текст который мы вводим
    def send_keys(self, element, text):
        input_element = self.browser.find_element(*element)
        input_element.send_keys(text)

    #Функция для просмотра текста который хранит элемент
    def text(self, element):
        text_element = self.browser.find_element(*element)
        return text_element.text

    #Функция для просмотра значения которое хранит элемент
    def atribut(self, element):
        text_element = self.browser.find_element(*element)
        return text_element.get_attribute('value')

    #Функция для снятия фокуса с поля ввода
    def tab(self, element):
        input_element = self.browser.find_element(*element)
        input_element.send_keys(Keys.TAB)

    #Функция для проверки доступности элемента
    def enabled(self, element):
        input_element = self.browser.find_element(*element)
        return input_element.is_enabled()

    #Функция для проверки НЕ доступности элемента
    def disabled(self, element):
        input_element = self.browser.find_element(*element)
        return not input_element.is_enabled

    #Функция проверки отсутствия элемента на странице
    def element_absent(self, element):
        elements = self.browser.find_elements(*element)
        return len(elements) == 0

    #Функция проверки подсветки поля
    def backColor(self, element):
        input_element = self.browser.find_element(*element)
        return input_element.value_of_css_property('background-color')

    #Функция проверки подсветки текста
    def textColor(self, element):
        input_element = self.browser.find_element(*element)
        return input_element.value_of_css_property('color')

    #Функция для выделения текста в поле
    def contrlA(self, element):
        input_element = self.browser.find_element(*element)
        input_element.send_keys(Keys.CONTROL, 'a')

    #Функция для перемещения курсора в начало строки
    def home(self, element):
        input_element = self.browser.find_element(*element)
        input_element.send_keys(Keys.HOME)

    #Функция поиска и выбора дня в календаре (вызывая заменить day на день хоторый хотим выбрать (Число))
    def searchDay(self, element, day):
        input_element = self.browser.find_elements(*element)
        # found_day указывает, был ли найден указанный день в календаре. Если день найден, то переменная found_day становится True, и цикл завершается
        found_day = False
        for input in input_element:
            if input.text == day:
                input.click()
                found_day = True
                true_step('ОР: Поле заполнено')
                break

        if not found_day:
            false_step(f"Ошибка: Не удалось найти указанный день {day} в календаре")






