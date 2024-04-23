#==============================================Автотесты ТАП============================================================
import time

import pytest

from checks.formChecks import *

#=========================Подписание назначения в ТАП (Для вызова в других кейсах)======================================
@pytest.mark.regress_tap
def test_1_cases_create_purpose():

    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)
    time.sleep(4)

    # Кликаю кнопку "Добавить" в блоке "Назначения"
    f.click_element(BT_add_purpose)
    time.sleep(4)

    #Кликаю по полю "Препарат"
    f.click_element(FD_drug)

    # Ввожу в поле название препарата
    f.send_keys(FD_drug, 'Хлоргексидин, Хлоргексидин, р-р д/наружн. прим., 0.05 %,1000 мл')
    time.sleep(1)

    # Выбираю и кликаю по первому элементу выпадающего списка поля "Препарат"
    f.click_element(LT)
    time.sleep(3)

    #Кликаю кнопку "Подписать"
    f.click_element(BT_signature_path)
    time.sleep(6)


#============================Сохранение рецепта в ТАП (Для вызова в других кейсах)======================================
@pytest.mark.regress_tap
def test_2_cases_create_recipe():
    #Создаю назначение
    test_1_cases_create_purpose()
    f = ContractsPage(browser)
    case_name('Сохранение рецепта в ТАП')
    # Добавляю задержку в 4 секунды
    time.sleep(5)

    #Кликаю кнопку "Добавить" в блоке "Рецепты"
    f.click_element(BT_add_recipe)
    time.sleep(4)

    #Кликаю по полю "Льгота"
    f.click_element(FD_privilege)

    # Выбираю и кликаю по первому элементу выпадающего списка поля "Льгота"
    f.click_element(LT)

    #Убираю чек-бокс "На дом"
    f.click_element(CH_home)
    time.sleep(2)

    #Сохраняю рецепт
    f.click_element(BT_save_recipe)
    time.sleep(6)

    #Проверяю что рецепт после сохранения отображается в гриде блока "Рецепты"
    assert f.text(CL_num_recipe) != "", "Рецепт не появился в гриде!"
    time.sleep(6)


#==========test-cases/597 Заполнение полей рецепта. Валидация полей "Серия" и "Номер" с флажком "Бланк"=================
@pytest.mark.regress_tap
def test_3_cases_597():
    case_name('Заполнение полей рецепта. Валидация полей "Серия" и "Номер" с флажком "Бланк"')

    step('Шаг 1: Создать назначение')
    test_1_cases_create_purpose()
    true_step('ОР: - Назначение создано')
    f = ContractsPage(browser)
    if f.enabled(BT_add_recipe):
        true_step('    - Кнопка "Добавить" в блоке "Рецепты" стала доступна')
    else:
        true_step('Ошибка: Кнопка "Добавить" в блоке "Рецепты" не доступна')
    time.sleep(4)

    step('Шаг 2: Нажать на кнопку "Добавить" в блоке "Рецепты".')
    f.click_element(BT_add_recipe)
    time.sleep(4)
    true_step('ОР: Открылась форма создания рецептов.')

    step('Шаг 3: Выбрать чек-бокс "Коммерческий"')
    f.click_element(CH_comm)
    time.sleep(2)
    true_step('ОР: Чек-бокс выбран')

    step('Шаг 4: Выбрать чек-бокс "Бланк"')
    f.click_element(CH_blank)
    true_step('ОР: - Чек-бокс выбран')
    time.sleep(2)
    if f.enabled(FD_series) and f.enabled(FD_number):
        true_step('    - Стали доступны для заполнения поля "Серия" и "Номер"')
    else:
        false_step('Ошибка: Поле серия или номер недоступны')

    step('Шаг 5: Заполнить поле "Серия" с клавиатуры любыми символами.')
    f.send_keys(FD_series, 'A0145')
    time.sleep(1)
    f.tab(FD_series)
    time.sleep(1)
    if f.atribut(FD_series) == 'A0145':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле "Серия" не заполнено')

    step('Шаг 6: Очистить поле "Серия" с клавиатуры')
    f.clear_element(FD_series)
    time.sleep(2)
    if f.atribut(FD_series) == '':
        true_step("Поле 'Серия' успешно очищено")
    else:
        false_step('Ошибка: Поле "Серия" не очистилось')

    step('Шаг 7: Заполнить поле "Номер" с клавиатуры цифрами')
    f.send_keys(FD_number, '00001')
    time.sleep(2)
    f.tab(FD_number)
    time.sleep(4)
    if f.atribut(FD_number) == '00001':
        true_step("Поле 'Номер' успешно заполнено")
    else:
        false_step('Ошибка: Поле "Номер" не заполнено')

    step('Шаг 8: Очистить поле "Номер" с клавиатуры')
    f.clear_element(FD_number)
    time.sleep(2)
    if f.atribut(FD_number) == '':
        true_step("Поле 'Номер' успешно очищено")
    else:
        false_step('Ошибка: Поле "Номер" не очищено')


#========================test-cases/629 Отмена подписанного назначения лекарственного препарата=========================
@pytest.mark.regress_tap
def test_4_cases_629():
    case_name('Отмена подписанного назначения лекарственного препарата')
    # Создаю назначение
    step('Шаг-1: Создать назначение ЛС в статусе "Подписано"')
    test_1_cases_create_purpose()
    f = ContractsPage(browser)
    time.sleep(4)
    true_step('ОР: Открылась форма, аналогичная форме создания назначения')

    # Кликаю кнопку "Отменить назначение" в форме назначения
    step('Шаг-2: Нажать кнопку "Отменить назначение" в конце формы')
    f.click_element(BT_cancel)
    time.sleep(2)
    if f.enabled(CH_rez):
        true_step('ОР: Появляется чек-бокс "Резистентность к ЛС"')
    else:
        false_step('Ошибка: Чек-бокс "Резистентность к ЛС" недоступен')

    step('Шаг-3: Установить чек-бокс "Резистентность к ЛС"')
    f.click_element(CH_rez)
    time.sleep(2)
    if f.enabled(FD_comments) and f.enabled(CH_rez):
        true_step('ОР: Флажок установлен. Поле "Комментарий" стало доступно для заполнения"')
    else:
        false_step('Ошибка: Чек-бокс не установлен или поле "Комментарий" не доступно')

    step('Шаг-4: Заполнить поле "Комментарий"')
    text = 'Назначение не актуально'
    f.send_keys(FD_comments, text)
    time.sleep(2)
    if f.atribut(FD_comments) == text:
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено')

    step('Шаг-5: Нажать кнопку "Сохранить"')
    f.click_element(BT_save_cancel)
    time.sleep(4)
    if f.text(ST_purpose) == "Отменено":
        true_step('ОР: Назначение перешло в статус "Отменено"')
    else:
        false_step('Ошибка: статус назначения не изменился на "Отменено"')

    step('Шаг-6: Проверить, что чек-бокс "Резистентность к ЛС" выбран, поле "Комментарий" сохранено')
    if f.atribut(FD_comments) == text and f.disabled(FD_comments) and f.disabled(CH_rez_true):
        true_step('ОР: Чек-бокс установлен, поле сохранено верно. Недоступны для редактирования')
        if f.atribut(FD_comments) != text:
            false_step('Ошибка: Поле "Комментарий" содержит некорректный текст')
        if f.enabled(FD_comments):
            false_step('Ошибка: Чек-бокс или поле доступны для редактирования')


#====================test-cases/595 Заполнение полей рецепта. Валидация поля "Адрес доставки"===========================
@pytest.mark.regress_tap
def test_5_cases_595():
    case_name('Заполнение полей рецепта. Валидация поля "Адрес доставки"')
    step('Шаг 1: Выбрать назначение из списка или создать новое')
    test_1_cases_create_purpose()
    f = ContractsPage(browser)
    time.sleep(4)
    if f.enabled(BT_add_recipe):
        true_step('ОР: Назначение выбрано. Кнопка "Добавить" в блоке "Рецепты" стала доступна.')
    else:
        false_step('Ошибка: Кнопка "Добавить" в блоке "Рецепты" не доступна')

    step('Шаг 2: Нажать на кнопку "Добавить" в блоке "Рецепты".')
    f.click_element(BT_add_recipe)
    if f.enabled(FM_recipe):
        true_step('ОР: Открылась форма создания рецептов.')
    else:
        false_step('Ошибка: Форма рецепта не открылась')
    time.sleep(3)

    step('Шаг 3: Установить флажок "Коммерческий".')
    f.click_element(CH_comm)
    if f.enabled(CH_comm):
        true_step('ОР: Флажок установлен.')
    else:
        false_step('Ошибка: Не удалось выбрать чек-бокс "Коммерческий"')
    time.sleep(1)

    step('Шаг 4: Установить флажок "На дом".')
    f.click_element(CH_home)
    time.sleep(1)
    if f.enabled(FD_phone) and f.enabled(FD_adress):
        true_step('ОР: Поля "Телефон" и "Адрес доставки" доступны для редактирования.')
    else:
        false_step('Ошибка: Поля "Телефон" и "Адрес доставки" не доступны')

    step('Шаг 5: Очистить поле "Адрес доставки".')
    f.click_element(BT_clear_adress)
    f.tab(FD_adress)
    time.sleep(1)
    text_errors = " Адрес должен содержать как минимум регион (объект фед. значения), улицу/населенный пункт и номер дома "
    if f.atribut(WD_adress) != text_errors and f.textColor(WD_adress) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения.')
    else:
        false_step('Ошибка: Отсутствует маркер обязательности поля')

    step('Шаг 6: Начать заполнять поле с клавиатуры.')
    text = 'Белгородская обл, г Строитель, ул Ленина, д 19 к а стр 1, кв 56'
    f.send_keys(FD_adress, text)
    time.sleep(1)
    if f.text(LT) == text:
        true_step('ОР: Происходит фильтрация значений в выпадающем списке.')
    else:
        false_step('Ошибка: Элементы выпадающего списка не доступны')

    step('Шаг 7: Выбрать значение из списка.')
    f.click_element(LT)
    time.sleep(1)
    f.tab(FD_adress)
    time.sleep(1)
    if f.enabled(FD_adress_text):
        true_step("ОР: Поле 'Адрес доставки' успешно заполнено")
    else:
        false_step('Ошибка: Поле "Адрес доставки" не заполнено')

    step('Шаг 8: Очистить поле "Адрес доставки" нажатием на крестик')
    f.click_element(BT_clear_adress)
    time.sleep(1)
    if f.element_absent(FD_adress_text) and f.textColor(WD_adress) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения.')
    else:
        false_step('Ошибка: Отсутствует маркер обязательности поля')

    step('Шаг 9: Ввести в поле невалидное значение и кликнуть в пустом месте формы.')
    f.send_keys(FD_adress, 'Невалидный адрес')
    f.tab(FD_adress)
    time.sleep(1)
    if f.element_absent(FD_adress_text) and f.textColor(WD_adress) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения.')
    else:
        false_step('Ошибка: Отсутствует маркер обязательности поля')


