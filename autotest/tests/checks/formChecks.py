#====================================Функции для проверки полей форм====================================================

from autotest.tests.config.function import *
#==========================================Форма назначения ТАП=========================================================


    #==========Функция проверки заполнения обязательных полей формы назначения в статусе 'Редактируется'================
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



    #==============Функция проверки заполнения обязательных полей формы назначения в статусе 'Подписано'================
def OB_form_purpose_signed():
    f = ContractsPage(browser)
    all_fields_filled = True

    if f.atribut(FD_drug) == '' or f.enabled(FD_drug):
        false_step('Ошибка: Поле "Препарат" не заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_mnn) == '' or f.enabled(FD_mnn):
        false_step('Ошибка: Поле "МНН" не заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_trn) == '' or f.enabled(FD_trn):
        false_step('Ошибка: Поле "Торговое" не заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_dosageform) == '' or f.enabled(FD_dosageform):
        false_step('Ошибка: Поле "Лекарственная форма" не заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_dose) == '' or f.enabled(FD_dose):
        false_step('Ошибка: Поле "Дозировка" не заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_singleDose) == '' or f.enabled(FD_singleDose):
        false_step('Ошибка: Поле "Разовая доза" не заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_unit) == '' or f.enabled(FD_unit):
        false_step('Ошибка: Поле "Ед. измерения" не заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_onceADay) == '' or f.enabled(FD_onceADay):
        false_step('Ошибка: Поле "Раз в день" не заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_countDay) == '' or f.enabled(FD_countDay):
        false_step('Ошибка: Поле "Количество дней" не заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_perCourse) == '' or f.enabled(FD_perCourse):
        false_step('Ошибка: Поле "Количество на курс" не заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_receptionMethod) == '' or f.enabled(FD_receptionMethod):
        false_step('Ошибка: Поле "Способ введения" не заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_way) == '' or f.enabled(FD_way):
        false_step('Ошибка: Поле "Путь введени" не заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_details) == '' or f.enabled(FD_details):
        false_step('Ошибка: Поле "Детализация" не заполнено или доступно для редактирования')
        all_fields_filled = False
    if all_fields_filled:
        true_step('ОР: Обязательные поля заполнены и недоступны для редактирования')






#============================================Форма рецепта ТАП==========================================================


    #Функция проверки доступности полей рецепта при выбранном чек-боксе "Коммерческий"
def OB_form_recipe_commerchesky():
    f = ContractsPage(browser)
    all_fields_filled = True


    if f.atribut(FD_privilege) != '' or f.enabled(FD_privilege):
        false_step('Ошибка: Поле "Льгота" заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_source_of_financing) != '' or f.enabled(FD_source_of_financing):
        false_step('Ошибка: Поле "Источник финансирования" заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_percentage_of_payment) != '' or f.enabled(FD_percentage_of_payment):
        false_step('Ошибка: Поле "% оплаты" заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_type_form) == '' or f.enabled(FD_type_form):
        false_step('Ошибка: Поле "Тип формы" не заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_series) != '' or f.enabled(FD_series):
        false_step('Ошибка: Поле "Серия" заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_number) != '' or f.enabled(FD_number):
        false_step('Ошибка: Поле "Номер" заполнено или доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_period_of_validity) == '' or f.disabled(FD_period_of_validity):
        false_step('Ошибка: Поле "Срок действия" не заполнено или не доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_date) == '' or f.disabled(FD_period_of_validity):
        false_step('Ошибка: Поле "Дата выписки" не заполнено или не доступно для редактирования')
        all_fields_filled = False
    if f.atribut(FD_doctor_recipe) == '' or f.disabled(FD_doctor_recipe):
        false_step('Ошибка: Поле "Врач" не заполнено или не доступно для редактирования')
        all_fields_filled = False
    if all_fields_filled:
        true_step('ОР: Обязательные поля заполнены, доступность полей корректна')