#=========test-cases/14508 Валидация поля 'Дата выписки' при создании рецепта с датой больше/меньще текущей=============
@pytest.mark.regress_tap
def test_6_cases_14508():
    case_name('Валидация поля "Дата выписки" при создании рецепта с датой больше/меньще текущей')

    step('Шаг 1: В блоке "Врачебные назначения" выбрать/создать назначение')
    test_1_cases_create_purpose()
    f = ContractsPage(browser)
    time.sleep(4)
    if f.enabled(BT_add_recipe):
        true_step('ОР: После создания назначения кнопка "Добавить" в блоке "Рецепты" стала активной')
    else:
        false_step('Ошибка: Кнопка "Добавить" в блоке "Рецепты" недоступна')

    step('Шаг 2: Нажать на кнопку "Добавить" в блоке "Рецепты".')
    f.click_element(BT_add_recipe)
    time.sleep(4)
    if f.enabled(FM_recipe):
        true_step('ОР: - Открылась форма создания рецептов.')
    else:
        false_step('Ошибка: Форма рецепта недоступна')

    if f.atribut(FD_date) == DT.strftime('%d.%m.%Y'):
        true_step('    - Поле "Дата выписки" по умолчанию заполнена текущей датой')
    else:
        false_step('Ошибка: Значение в поле "Дата выписки" НЕ содержит текущую дату')

    step('Шаг 3: Установить флажок "Коммерческий".')
    f.click_element(CH_comm)
    time.sleep(1)
    if f.enabled(CH_comm):
        true_step('ОР: Флажок установлен.')
    else:
        false_step('Ошибка: Не удалось выбрать чек-бокс "Коммерческий"')

    step('Шаг 4: В поле "Дата выписки" ввести дату больше текущей даты')
    # Вводжу дату больше текущей
    date = (DT + timedelta(days=1)).strftime('%d.%m.%Y')
    f.contrlA(FD_date)
    f.send_keys(FD_date, date)
    f.tab(FD_date)
    time.sleep(1)
    if f.atribut(FD_date) == date:
        true_step(f'ОР: Поле "Дата выписки" заполнено датой {date}')
    else:
        false_step('Ошибка: Поле "Дата выписки" НЕ заполнено')

    step('Шаг 5: Кликнуть кнопку "Подписать и отправить"')
    f.click_element(BT_caption_recipe)
    time.sleep(5)
    if f.text(ER) == 'Оформление рецепта невозможно. Дата выписки рецепта не может быть больше текущей даты.':
        true_step(f'ОР: - Сообщение об ошибке: {f.text(ER)}')
        true_step('    - Рецепт не подписан')
    else:
        false_step('Ошибка: Сообщение об ошибке не отображается')

    step('Шаг 6: В поле "Дата выписки" поставить дату меньше "Даты начала" действия назначения')
    f.contrlA(FD_date)
    date = (DT - timedelta(days=1)).strftime('%d.%m.%Y')
    f.send_keys(FD_date, date)
    f.tab(FD_date)
    time.sleep(1)
    if f.atribut(FD_date) == date:
        true_step(f'ОР: Поле "Дата выписки" заполнено датой {date}')
    else:
        false_step('Ошибка: Поле "Дата выписки" НЕ заполнено')

    step('Шаг 7: Кликнуть кнопку "Подписать и отправить"')
    f.click_element(BT_caption_recipe)
    time.sleep(5)
    if f.text(ER) == 'Оформление рецепта невозможно. Дата выписки рецепта не может быть меньше даты начала действия назначения.':
        true_step(f'ОР: - Сообщение об ошибке: {f.text(ER)}')
        true_step('    - Рецепт не подписан')
    else:
        false_step('Ошибка: Сообщение об ошибке не отображается')


#=======================test-cases/677 Заполнение шапки назначения. Валидация поля "Время"==============================
@pytest.mark.regress_tap
def test_7_cases_677():
    case_name('Заполнение шапки назначения. Валидация поля "Время"')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить" в блоке "Врачебные назначения"')
    #Кликаю кнопку "Добавить" в блоке "Назначения"
    f.click_element(BT_add_purpose)
    date = DT.strftime('%H:%M')
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Проверить, что поле "Время" заполнено автоматически текущим временем')
    if f.atribut(FD_time) == date:
        true_step('ОР: - Поле заполнено автоматически текущим временем')
    else:
        false_step('Ошибка: Значение в поле "Время" НЕ содержит текущее время')

    step('Шаг 3: Очистить поле "Время" с клавиатуры')
    f.clear_element(FD_time)
    f.tab(FD_time)
    time.sleep(1)
    if f.atribut(FD_time) == '00:00':
        true_step('ОР: - Поле установило значение 00:00')
    else:
        false_step('Ошибка: Поле некорректно очистилось')

    step('Шаг 4: Ввести в поле буквы')
    f.clear_element(FD_time)
    f.home(FD_time)  # Перемещение курсора в начало строки
    f.send_keys(FD_time, 'буквы')
    f.tab(FD_time)
    time.sleep(1)
    if f.atribut(FD_time) == '00:00':
        true_step('ОР: - Поле не заполняется буквами')
    else:
        false_step('Ошибка: Поле некорректно заполнилось')

    step('Шаг 5: Ввести в поле символы')
    f.clear_element(FD_time)
    f.home(FD_time)  # Перемещение курсора в начало строки
    f.send_keys(FD_time, '!@#$')
    f.tab(FD_time)
    time.sleep(1)
    if f.atribut(FD_time) == '00:00':
        true_step('ОР: - Поле не заполняется символами')
    else:
        false_step('Ошибка: Поле некорректно заполнилось')

    step('Шаг 6: Ввести в поле валидное значение (цифры)')
    f.clear_element(FD_time)
    f.home(FD_time)  # Перемещение курсора в начало строки
    f.send_keys(FD_time, '12:14')
    f.tab(FD_time)
    time.sleep(1)
    if f.atribut(FD_time) == '12:14':
        true_step('ОР: - Поле заполняется корректно')
    else:
        false_step('Ошибка: Поле некорректно заполнилось')


#===================test-cases/649 Подписание назначения лекарственного препарата из создания назначения================
@pytest.mark.regress_tap
def test_8_cases_649():
    case_name('Подписание назначения лекарственного препарата из создания назначения')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    # Кликаю кнопку "Добавить" в блоке "Назначения"
    f.click_element( BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Заполнить поле препарат для добавления назначения')
    #Кликаю по полю "Препарат"
    f.click_element(FD_drug)
    f.send_keys(FD_drug, 'Хлоргексидин, Хлоргексидин, р-р д/наружн. прим., 0.05 %,1000 мл')
    time.sleep(2)
    f.click_element(LT)
    time.sleep(4)
    OB_form_purpose() #Вызываю функцию проверки обязательных полей формы

    step('Шаг 3: Нажать кнопку "Подписать"')
    f.click_element(BT_signature_path)
    time.sleep(4)
    if f.text(ST_purpose) == 'Подписано':
        true_step('ОР: - Назначение сохранилось со статусом "Подписано"')
    else:
        false_step('Ошибка: Статус назначения отображается некорректно')

    step('Шаг 4: Проверить, что подписанное назначение отображается в списке назначений со статусом "Подписано"')
    f.getStateGrid(ST_purpose_grid, BT_next, 'Подписано')


#=======================test-cases/609 Валидация поля "Врач" при создании назначения лекарственного препарата===========
@pytest.mark.regress_tap
def test_9_case_609():
    case_name('Валидация поля "Врач" при создании назначения лекарственного препарата')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    # Кликаю кнопку "Добавить" в блоке "Назначения"
    f.click_element( BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Проверить, что поле "Врач" заполнено автоматически лечащим врачом и доступно для редактирования')
    text = '2372 - Гиппократ Ирина Константиновна (врач-хирург, Косметология, Ржевка кабинет терапевта, ОГБУЗ "ШЕБЕКИНСКАЯ ЦРБ" РЖЕВСКАЯ АМБУЛАТОРИЯ)'
    if f.enabled(FD_doctor) and f.atribut(FD_doctor) == text:
        true_step('    - Поле "Врач" заполнено автоматически лечащим врачом и доступно для редактирования')
    else:
        false_step('Ошибка: Поле "Врач" заполнено некорректно или недоступно для редактирования')
    time.sleep(4)

    step('Шаг 3: Очистить поле нажатием на крестик')
    f.click_element(BT_clear_doctor)
    time.sleep(1)
    if f.atribut(FD_doctor) == '' and f.backColor(OB_doctor) == 'rgba(255, 82, 82, 1)':
        true_step("ОР: - Поле очищено и подсвечено красным, как обязательное для заполнения")
    else:
        false_step('Ошибка: Поле не очищено или не подсвечено красным')
    if f.enabled(LT_doctor_list):
        true_step('    - Открыт выпадающий список врачей')
    else:
        false_step('Ошибка: Выпадающий список не отображается')

    step('Шаг 4: Начать заполнять поле "Врач" буквами')
    name = 'Гиппократ Ирина Константиновна'
    f.send_keys(FD_doctor, name)
    time.sleep(2)
    name_doctor = '2372 - Гиппократ Ирина Константиновна (врач-хирург, Косметология, Ржевка кабинет терапевта)'
    if f.text(LT_doctor) == name_doctor:
        true_step('ОР: Происходит фильтрация значений в выпадающем списке врачей по ФИО')
    else:
        false_step('Ошибка: Фильтрация не работает, либо работает некорректно')

    step('Шаг 5: Выбрать значение из выпадающего списка')
    f.click_element(LT_doctor)
    f.tab(FD_doctor)
    time.sleep(1)
    if f.atribut(FD_doctor) == name_doctor:
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено')

    step('Шаг 6: Очистить поле с клавиатуры')
    f.clear_element(FD_doctor)
    time.sleep(1)
    if f.atribut(FD_doctor) == '' and f.backColor(OB_doctor) == 'rgba(255, 82, 82, 1)':
        true_step("ОР: - Поле очищено и подсвечено красным, как обязательное для заполнения")
    else:
        false_step('Ошибка: Поле не очищено или не подсвечено красным')

    step('Шаг 7: Начать заполнять поле символами. Нажать в пустое место')
    simvols = '!@#$%^'
    f.send_keys(FD_doctor, simvols)
    time.sleep(1)
    f.tab(FD_doctor)
    time.sleep(1)
    if f.atribut(FD_doctor) == '':
        true_step("ОР: - Поле не заполнено")
    else:
        false_step('Ошибка: Поле заполнено')

    step('Шаг 8: Начать заполнять поле цифрами')
    code = '2372'
    f.send_keys(FD_doctor, code)
    time.sleep(1)
    if f.text(LT_doctor) == name_doctor:
        true_step('ОР: Происходит фильтрация значений в выпадающем списке врачей по коду')
    else:
        false_step('Ошибка: Фильтрация не работает, либо работает некорректно')

    step('Шаг 9: Выбрать значение из выпадающего списка')
    f.click_element(LT_doctor)
    f.tab(FD_doctor)
    time.sleep(1)
    if f.atribut(FD_doctor) == name_doctor:
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено')

    step('Шаг 10: Очистить поле нажатием на крестик')
    f.click_element(BT_clear_doctor)
    time.sleep(1)
    if f.atribut(FD_doctor) == '' and f.backColor(OB_doctor) == 'rgba(255, 82, 82, 1)':
        true_step("ОР: - Поле очищено и подсвечено красным, как обязательное для заполнения")
    else:
        false_step('Ошибка: Поле не очищено или не подсвечено красным')
    if f.enabled(LT_doctor_list):
        true_step('    - Открыт выпадающий список врачей')
    else:
        false_step('Ошибка: Выпадающий список не отображается')


#=================test-cases/616 Валидация поля "Дата начала" при создании назначения лекарственного препарата==========
@pytest.mark.regress_tap
def test_10_case_616():
    case_name('Валидация поля "Дата начала" при создании назначения лекарственного препарата')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    # Кликаю кнопку "Добавить" в блоке "Назначения"
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Проверить, что поле «Дата начала» по умолчанию заполнено текущей датой')
    date = DT.strftime('%d.%m.%Y')
    if f.atribut(FD_startDate) == date:
        true_step('ОР: Поле «Дата начала» заполнено текущей датой')
    else:
        false_step('Ошибка: Поле «Дата начала» заполнено некорректной датой')
    time.sleep(4)

    step('Шаг 3: Очистить поле с клавиатуры')
    f.clear_element(FD_startDate)
    time.sleep(1)
    if f.atribut(FD_startDate) == '':
        true_step('ОР: Поле очищено и отображается по умолчанию "дд.мм.гггг"')
    else:
        false_step('Ошибка: Поле "Дата начала" не очищено либо заполнено некорректно')

    step('Шаг 4: Нажать на календарь и выбрать дату начала ')
    f.click_element(BT_startDate)
    time.sleep(1)
    # Получаю вчерашний день в формате: только число/день
    day = (DT - timedelta(days=1)).strftime('%d')
    f.searchDay(CL_startDate, day)
    time.sleep(3)

    step('Шаг 5: Очистить поле с клавиатуры')
    f.clear_element(FD_startDate)
    time.sleep(1)
    if f.atribut(FD_startDate) == '':
        true_step('ОР: Поле очищено и отображается по умолчанию "дд.мм.гггг"')
    else:
        false_step('Ошибка: Поле "Дата начала" не очищено либо заполнено некорректно')

    step('Шаг 6: Заполнить поле с клавиатуры цифрами')
    newDate = (DT - timedelta(days=4)).strftime('%d.%m.%Y')
    f.send_keys(FD_startDate, newDate)
    f.tab(FD_startDate)
    time.sleep(1)
    if f.atribut(FD_startDate) == newDate:
        true_step('ОР: Поле заполнено корректно')
    else:
        false_step('Ошибка: Поле "Дата начала" заполнилось некорректно')

    step('Шаг 7: Очистить поле с клавиатуры')
    f.clear_element(FD_startDate)
    time.sleep(1)
    if f.atribut(FD_startDate) == '':
        true_step('ОР: Поле очищено и отображается по умолчанию "дд.мм.гггг"')
    else:
        false_step('Ошибка: Поле "Дата начала" не очищено либо заполнено некорректно')

    step('Шаг 8: Заполнить поле с клавиатуры буквами')
    f.send_keys(FD_startDate, 'дата')
    f.tab(FD_startDate)
    time.sleep(1)
    if f.atribut(FD_startDate) == newDate:
        true_step('ОР: В поле не вводятся буквы')
    else:
        false_step('Ошибка: Поле "Дата начала" заполнилось некорректно')

    step('Шаг 9: Заполнить поле с клавиатуры спецсимволами')
    f.send_keys(FD_startDate, '!"№;;%')
    f.tab(FD_startDate)
    time.sleep(1)
    if f.atribut(FD_startDate) == newDate:
        true_step('ОР: В поле не вводятся спецсимволы')
    else:
        false_step('Ошибка: Поле "Дата начала" заполнилось некорректно')


# =================test-cases/611 Валидация поля "Детализация" при создании назначения лекарственного препарата=========
@pytest.mark.regress_tap
def test_11_case_611():
    case_name('Валидация поля "Детализация" при создании назначения лекарственного препарата')
    # Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    # Кликаю кнопку "Добавить" в блоке "Назначения"
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Заполнить поле "Детализация" - буквами')
    f.send_keys(FD_details, 'Детализация')
    f.tab(FD_details)
    time.sleep(1)
    if f.atribut(FD_details) == 'Детализация':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле "Детализация" не заполнено или заполнилось некорректно')

    step('Шаг 3: Очистить поле нажатием на крестик')
    f.click_element(BT_details)
    time.sleep(1)
    if f.atribut(FD_details) == '':
        true_step('ОР: Поле очищено')
    else:
        false_step('Ошибка: Поле "Детализация" не очищено либо заполнено некорректно')

    step('Шаг 4: Заполнить поле "Детализация" - цифрами')
    f.send_keys(FD_details, '12345')
    f.tab(FD_details)
    time.sleep(1)
    if f.atribut(FD_details) == '12345':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле "Детализация" не заполнено или заполнилось некорректно')

    step('Шаг 5: Очистить поле с клавиатуры')
    f.clear_element(FD_details)
    time.sleep(1)
    if f.atribut(FD_details) == '':
        true_step('ОР: Поле очищено')
    else:
        false_step('Ошибка: Поле "Детализация" не очищено либо заполнено некорректно')

    step('Шаг 6: Заполнить поле "Детализация" - спецсимволами')
    f.send_keys(FD_details, '!"№;%:?')
    f.tab(FD_details)
    time.sleep(1)
    if f.atribut(FD_details) == '!"№;%:?':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле "Детализация" не заполнено или заполнилось некорректно')

    step('Шаг 7: Очистить поле нажатием на крестик')
    f.click_element(BT_details)
    time.sleep(2)
    if f.atribut(FD_details) == '':
        true_step('ОР: Поле очищено')
    else:
        false_step('Ошибка: Поле "Детализация" не очищено либо заполнено некорректно')


# ============test-cases/618 Валидация поля "Ед. измерения" при создании назначения лекарственного препарата============
@pytest.mark.regress_tap
def test_12_cases_618():
    case_name('Валидация поля "Ед. измерения" при создании назначения лекарственного препарата')
    # Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    # Кликаю кнопку "Добавить" в блоке "Назначения"
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Заполнить поле препарат для добавления назначения')
    #Кликаю по полю "Препарат"
    f.click_element(FD_drug)
    f.send_keys(FD_drug, 'Хлоргексидин, Хлоргексидин, р-р д/наружн. прим., 0.05 %,1000 мл')
    time.sleep(2)
    f.click_element(LT)
    time.sleep(3)
    OB_form_purpose() #Вызываю функцию проверки обязательных полей формы

    step('Шаг 3: Проверить, что поле «Ед. измерения» заполнено автоматически значением из справочника и доступно для редактирования.')
    if f.atribut(FD_unit) == 'мл' and f.enabled(FD_unit):
        true_step('ОР: Поле заполнено значением из справочника и доступно для редактирования')
    else:
        false_step('Ошибка: Поле заполнено некорректно или недоступно для редактирования')

    step('Шаг 4: Очистить поле с клавиатуры')
    f.clear_element(FD_unit)
    f.tab(FD_unit)
    time.sleep(1)
    if f.atribut(FD_unit) == '' and f.backColor(OB_unit) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Поле не очистилось или не подсвечено красным')

    step('Шаг 5: Заполнить поле - буквами')
    f.send_keys(FD_unit, 'Буквы')
    f.tab(FD_unit)
    time.sleep(1)
    if f.atribut(FD_unit) == 'Буквы':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено или заполенно некорректно')

    step('Шаг 6: Очистить поле с клавиатуры')
    f.clear_element(FD_unit)
    time.sleep(1)
    if f.atribut(FD_unit) == '' and f.backColor(OB_unit) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Поле не очистилось или не подсвечено красным')

    step('Шаг 7: Заполнить поле - цыфрами')
    f.send_keys(FD_unit, '12345')
    f.tab(FD_unit)
    time.sleep(1)
    if f.atribut(FD_unit) == '12345':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено или заполенно некорректно')

    step('Шаг 8: Очистить поле с клавиатуры')
    f.clear_element(FD_unit)
    time.sleep(1)
    if f.atribut(FD_unit) == '' and f.backColor(OB_unit) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Поле не очистилось или не подсвечено красным')

    step('Шаг 9: Заполнить поле - символами')
    f.send_keys(FD_unit, '!"№;%:')
    f.tab(FD_unit)
    time.sleep(1)
    if f.atribut(FD_unit) == '!"№;%:':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено или заполенно некорректно')

    step('Шаг 10: Очистить поле с клавиатуры')
    f.clear_element(FD_unit)
    time.sleep(1)
    if f.atribut(FD_unit) == '' and f.backColor(OB_unit) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Поле не очистилось или не подсвечено красным')


# ============test-cases/615 Валидация поля "Кол-во дней" при создании назначения лекарственного препарата==============
@pytest.mark.regress_tap
def test_13_cases_615():
    case_name('Валидация поля "Кол-во дней" при создании назначения лекарственного препарата')
    # Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    # Кликаю кнопку "Добавить" в блоке "Назначения"
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Проверить, что поле "Кол-во дней" заполнено автоматически значением "1"')
    if f.atribut(FD_countDay) == '1':
        true_step('ОР: Поле заполнено автоматически значением "1"')
    else:
        false_step('Ошибка: Поле заполнено некорректно')

    step('Шаг 3: Заполнить поле значением <0')
    f.contrlA(FD_countDay)
    f.send_keys(FD_countDay, '-1')
    f.tab(FD_countDay)
    time.sleep(1)
    if f.atribut(FD_countDay) == '11':
        true_step('ОР: Поле не заполнено')
    else:
        false_step('Ошибка: Поле заполнено или заполенно некорректно')

    step('Шаг 4: Заполнить поле значением >0')
    f.contrlA(FD_countDay)
    f.send_keys(FD_countDay, '3')
    f.tab(FD_countDay)
    time.sleep(1)
    if f.atribut(FD_countDay) == '3':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено или заполенно некорректно')

    step('Шаг 5: Заполнить поле буквами')
    f.contrlA(FD_countDay)
    f.send_keys(FD_countDay, 'Б')
    f.tab(FD_countDay)
    time.sleep(1)
    if f.atribut(FD_countDay) == '1':
        true_step('ОР: Поле не заполнено')
    else:
        false_step('Ошибка: Поле заполнено или заполенно некорректно')

    step('Шаг 6: Заполнить поле символами')
    f.contrlA(FD_countDay)
    f.send_keys(FD_countDay, '!№')
    f.tab(FD_countDay)
    time.sleep(1)
    if f.atribut(FD_countDay) == '1':
        true_step('ОР: Поле не заполнено')
    else:
        false_step('Ошибка: Поле заполнено или заполенно некорректно')


# ============test-cases/614 Валидация поля "Кол-во на курс" при создании назначения лекарственного препарата===========
@pytest.mark.regress_tap
def test_14_cases_614():
    case_name('Валидация поля "Кол-во на курс" при создании назначения лекарственного препарата')
    # Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    # Кликаю кнопку "Добавить" в блоке "Назначения"
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Проверить, что поле "Кол-во на курс" заполнено автоматически значением "1"')
    if f.atribut(FD_perCourse) == '1':
        true_step('ОР: Поле заполнено автоматически значением "1"')
    else:
        false_step('Ошибка: Поле заполнено некорректно')

    step('Шаг 3: Очистить поле с клавиатуры')
    f.clear_element(FD_perCourse)
    f.tab(FD_perCourse)
    time.sleep(1)
    if f.atribut(FD_perCourse) == '' and f.backColor(OB_perCourse) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Поле не очистилось или не подсвечено красным')

    step('Шаг 4: Заполнить поле значением "0"')
    f.send_keys(FD_perCourse, '0')
    f.tab(FD_perCourse)
    time.sleep(1)
    if f.atribut(FD_perCourse) == '0':
        true_step('ОР: Поле заполнено и подсвечено красным')
    else:
        false_step('Ошибка: Поле заполнено некорректно либо не подсвечено красным')

    step('Шаг 5: Очистить поле с клавиатуры')
    f.clear_element(FD_perCourse)
    f.tab(FD_perCourse)
    time.sleep(1)
    if f.atribut(FD_perCourse) == '' and f.backColor(OB_perCourse) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Поле не очистилось или не подсвечено красным')

    step('Шаг 6: Заполнить поле значением <0')
    f.send_keys(FD_perCourse, '-1')
    f.tab(FD_perCourse)
    time.sleep(1)
    if f.atribut(FD_perCourse) == '1':
        true_step('ОР: В поле знак "-" не ввелся, поле заполнилось значением >0')
    else:
        false_step('Ошибка: Поле заполнено некорректно')

    step('Шаг 7: Очистить поле с клавиатуры')
    f.clear_element(FD_perCourse)
    f.tab(FD_perCourse)
    time.sleep(1)
    if f.atribut(FD_perCourse) == '' and f.backColor(OB_perCourse) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Поле не очистилось или не подсвечено красным')

    step('Шаг 8: Заполнить поле значением >0')
    f.send_keys(FD_perCourse, '12')
    f.tab(FD_perCourse)
    time.sleep(1)
    if f.atribut(FD_perCourse) == '12':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле заполнено некорректно')

    step('Шаг 9: Очистить поле с клавиатуры')
    f.clear_element(FD_perCourse)
    f.tab(FD_perCourse)
    time.sleep(1)
    if f.atribut(FD_perCourse) == '' and f.backColor(OB_perCourse) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Поле не очистилось или не подсвечено красным')

    step('Шаг 10: Заполнить поле буквами')
    f.send_keys(FD_perCourse, 'Буквы')
    f.tab(FD_perCourse)
    time.sleep(1)
    if f.atribut(FD_perCourse) == '' and f.backColor(OB_perCourse) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле не заполнилось и подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Поле не очистилось или не подсвечено красным')

    step('Шаг 11: Заполнить поле символами')
    f.send_keys(FD_perCourse, '!№')
    f.tab(FD_perCourse)
    time.sleep(1)
    if f.atribut(FD_perCourse) == '' and f.backColor(OB_perCourse) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле не заполнилось и подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Поле не очистилось или не подсвечено красным')


# ========test-cases/610 Валидация поля "Обоснование назначения" при создании назначения лекарственного препарата=======
@pytest.mark.regress_tap
def test_15_cases_610():
    case_name('Валидация поля "Обоснование назначения" при создании назначения лекарственного препарата')
    # Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Заполнить поле "Обоснование назначения" буквами')
    f.send_keys(FD_rationalDose, 'Буквы')
    f.tab(FD_rationalDose)
    time.sleep(1)
    if f.atribut(FD_rationalDose) == 'Буквы':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнилось или заполнилось некорректно')

    step('Шаг 3: Очистить поле с клавиатуры')
    f.clear_element(FD_rationalDose)
    f.tab(FD_rationalDose)
    time.sleep(1)
    if f.atribut(FD_rationalDose) == '':
        true_step('ОР: Поле очищено')
    else:
        false_step('Ошибка: Поле не очистилось')

    step('Шаг 4: Заполнить поле цифрами')
    f.send_keys(FD_rationalDose, '12345')
    f.tab(FD_rationalDose)
    time.sleep(1)
    if f.atribut(FD_rationalDose) == '12345':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнилось или заполнилось некорректно')

    step('Шаг 5: Очистить поле с клавиатуры')
    f.clear_element(FD_rationalDose)
    f.tab(FD_rationalDose)
    time.sleep(1)
    if f.atribut(FD_rationalDose) == '':
        true_step('ОР: Поле очищено')
    else:
        false_step('Ошибка: Поле не очистилось')

    step('Шаг 6: Заполнить поле цифрами')
    f.send_keys(FD_rationalDose, '!№;%:')
    f.tab(FD_rationalDose)
    time.sleep(1)
    if f.atribut(FD_rationalDose) == '!№;%:':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнилось или заполнилось некорректно')

    step('Шаг 7: Очистить поле с клавиатуры')
    f.clear_element(FD_rationalDose)
    f.tab(FD_rationalDose)
    time.sleep(1)
    if f.atribut(FD_rationalDose) == '':
        true_step('ОР: Поле очищено')
    else:
        false_step('Ошибка: Поле не очистилось')


# ============test-cases/617 Валидация поля "Раз в день" при создании назначения лекарственного препарата===============
@pytest.mark.regress_tap
def test_16_cases_617():
    case_name('Валидация поля "Раз в день" при создании назначения лекарственного препарата')
    # Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Заполнить поле препарат для добавления назначения')
    #Кликаю по полю "Препарат"
    f.click_element(FD_drug)
    f.send_keys(FD_drug, 'Хлоргексидин, Хлоргексидин, р-р д/наружн. прим., 0.05 %,1000 мл')
    time.sleep(2)
    f.click_element(LT)
    time.sleep(3)
    OB_form_purpose() #Вызываю функцию проверки обязательных полей формы

    step('Шаг 3: Проверить, что поле "Раз в день" заполнено автоматически значением "1"')
    if f.atribut(FD_onceADay) == '1':
        true_step('ОР: Поле заполнено автоматически значением "1"')
    else:
        false_step('Ошибка: Поле заполнено некорректно')

    step('Шаг 4: Очистить поле с клавиатуры')
    f.clear_element(FD_onceADay)
    f.tab(FD_onceADay)
    time.sleep(1)
    if f.atribut(FD_onceADay) == '1':
        true_step('ОР: Поле не очищается, прописывается "1"')
    else:
        false_step('Ошибка: Поле очистилось или заполенно некорректно')

    step('Шаг 5: Заполнить поле значением 0')
    f.contrlA(FD_onceADay)
    f.send_keys(FD_onceADay, '0')
    f.tab(FD_onceADay)
    time.sleep(1)
    if f.atribut(FD_onceADay) == '1':
        true_step('ОР: Поле не заполняется, прописывается "1"')
    else:
        false_step('Ошибка: Поле очистилось или заполенно некорректно')

    step('Шаг 6: Заполнить поле значением <0')
    f.contrlA(FD_onceADay)
    f.send_keys(FD_onceADay, '-1')
    f.tab(FD_onceADay)
    time.sleep(1)
    if f.atribut(FD_onceADay) == '11':
        true_step('ОР: В поле знак "-" не ввелся, поле заполнилось значением >0')
    else:
        false_step('Ошибка: Поле не заполнено или заполенно некорректно')

    step('Шаг 7: Заполнить поле значением >0')
    f.contrlA(FD_onceADay)
    f.send_keys(FD_onceADay, '5')
    f.tab(FD_onceADay)
    time.sleep(1)
    if f.atribut(FD_onceADay) == '5':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено или заполенно некорректно')

    step('Шаг 8: Заполнить поле буквами')
    f.contrlA(FD_onceADay)
    f.send_keys(FD_onceADay, 'Б')
    f.tab(FD_onceADay)
    time.sleep(1)
    if f.atribut(FD_onceADay) == '1':
        true_step('ОР: Поле не заполнено')
    else:
        false_step('Ошибка: Поле заполнено или заполенно некорректно')

    step('Шаг 9: Заполнить поле символами')
    f.contrlA(FD_onceADay)
    f.send_keys(FD_onceADay, '!№')
    f.tab(FD_onceADay)
    time.sleep(1)
    if f.atribut(FD_onceADay) == '1':
        true_step('ОР: Поле не заполнено')
    else:
        false_step('Ошибка: Поле заполнено или заполенно некорректно')


# ===========test-cases/619 Валидация поля "Разовая доза" при создании назначения лекарственного препарата==============
@pytest.mark.regress_tap
def test_17_cases_619():
    case_name('Валидация поля "Разовая доза" при создании назначения лекарственного препарата')
    # Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Заполнить поле препарат для добавления назначения')
    #Кликаю по полю "Препарат"
    f.click_element(FD_drug)
    f.send_keys(FD_drug, 'Хлоргексидин, Хлоргексидин, р-р д/наружн. прим., 0.05 %,1000 мл')
    time.sleep(2)
    f.click_element(LT)
    time.sleep(3)
    OB_form_purpose() #Вызываю функцию проверки обязательных полей формы

    step('Шаг 3: Проверить, что поле "Разовая доза" заполнено автоматически в соответствии с выбранным "Препарат"')
    if f.atribut(FD_singleDose) == '1000':
        true_step('ОР: Поле заполнено автоматически значением в соответствии с выбранным "Препарат"')
    else:
        false_step('Ошибка: Поле заполнено некорректно')

    step('Шаг 4: Очистить поле с клавиатуры')
    f.clear_element(FD_singleDose)
    f.tab(FD_singleDose)
    time.sleep(1)
    if f.atribut(FD_singleDose) == '':
        true_step('ОР: Поле очищено')
    else:
        false_step('Ошибка: Поле очистилось или заполенно некорректно')

    step('Шаг 5: Заполнить поле значением 0')
    f.contrlA(FD_singleDose)
    f.send_keys(FD_singleDose, '0')
    f.tab(FD_singleDose)
    time.sleep(1)
    if f.atribut(FD_singleDose) == '0':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле очистилось или заполенно некорректно')

    step('Шаг 6: Заполнить поле значением <0')
    f.contrlA(FD_singleDose)
    f.send_keys(FD_singleDose, '-1')
    f.tab(FD_singleDose)
    time.sleep(1)
    if (f.atribut(FD_singleDose)== '1'):
        true_step('ОР: В поле знак "-" не ввелся, поле заполнилось значением >0')
    else:
        false_step('Ошибка: Поле не заполнено или заполенно некорректно')

    step('Шаг 7: Заполнить поле значением >0')
    f.contrlA(FD_singleDose)
    f.send_keys(FD_singleDose, '5')
    f.tab(FD_singleDose)
    time.sleep(1)
    if f.atribut(FD_singleDose) == '5':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено или заполенно некорректно')

    step('Шаг 8: Заполнить поле буквами')
    f.contrlA(FD_singleDose)
    f.send_keys(FD_singleDose, 'Б')
    f.tab(FD_singleDose)
    time.sleep(1)
    if f.atribut(FD_singleDose) == '':
        true_step('ОР: Поле не заполнено')
    else:
        false_step('Ошибка: Поле заполнено или заполенно некорректно')

    step('Шаг 9: Заполнить поле символами')
    f.contrlA(FD_singleDose)
    f.send_keys(FD_singleDose, '!№')
    f.tab(FD_singleDose)
    time.sleep(1)
    if f.atribut(FD_singleDose) == '':
        true_step('ОР: Поле не заполнено')
    else:
        false_step('Ошибка: Поле заполнено или заполенно некорректно')


# ==========test-cases/613 Валидация поля "Способ приема" при создании назначения лекарственного препарата==============
@pytest.mark.regress_tap
def test_18_cases_613():
    case_name('Валидация поля "Разовая доза" при создании назначения лекарственного препарата')
    # Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Нажать на поле "Способ приема" для заполнения')
    f.click_element(FD_receptionMethod)
    time.sleep(2)
    if f.enabled(LT_receptionMethod):
        true_step('ОР: Открыт выпадающий список способов приема')
    else:
        false_step('Ошибка: Выпадающий список не отображается')

    step('Шаг 3: Выбрать значение из выпадающего списка')
    f.click_element(LT)
    f.tab(FD_receptionMethod)
    if f.atribut(FD_receptionMethod) == 'Принимать':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено или заполнено некорректно')

    step('Шаг 4: Очистить поле нажатием на крестик')
    f.click_element(BT_receptionMethod)
    time.sleep(2)
    if f.atribut(FD_receptionMethod) == '' and f.enabled(LT_receptionMethod):
        true_step('ОР: - Поле очищено')
        true_step('    - Открыт выпадающий список способов приема')
    else:
        false_step('Ошибка: Поле не очистилось или не отображается выпадающий список')

    step('Шаг 5: Заполнить поле буквами')
    f.contrlA(FD_receptionMethod)
    f.send_keys(FD_receptionMethod, 'Жевать')
    time.sleep(4)
    if f.atribut(FD_receptionMethod) == 'Жевать' and f.text(LT) == 'Жевать':
        true_step('ОР: Происходит фильтрация значений в выпадающем списке способов приема')
    else:
        false_step('Ошибка: Некорректно фильтруется значение в списке либо поле заполнено некорректно')

    step('Шаг 6: Выбрать значение из выпадающего списка')
    f.click_element(LT)
    f.tab(FD_receptionMethod)
    if f.atribut(FD_receptionMethod) == 'Жевать':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено или заполнено некорректно')

    step('Шаг 7: Очистить поле с клавиатуры')
    f.clear_element(FD_receptionMethod)
    f.tab(FD_receptionMethod)
    time.sleep(1)
    if f.atribut(FD_receptionMethod) == '' and f.enabled(LT_receptionMethod):
        true_step('ОР: - Поле очищено')
        true_step('    - Открыт выпадающий список способов приема')
    else:
        false_step('Ошибка: Поле не очистилось или не отображается выпадающий список')

    step('Шаг 8: Заполнить поле символами')
    f.contrlA(FD_receptionMethod)
    f.send_keys(FD_receptionMethod, '!№')
    time.sleep(1)
    if f.text(LT) == 'Совпадений не найдено':
        true_step('ОР: Происходит фильтрация значений в выпадающем списке способов приема. Совпадений не найдено.')
        f.tab(FD_receptionMethod)
    else:
        false_step('Ошибка: Некорректно фильтруется значение в списке')
    if f.atribut(FD_receptionMethod) == '':
        true_step('ОР: Поле не заполнено')
    else:
        false_step('Ошибка: Поле заполнено или заполенно некорректно')

    step('Шаг 9: Заполнить поле символами')
    f.contrlA(FD_receptionMethod)
    f.send_keys(FD_receptionMethod, '12345')
    time.sleep(1)
    if f.text(LT) == 'Совпадений не найдено':
        true_step('ОР: Происходит фильтрация значений в выпадающем списке способов приема. Совпадений не найдено.')
        f.tab(FD_receptionMethod)
    else:
        false_step('Ошибка: Некорректно фильтруется значение в списке')
    if f.atribut(FD_receptionMethod) == '':
        true_step('ОР: Поле не заполнено')
    else:
        false_step('Ошибка: Поле заполнено или заполенно некорректно')


#=====test-cases/601 Проверка обязательности поля "Детализация" при создании назначения лекарственного препарата========
@pytest.mark.regress_tap
def test_19_cases_601():
    case_name('Проверка обязательности поля "Детализация" при создании назначения лекарственного препарата')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Заполнить поле препарат из справочника')
    f.click_element(FD_drug)
    f.send_keys(FD_drug, 'Хлоргексидин, Хлоргексидин, р-р д/наружн. прим., 0.05 %,1000 мл')
    time.sleep(2)
    f.click_element(LT)
    time.sleep(3)
    if f.atribut(FD_drug) != '':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено')

    step('Шаг 3: Проверить, что все обязательные поля заполнены')
    OB_form_purpose()
    time.sleep(2)

    step('Шаг 4: Очистить поле "Детализация" нажатием на крестик')
    f.click_element(BT_details)
    time.sleep(1)
    if f.atribut(FD_details) == '':
        true_step('ОР: Поле очищено')
    else:
        false_step('Ошибка: поле не очистилось')

    step('Шаг 5: Нажать кнопку "Сохранить"')
    f.click_element(BT_save_purpose)
    time.sleep(2)
    if f.backColor(OB_details) == 'rgba(255, 82, 82, 1)' and f.text(ER) == 'Не удалось сохранить назначение':
        true_step('ОР: Появляется уведомление о том, что не удалось добавить назначение, поле "Детализация" подсвечено красным')
    else:
        false_step('Ошибка: Отсутствует уведомление об ошибке сохранения назначения или поле детализация не подсвечено красным')


#===test-cases/605 Проверка обязательности поля "Ед. измерения" при создании назначения лекарственного препарата========
@pytest.mark.regress_tap
def test_20_cases_605():
    case_name('Проверка обязательности поля "Ед. измерения" при создании назначения лекарственного препарата')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Заполнить поле препарат из справочника')
    f.click_element(FD_drug)
    f.send_keys(FD_drug, 'Хлоргексидин, Хлоргексидин, р-р д/наружн. прим., 0.05 %,1000 мл')
    time.sleep(2)
    f.click_element(LT)
    time.sleep(2)
    if f.atribut(FD_drug) != '':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено')

    step('Шаг 3: Проверить, что все обязательные поля заполнены')
    OB_form_purpose()
    time.sleep(1)

    step('Шаг 4: Очистить поле "Ед. измерения"')
    f.clear_element(FD_unit)
    time.sleep(1)
    if f.atribut(FD_unit) == '':
        true_step('ОР: Поле очищено')
    else:
        false_step('Ошибка: Поле не очищено')

    step('Шаг 5: Нажать кнопку "Сохранить"')
    f.click_element(BT_save_purpose)
    time.sleep(2)
    if f.backColor(OB_unit) == 'rgba(255, 82, 82, 1)' and f.text(ER) == 'Не удалось сохранить назначение':
        true_step('ОР: Появляется уведомление о том, что не удалось добавить назначение, поле "Детализация" подсвечено красным')
    else:
        false_step('Ошибка: Отсутствует уведомление об ошибке сохранения назначения или поле детализация не подсвечено красным')


#===test-cases/604 Проверка обязательности поля "Кол-во дней" при создании назначения лекарственного препарата========
@pytest.mark.regress_tap
def test_21_cases_604():
    case_name('Проверка обязательности поля "Кол-во дней" при создании назначения лекарственного препарата')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Заполнить поле препарат из справочника')
    f.click_element(FD_drug)
    f.send_keys(FD_drug, 'Хлоргексидин, Хлоргексидин, р-р д/наружн. прим., 0.05 %,1000 мл')
    time.sleep(2)
    f.click_element(LT)
    time.sleep(3)
    if f.atribut(FD_drug) != '':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено')

    step('Шаг 3: Проверить, что все обязательные поля заполнены')
    OB_form_purpose()
    time.sleep(2)

    step('Шаг 4: Очистить поле "Кол-во дней"')
    f.clear_element(FD_countDay)
    time.sleep(1)
    if f.atribut(FD_countDay) == '1':
        true_step('ОР: Поле не очищается, проставляется "1"')
    else:
        false_step('Ошибка: Поле не очищено')


#===test-cases/603 Проверка обязательности поля "Кол-во на курс" при создании назначения лекарственного препарата=======
@pytest.mark.regress_tap
def test_22_cases_603():
    case_name('Проверка обязательности поля "Кол-во на курс" при создании назначения лекарственного препарата')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Заполнить поле препарат из справочника')
    f.click_element(FD_drug)
    f.send_keys(FD_drug, 'Хлоргексидин, Хлоргексидин, р-р д/наружн. прим., 0.05 %,1000 мл')
    time.sleep(2)
    f.click_element(LT)
    time.sleep(3)
    if f.atribut(FD_drug) != '':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено')

    step('Шаг 3: Проверить, что все обязательные поля заполнены')
    OB_form_purpose()
    time.sleep(2)

    step('Шаг 4: Очистить поле "Количество на курс"')
    f.clear_element(FD_perCourse)
    time.sleep(1)
    if f.atribut(FD_perCourse) == '':
        true_step('ОР: Поле очищено')
    else:
        false_step('Ошибка: Поле не очищено')

    step('Шаг 5: Нажать кнопку "Сохранить"')
    f.click_element(BT_save_purpose)
    time.sleep(2)
    if f.backColor(OB_perCourse) == 'rgba(255, 82, 82, 1)' and f.text(ER) == 'Не удалось сохранить назначение':
        true_step('ОР: Появляется уведомление о том, что не удалось добавить назначение, поле "Детализация" подсвечено красным')
    else:
        false_step('Ошибка: Отсутствует уведомление об ошибке сохранения назначения или поле детализация не подсвечено красным')


#===test-cases/602 Проверка обязательности поля "Путь введения" при создании назначения лекарственного препарата========
@pytest.mark.regress_tap
def test_23_cases_602():
    case_name('Проверка обязательности поля "Путь введения" при создании назначения лекарственного препарата')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Заполнить поле препарат из справочника')
    f.click_element(FD_drug)
    f.send_keys(FD_drug, 'Хлоргексидин, Хлоргексидин, р-р д/наружн. прим., 0.05 %,1000 мл')
    time.sleep(2)
    f.click_element(LT)
    time.sleep(3)
    if f.atribut(FD_drug) != '':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено')

    step('Шаг 3: Проверить, что все обязательные поля заполнены')
    OB_form_purpose()
    time.sleep(2)

    step('Шаг 4: Очистить поле "Путь введения"')
    f.clear_element(FD_way)
    time.sleep(1)
    if f.atribut(FD_way) == '':
        true_step('ОР: Поле очищено')
    else:
        false_step('Ошибка: Поле не очищено')

    step('Шаг 5: Нажать кнопку "Сохранить"')
    f.click_element(BT_save_purpose)
    time.sleep(2)
    if f.backColor(OB_way) == 'rgba(255, 82, 82, 1)' and f.text(ER) == 'Не удалось сохранить назначение':
        true_step('ОР: Появляется уведомление о том, что не удалось добавить назначение, поле "Детализация" подсвечено красным')
    else:
        false_step('Ошибка: Отсутствует уведомление об ошибке сохранения назначения или поле детализация не подсвечено красным')


#==========================test-cases/592 Заполнение полей рецепта. Валидация поля "Врач"===============================
@pytest.mark.regress_tap
def test_24_cases_592():
    case_name('Заполнение полей рецепта. Валидация поля "Врач"')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Выбрать назначение из списка или создать новое')
    test_1_cases_create_purpose()
    true_step('ОР: - Назначение выбрано/Создано')
    if f.enabled(BT_add_recipe):
        true_step('    - Кнопка "Добавить" в блоке "Рецепты" стала доступна')
    else:
        false_step('Ошибка: Кнопка добавить в блоке "Рецепты" недоступна')

    step('Шаг 2: Нажать на кнопку "Добавить" в блоке "Рецепты"')
    f.click_element(BT_add_recipe)
    time.sleep(3)
    if f.enabled(FM_recipe):
        true_step('ОР: Открылась форма создания рецептов')
    else:
        false_step('Ошибка: Форма создания рецепта недоступна')

    step('Шаг 3: Выбрать чек-бокс "Коммерческий"')
    f.click_element(CH_comm)
    time.sleep(2)
    if f.enabled(CH_comm):
        true_step('ОР: Чек-бокс выбран')
    else:
        false_step('Ошибка: Чек- бокс не выбран')

    step('Шаг 4: Проверить, что поле "Врач" заполнено автоматически текущим врачом')
    name = '2372 - Гиппократ Ирина Константиновна'
    if f.atribut(FD_doctor_recipe) == name:
        true_step('ОР: Поле заполнено автоматически')
    else:
        false_step('Ошибка: Поле не заполнено или заполнено некорректно')

    step('Шаг 5: Очистить поле "Врач" с клавиатуры')
    f.clear_element(FD_doctor_recipe)
    f.tab(FD_doctor_recipe)
    time.sleep(1)
    if f.atribut(FD_doctor_recipe) == '' and f.backColor(OB_doctor_recipe) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Поле не очищено или нет обязательности')

    step('Шаг 6: Начать заполнять поле существующим в списке значением с клавиатуры')
    f.send_keys(FD_doctor_recipe, name)
    time.sleep(1)
    if f.atribut(FD_doctor_recipe) == name and f.text(LT) == name:
        true_step('ОР: - Поле заполнено')
        true_step('    - Происходит фильтрация значений в выпадающем списке')
        true_step('    - Отображается найденное значение')
    else:
        false_step('Ошибка: Поле не заполнено или фильтрация происходит некорректно')

    step('Шаг 7: Очистить поле "Врач" нажатием на крестик')
    f.click_element(BT_clear_doctor_recipe)
    f.tab(FD_doctor_recipe)
    time.sleep(2)
    if f.atribut(FD_doctor_recipe) == '' and f.backColor(OB_doctor_recipe) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным')
    else:
        false_step('Ошибка: Поле не очистилось или нет обязательности')

    step('Шаг 8: Ввести в поле невалидное значение и кликнуть в пустом месте формы')
    f.send_keys(FD_doctor_recipe, 'Невалидное значение')
    time.sleep(1)
    if f.text(LT) == 'Совпадений не найдено':
        f.tab(FD_doctor_recipe)
        time.sleep(2)
    else:
        false_step('Ошибка: Фильтрация происходит некорректно')
    if f.atribut(FD_doctor_recipe) == '' and f.backColor(OB_doctor_recipe) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: -В выпадающем списке отображается "Совпадений не найдено"')
        true_step('    - После клика поле очищено и подсвечено красным')
    else:
        false_step('Ошибка: Поле не очистилось или очистилось некорректно')


#=========================test-cases/593 Заполнение полей рецепта. Валидация поля "Дата выписки"========================
@pytest.mark.regress_tap
def test_25_cases_593():
    case_name('Заполнение полей рецепта. Валидация поля "Дата выписки"')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Выбрать назначение из списка или создать новое')
    test_1_cases_create_purpose()
    true_step('ОР: - Назначение выбрано/Создано')
    if f.enabled(BT_add_recipe):
        true_step('    - Кнопка "Добавить" в блоке "Рецепты" стала доступна')
    else:
        false_step('Ошибка: Кнопка добавить в блоке "Рецепты" недоступна')

    step('Шаг 2: Нажать на кнопку "Добавить" в блоке "Рецепты"')
    f.click_element(BT_add_recipe)
    time.sleep(3)
    if f.enabled(FM_recipe):
        true_step('ОР: Открылась форма создания рецептов')
    else:
        false_step('Ошибка: Форма создания рецепта недоступна')

    step('Шаг 3: Выбрать чек-бокс "Коммерческий"')
    f.click_element(CH_comm)
    time.sleep(2)
    if f.enabled(CH_comm):
        true_step('ОР: Чек-бокс выбран')
    else:
        false_step('Ошибка: Чек- бокс не выбран')

    step('Шаг 4: Проверить, что поле "Дата выписки" заполнено автоматически текущей датой')
    date = (DT.strftime('%d.%m.%Y'))
    if f.atribut(FD_date) == date:
        true_step(f'ОР: Поле "Дата выписки" заполнено текущей датой {date}')
    else:
        false_step('Ошибка: Поле "Дата выписки" заполнено некорректно по умолчанию')

    step('Шаг 5: Очистить поле "Дата выписки" с клавиатуры')
    f.clear_delete(FD_date)
    time.sleep(2)
    f.tab(FD_date)
    time.sleep(2)
    if f.atribut(FD_date) == '' and f.backColor(OB_date) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Поле не очистилось или нет обязательности')

    step('Шаг 6: Нажать на календарь и выбрать дату выписки')
    f.click_element(BT_date)
    time.sleep(1)
    # Получаю вчерашний день в формате: только число/день
    day = (DT - timedelta(days=1)).strftime('%d')
    f.searchDay(CL_date, day)
    time.sleep(3)

    step('Шаг 7: Очистить поле "Дата выписки" с клавиатуры')
    f.clear_delete(FD_date)
    f.tab(FD_date)
    time.sleep(1)
    if f.atribut(FD_date) == '' and f.backColor(OB_date) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Поле не очистилось или нет обязательности')

    step('Шаг 8: Заполнить поле "Дата выписки" цифрами с клавиатуры')
    newDate = (DT - timedelta(days=4)).strftime('%d.%m.%Y')
    f.send_keys(FD_date, newDate)
    f.tab(FD_date)
    time.sleep(1)
    if f.atribut(FD_date) == newDate:
        true_step('ОР: Поле заполнено корректно')
    else:
        false_step('Ошибка: Поле "Дата начала" заполнилось некорректно')

    step('Шаг 9: Очистить поле "Дата выписки" с клавиатуры')
    f.clear_delete(FD_date)
    f.tab(FD_date)
    time.sleep(1)
    if f.atribut(FD_date) == '' and f.backColor(OB_date) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищено и подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Поле не очистилось или нет обязательности')

    step('Шаг 10: Заполнить поле "Дата выписки" буквами с клавиатуры')
    f.send_keys(FD_date, 'буквы')
    f.tab(FD_date)
    time.sleep(1)
    if f.atribut(FD_date) == '' and f.backColor(OB_date) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле заполнено корректно')
    else:
        false_step('Ошибка: Поле "Дата начала" заполнилось некорректно')

    step('Шаг 11: Заполнить поле "Дата выписки" с клавиатуры символами')
    f.send_keys(FD_date, '!№;%:')
    f.tab(FD_date)
    time.sleep(1)
    if f.atribut(FD_date) == '' and f.backColor(OB_date) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле заполнено корректно')
    else:
        false_step('Ошибка: Поле "Дата начала" заполнилось некорректно')


#=====test-cases/631 Проверка возможности редактирования назначения лекарственного препарата в статусе "Подписано"======
@pytest.mark.regress_tap
def test_26_cases_631():
    case_name('Проверка возможности редактирования назначения лекарственного препарата в статусе "Подписано"')
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать в списке назначений на назначение лекарственного препарата в статусе "Подписано"')
    f.clickStateGrid(ST_all_purpose_grid, BT_next, 'Подписано')
    if f.enabled(FM_purpose):
        true_step('ОР: Открывается форма, аналогичная форме создания назначения')
    else:
        false_step('Ошибка: Форма создания назначения недоступна')
    time.sleep(5)

    step('Шаг 2: Проверить, что все обязательные поля заполнены и недоступны для редактирования')
    OB_form_purpose_signed()


#=======test-cases/600 Проверка обязательности поля "Врач" при создании назначения лекарственного препарата=============
@pytest.mark.regress_tap
def test_27_cases_600():
    case_name('Проверка обязательности поля "Врач" при создании назначения лекарственного препарата')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Заполнить поле препарат для добавления назначения')
    #Кликаю по полю "Препарат"
    f.click_element(FD_drug)
    f.send_keys(FD_drug, 'Хлоргексидин, Хлоргексидин, р-р д/наружн. прим., 0.05 %,1000 мл')
    time.sleep(1)
    f.click_element(LT)
    time.sleep(2)
    if f.atribut(FD_drug) != '':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено')

    step('Шаг 3: Проверить, что все обязательные поля заполнены')
    OB_form_purpose() #Вызываю функцию проверки обязательных полей формы

    step('Шаг 4: Очистить поле "Врач" нажатием на крестик')
    f.click_element(BT_clear_doctor)
    time.sleep(1)
    f.tab(FD_doctor)
    if f.atribut(FD_doctor) == '':
        true_step('ОР: Поле очищено')
    else:
        false_step('Ошибка: Поле не очистилось')

    step('Шаг 5: Нажать кнопку "Сохранить"')
    f.click_element(BT_save_purpose)
    time.sleep(1)
    if f.text(ER) == 'Не удалось сохранить назначение' and f.backColor(OB_doctor) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Появляется уведомление "Не удалось сохранить назначение", поле "Врач" подсвечено красным')
    else:
        false_step('Ошибка: отсутствует уведомление или обязательность поля')


#===========test-cases/612 Валидация поля "Путь введения" при создании назначения лекарственного препарата==============
@pytest.mark.regress_tap
def test_28_cases_612():
    case_name('Валидация поля "Путь введения" при создании назначения лекарственного препарата')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Нажать на поле "Путь введения" для заполнения')
    f.click_element(FD_way)
    time.sleep(1)
    if f.enabled(LT_Way) and f.backColor(OB_way) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: -Поле подсвечено красным, как обязательное для заполнения')
        true_step('    -Открыт выпадающий список путей введения')
    else:
        false_step('Ошибка: Отсутсвует обязательность поля или выпадающий список')

    step('Шаг 3: Выбрать значение из выпадающего списка')
    f.click_element(LT)
    time.sleep(1)
    if f.atribut(FD_way) != '':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено')

    step('Шаг 4: Очистить поле нажатием на крестик')
    f.click_element(BT_clear_way)
    time.sleep(1)
    if f.enabled(LT_Way) and f.backColor(OB_way) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: -Поле подсвечено красным, как обязательное для заполнения')
        true_step('    -Открыт выпадающий список путей введения')
    else:
        false_step('Ошибка: Отсутсвует обязательность поля или выпадающий список')

    step('Шаг 5: Начать заполнять поле буквами')
    f.send_keys(FD_way, 'Местно')
    time.sleep(1)
    if f.text(LT) == 'Местно':
        true_step('ОР: Происходит фильтрация значений в выпадающем списке путей введения')
    else:
        false_step('Ошибка: Фильтрация не происходит')

    step('Шаг 6: Выбрать значение из выпадающего списка')
    f.click_element(LT)
    time.sleep(1)
    f.tab(FD_way)
    if f.atribut(FD_way) == 'Местно':
        true_step('ОР: Поле заполнено')
    else:
        false_step('Ошибка: Поле не заполнено или заполнено некорректно')

    step('Шаг 7: Очистить поле с клавиатуры')
    f.clear_delete(FD_way)
    time.sleep(1)
    if f.enabled(LT_Way) and f.backColor(OB_way) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: -Поле подсвечено красным, как обязательное для заполнения')
        true_step('    -Открыт выпадающий список путей введения')
    else:
        false_step('Ошибка: Отсутсвует обязательность поля или выпадающий список')

    step('Шаг 8: Заполнить поле символами и нажать на пустое место')
    f.send_keys(FD_way, '!@&^%$')
    f.tab(FD_way)
    time.sleep(1)
    if f.backColor(OB_way) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: -Поле подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Отсутсвует обязательность поля или выпадающий список')

    step('Шаг 9: Заполнить поле цифрами и нажать на пустое место')
    f.send_keys(FD_way, '12345')
    f.tab(FD_way)
    time.sleep(1)
    if f.backColor(OB_way) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: -Поле подсвечено красным, как обязательное для заполнения')
    else:
        false_step('Ошибка: Отсутсвует обязательность поля или выпадающий список')


#=========test-cases/667 Создание назначения со значением поля "Дата назначения" равным больше текущей даты=============
@pytest.mark.regress_tap
def test_29_cases_667():
    case_name('Создание назначения со значением поля "Дата назначения" равным больше текущей даты')
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Нажать кнопку "Добавить"')
    f.click_element(BT_add_purpose)
    time.sleep(3)
    if f.enabled(FM_purpose):
        true_step('ОР: - Открывается форма ввода данных нового назначения')
    else:
        false_step('Ошибка: Форма назначения недоступна')
    if f.enabled(CL_medicament):
        true_step('    - По умолчанию открывается вкладка "Лекарственный препарат"')
    else:
        false_step('Ошибка: Не выбрана вкладка "Лекарственный препарат" по умолчанию')

    step('Шаг 2: Проверить, что поле "Дата назначения" заполнено автоматически текущей датой')
    if f.atribut(FD_date_purpose) == DT.strftime('%d.%m.%Y'):
        true_step('ОР: Поле "Дата назначения" по умолчанию заполнена текущей датой')
    else:
        false_step('Ошибка: Значение в поле "Дата назначения" НЕ содержит текущую дату')

    step('Шаг 3: Очистить поле "Дата назначения" с клавиатуры')
    f.clear_delete(FD_date_purpose)
    f.tab(FD_date_purpose)
    time.sleep(1)
    if f.atribut(FD_date_purpose) == '' and f.backColor(OB_date_purpose) == 'rgba(255, 82, 82, 1)':
        true_step('ОР: Поле очищается и подсвечено красным как обязательное')
    else:
        false_step('Ошибка: Поле не очистилось или отсутствует обязательность')

    step('Шаг 4: Нажать на календарь и выбрать дату назначения больше текущей')
    f.click_element(BT_date_purpose)
    time.sleep(1)
    day = (DT + timedelta(days=1)).strftime('%d')
    f.searchDay(CL_date, day)
    time.sleep(2)

    step('Шаг 5: Заполнить  обязательные поля')
    f.send_keys(FD_drug, 'Хлоргексидин, Хлоргексидин, р-р д/наружн. прим., 0.05 %,1000 мл')
    time.sleep(1)
    f.click_element(LT)
    time.sleep(2)
    OB_form_purpose()

    step('Шаг 6: Нажать кнопку "Сохранить"')
    f.click_element(BT_save_purpose)
    time.sleep(2)
    if f.text(ER) == 'Не удалось сохранить назначение':
        true_step('ОР: Появляется уведомление "Не удалось сохранить назначение"')
    else:
        false_step('Ошибка: отсутствует уведомление об ошибке')

    step('Шаг 7: Проверить в гриде, что назначение не было создано')
    f.getNullGrid(ST_purpose_grid, BT_next, 'Редактируется')


#=================================test-cases/662 Отмена рецепта до подписания===========================================
@pytest.mark.regress_tap
def test_30_cases_662():
    case_name('Отмена рецепта до подписания')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)

    step('Шаг 1: Выбрать назначение из списка или создать новое')
    test_1_cases_create_purpose()
    true_step('ОР: - Назначение выбрано/Создано')
    if f.enabled(BT_add_recipe):
        true_step('    - Кнопка "Добавить" в блоке "Рецепты" стала доступна')
    else:
        false_step('Ошибка: Кнопка добавить в блоке "Рецепты" недоступна')

    step('Шаг 2: Нажать на кнопку "Добавить" в блоке "Рецепты"')
    f.click_element(BT_add_recipe)
    time.sleep(4)
    if f.enabled(FM_recipe):
        true_step('ОР: Открылась форма создания рецептов')
    else:
        false_step('Ошибка: Форма создания рецепта недоступна')

    step('Шаг 3: Выбрать чек-бокс "Коммерческий"')
    f.click_element(CH_comm)
    time.sleep(2)
    if f.enabled(CH_comm):
        true_step('ОР: Чек-бокс выбран')
    else:
        false_step('Ошибка: Чек- бокс не выбран')

    step('Шаг 4: Проверить автоматическое заполнение обязательных полей и доступность')
    OB_form_recipe_commerchesky()

    step('Шаг 5: Установить признак "Электронный"')
    f.click_element(CH_electronic_recipe)
    if f.enabled(CH_electronic_recipe):
        true_step('ОР: Признак установлен')
    else:
        false_step('Ошибка: Радиокнопка не выбрана')

    step('Шаг 6: Нажать на кнопку "Сохранить"')
    f.click_element(BT_save_recipe)
    time.sleep(3)
    if f.text(ER) == 'Рецепт успешно сохранен':
        true_step('ОР: Рецепт сохранен')
    else:
        false_step('Ошибка: Отсутствует сообщение об успешном сохранении')

    step('Шаг 7: У рецепта нажать кнопку "Отменить"')
    time.sleep(6)
    f.click_element(BT_cancel_recipe)
    time.sleep(3)
    if f.text(CL_crid_recipe_text) == 'Нет данных для отображения':
        true_step('ОР: Рецепт удален')
    else:
        false_step('Ошибка: Рецепт отображается в гриде')


#===========test-cases/636 Проверка поля "Льгота" при выписке рецепта для пациента с одной льготой======================
@pytest.mark.regress_tap
def test_31_cases_636():
    case_name('Проверка поля "Льгота" при выписке рецепта для пациента с одной льготой')

    step('Шаг 1: Выбрать назначение из списка или создать новое')
    # Перехожу по ссылке в ТАП
    browser.get(url_1Lgot_TAP)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)
    time.sleep(4)
    # Кликаю кнопку "Добавить" в блоке "Назначения"
    f.click_element(BT_add_purpose)
    time.sleep(4)
    # Кликаю по полю "Препарат"
    f.click_element(FD_drug)
    # Ввожу в поле название препарата
    f.send_keys(FD_drug, 'Хлоргексидин, Хлоргексидин, р-р д/наружн. прим., 0.05 %,1000 мл')
    time.sleep(1)
    # Выбираю и кликаю по первому элементу выпадающего списка поля "Препарат"
    f.click_element(LT)
    time.sleep(3)
    # Кликаю кнопку "Подписать"
    f.click_element(BT_signature_path)
    time.sleep(6)
    true_step('ОР: - Назначение выбрано/Создано')
    if f.enabled(BT_add_recipe):
        true_step('    - Кнопка "Добавить" в блоке "Рецепты" стала доступна')
    else:
        false_step('Ошибка: Кнопка добавить в блоке "Рецепты" недоступна')

    step('Шаг 2: Нажать на кнопку "Добавить" в блоке "Рецепты"')
    f.click_element(BT_add_recipe)
    time.sleep(4)
    if f.enabled(FM_recipe):
        true_step('ОР: Открылась форма создания рецептов')
    else:
        false_step('Ошибка: Форма создания рецепта недоступна')

    step('Шаг 3: Проверить, что по умолчанию выбрана радиокнопка  "Льготный"')
    if f.is_selected(CH_privilege) and f.enabled(CH_privilege):
        true_step('ОР: Радиокнопка выбрана по умолчанию и доступна')
    else:
        false_step('Ошибка: Радиокнопка не выбрана')

    step('Шаг 4: Проверить, что поле "Льгота" заполнено автоматически действующей льготой')
    if f.atribut(FD_privilege) == '554 - Члены семьи погибшего участника СВО':
        true_step('ОР: Поле заполнено автоматически действующей льготой')
    else:
        false_step('Ошибка: Поле не заполнено или заполнено некорреткно')


#=================================test-cases/661 Отмена рецепта после подписания===========================================
@pytest.mark.regress_tap
def test_32_cases_661():
    case_name('Отмена рецепта после подписания')
    #Перехожу по ссылке в ТАП
    browser.get(url_TAP)
    browser.implicitly_wait(20)

    f = ContractsPage(browser)

    step('Шаг 1: Выбрать назначение из списка или создать новое')
    test_1_cases_create_purpose()
    true_step('ОР: - Назначение выбрано/Создано')
    if f.enabled(BT_add_recipe):
        true_step('    - Кнопка "Добавить" в блоке "Рецепты" стала доступна')
    else:
        false_step('Ошибка: Кнопка добавить в блоке "Рецепты" недоступна')

    step('Шаг 2: Нажать на кнопку "Добавить" в блоке "Рецепты"')
    f.click_element(BT_add_recipe)
    time.sleep(4)
    if f.enabled(FM_recipe):
        true_step('ОР: Открылась форма создания рецептов')
    else:
        false_step('Ошибка: Форма создания рецепта недоступна')

    step('Шаг 3: Выбрать чек-бокс "Коммерческий"')
    f.click_element(CH_comm)
    time.sleep(2)
    if f.enabled(CH_comm):
        true_step('ОР: Чек-бокс выбран')
    else:
        false_step('Ошибка: Чек- бокс не выбран')

    step('Шаг 4: Проверить автоматическое заполнение обязательных полей и доступность')
    OB_form_recipe_commerchesky()

    step('Шаг 5: Установить признак "Электронный"')
    f.click_element(CH_electronic_recipe)
    if f.enabled(CH_electronic_recipe):
        true_step('ОР: Признак установлен')
    else:
        false_step('Ошибка: Радиокнопка не выбрана')

    step('Шаг 6: Нажать на кнопку "Сохранить"')
    f.click_element(BT_save_recipe)
    time.sleep(3)
    if f.text(ER) == 'Рецепт успешно сохранен':
        true_step('ОР: Рецепт сохранен')
    else:
        false_step('Ошибка: Отсутствует сообщение об успешном сохранении')

    step('Шаг 7: Нажать на кнопку "Подпись врача"')
    f.click_element(BT_caption_recipe)
    time.sleep(5)
    if f.element_absent(BT_caption_recipe) and f.atribut(ST_recipe_grid) == 'Сформирован':
        true_step('ОР: Рецепт подписан. Кнопка "Подпись врача" стала недоступной.')
    else:
        false_step('Ошибка: Рецепт не подписан')

    step('Шаг 8: У рецепта нажать кнопку "Отменить"')
    time.sleep(6)
    f.click_element(BT_cancel_recipe)
    time.sleep(3)
    if f.text(CL_crid_recipe_text) == 'Нет данных для отображения':
        true_step('ОР: Рецепт удален')
    else:
        false_step('Ошибка: Рецепт отображается в гриде')





