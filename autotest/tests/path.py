#=================В этом файле находятся локаторы элементов ТАП==============================

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from datetime import datetime, timedelta

chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension('C:/Users/Арутюн/AppData/Local/Google/Chrome/User Data/component_crx_cache/eeigpngbgcognadeebkilcpcaedhellh_1.c64c9c1008f3ba5f6e18b3ca524bc98dcd8acfae0a2720a8f1f3ef0f8d643d05')
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()


#====================================Ссылка на ТАП==============================================
url_TAP = 'http://192.168.7.218/test/statist/purpose/3648973/523452F6-124E-4D63-94C4-012D71072FD3/2023-01-17T00:00:00/jZ3zgDedI7%2BnkR5IPdNbH%2FYaNpaXLi%2Fq3URuK4TMHjdxRovpj%2BuRfl6d5R9UdVJHkXRZNYvHAKwdlRjlu0Ry2BmWuoW3v3%2BWj5a3V%2BfC%2FjDZJgEYe9bA93Tw2knvaQ9x2du9y3JXxlsvzoYAApnrPZPYTq07wrMBXF1882SI8vY6JxyPkd8P1pLYKURqhCzaU7toAm0X30QzqDPL2XbUx3HhaHGpwiY0%2Bu%2Fp%2BZzQJd9jmmRXr7jdejb5a%2Bb0aRKixcOw2lrUv5TqE0NJWaFFLKMOdaw%2BBqk4T2Gk0d0DAUEgkH%2BihWJDogj2SMAjs%2FcdW5F5YA%3D%3D?ticket=jZ3zgDedI7%2BnkR5IPdNbH%2FYaNpaXLi%2Fq3URuK4TMHjdxRovpj%2BuRfl6d5R9UdVJHkXRZNYvHAKwdlRjlu0Ry2BmWuoW3v3%2BWj5a3V%2BfC%2FjDZJgEYe9bA93Tw2knvaQ9x2du9y3JXxlsvzoYAApnrPZPYTq07wrMBXF1882SI8vY6JxyPkd8P1pLYKURqhCzaU7toAm0X30QzqDPL2XbUx3HhaHGpwiY0%2Bu%2Fp%2BZzQJd9jmmRXr7jdejb5a%2Bb0aRKixcOw2lrUv5TqE0NJWaFFLKMOdaw%2BBqk4T2Gk0d0DAUEgkH%2BihWJDogj2SMAjs%2FcdW5F5YA%3D%3D&DocPrvdId=2000&MisUrl=https:%2F%2Ftest.2dr.ru%2Fdemo&ReturnUrl=http:%2F%2Ftest.2dr.ru%2Fdemo%2FTap'

#====================================Ссылка на ТАП пациент с 1 льготой==============================================
url_1Lgot_TAP = 'http://192.168.7.218/test/statist/purpose/3649164/523452F6-124E-4D63-94C4-012D71072FD3/2023-01-17T00:00:00/jZ3zgDedI7%2BnkR5IPdNbH%2FYaNpaXLi%2Fq3URuK4TMHjdxRovpj%2BuRfl6d5R9UdVJHkXRZNYvHAKwdlRjlu0Ry2BmWuoW3v3%2BWj5a3V%2BfC%2FjDZJgEYe9bA93Tw2knvaQ9x2du9y3JXxlsvzoYAApnrPZPYTq07wrMBXF1882SI8vY6JxyPkd8P1pLYKURqhCzaU7toAm0X30QzqDPL2XbUx3HhaHGpwiY0%2Bu%2Fp%2BZzQJd9jmmRXr7jdejb5a%2Bb0aRKixcOw2lrUv5TqE0NJWaFFLKMOdaw%2BBqk4T2Gk0d0DAUEgkH%2BihWJDogj2SMAjs%2FcdW5F5YA%3D%3D?ticket=jZ3zgDedI7%2BnkR5IPdNbH%2FYaNpaXLi%2Fq3URuK4TMHjdxRovpj%2BuRfl6d5R9UdVJHkXRZNYvHAKwdlRjlu0Ry2BmWuoW3v3%2BWj5a3V%2BfC%2FjDZJgEYe9bA93Tw2knvaQ9x2du9y3JXxlsvzoYAApnrPZPYTq07wrMBXF1882SI8vY6JxyPkd8P1pLYKURqhCzaU7toAm0X30QzqDPL2XbUx3HhaHGpwiY0%2Bu%2Fp%2BZzQJd9jmmRXr7jdejb5a%2Bb0aRKixcOw2lrUv5TqE0NJWaFFLKMOdaw%2BBqk4T2Gk0d0DAUEgkH%2BihWJDogj2SMAjs%2FcdW5F5YA%3D%3D&DocPrvdId=2000&MisUrl=https:%2F%2Ftest.2dr.ru%2Fdemo&ReturnUrl=http:%2F%2Ftest.2dr.ru%2Fdemo%2FTap'

#====================================Текущая дата и время=======================================
DT = datetime.now()     # Формат даты: '%d/%m/%Y',
                        # формат времени: '%H:%M:%S'

#====================================Локатор всплывающего окна ошибки===========================
ER = (By.XPATH, "//div[@class='snackbar-text-wrapper']")

#Локатор кнопки числа даты в календаре (Выбор числа в календаре, указав value = 12 например)
CL_date = (By.CSS_SELECTOR, '.mat-calendar-body-cell-content.mat-focus-indicator')



#====================================Локаторы блока/формы "Назначения" в ТАП============================================

    #Локатор кнопки "Добавить"
BT_add_purpose = (By.CSS_SELECTOR, '.btn-panel.ng-star-inserted')

    #Локатор формы назначения
FM_purpose = (By.ID, 'appointmentAdding')

    #Локатор поля "Препарат"
FD_drug = (By.XPATH, '//*[@id="mat-input-12"]')

    #Локатор первого элемента выпадающего списка
LT = (By.CSS_SELECTOR, '.mat-option-text')

    #Локатор кнопки "Подписать"
BT_signature_path = (By.XPATH, '//*[@id="appointmentAdding"]/appointment-add/div[1]/div/div/mat-card/div[2]/div/div[3]')

    #Локатор выбранного назначения в гриде
CL_purpose_grid = (By.CSS_SELECTOR, '#appointment > app-appointment > div > div:nth-child(3) > div > div > app-st-table > div > table > tbody > tr.mat-mdc-row.mdc-data-table__row.cdk-row.example-element-row.cursorPointer.row-element.ng-star-inserted.select-row')

    #Локатор статуса выбранного назначения в гриде
ST_purpose_grid = (By.CSS_SELECTOR, '.mat-mdc-row.mdc-data-table__row.cdk-row.example-element-row.cursorPointer.row-element.ng-star-inserted.select-row > td.mat-mdc-cell.mdc-data-table__cell.cdk-cell.cdk-column-appointmentCardNum.mat-column-appointmentCardNum.appointment__row.ng-star-inserted')

    #Локатор всех статусов назначений в гриде
ST_all_purpose_grid = (By.CSS_SELECTOR, '.mat-mdc-cell.mdc-data-table__cell.cdk-cell.cdk-column-appointmentCardNum.mat-column-appointmentCardNum.appointment__row.ng-star-inserted')

    #Локатор кнопки "Отменить"
BT_cancel = (By.XPATH, '//*[@id="appointmentAdding"]/appointment-add/div[1]/div/div/mat-card/div[3]/div/div/button')

    #Локатор чек-бокса "Резистентность к ЛС"
CH_rez = (By.XPATH, '//*[@id="appointmentAdding"]/appointment-add/div[1]/div/div/mat-card/div[2]/div[1]')

    #Локатор чек-бокса "Резистентность к ЛС" выбранного
CH_rez_true = (By.CSS_SELECTOR, '.mdc-checkbox__native-control.mdc-checkbox--selected')

    #Локатор поля "Комментарий" при отмене назначения
FD_comments = (By.XPATH, '//*[@id="appointmentAdding"]/appointment-add/div[1]/div/div/mat-card/div[2]/div[2]/mat-form-field/div/div[1]/div/input')

    #Локатор кнопки "Сохранить" при отмене назначения
BT_save_cancel = (By.XPATH, '//*[@id="appointmentAdding"]/appointment-add/div[1]/div/div/mat-card/div[5]/div/div[2]/button')

    #Локатор кнопки "Сохранить"
BT_save_purpose = (By.XPATH, '//*[@id="appointmentAdding"]/appointment-add/div[1]/div/div/mat-card/div[2]/div/div[2]/button')

    #Локатор статуса назначения в форме назначения
ST_purpose = (By.XPATH, '//*[@id="appointmentAdding"]/appointment-add/div[1]/div/div/mat-card/div[1]/div/h2/span[2]')

CH_rez_of = (By.XPATH, "//input[contains(@class, 'mdc-checkbox--selected')][@disabled]")

    #Локатор вкладки "Лекарственный препарат"
CL_medicament = (By.CSS_SELECTOR, '.mdc-tab.mat-mdc-tab.mat-mdc-focus-indicator.ng-star-inserted.mdc-tab--active.mdc-tab-indicator--active')

    #Локатор поля "Время"
FD_time = (By.CSS_SELECTOR, '.mat-input-element.mat-form-field-autofill-control.mat-mdc-tooltip-trigger.ng-tns-c11-30.ng-touched.ng-pristine.cdk-text-field-autofill-monitored.ng-valid')

    #Локатор поля ввода "Врач"
FD_doctor = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-17 > input')

    #Локатор выпадающего списка поля "Врач"
LT_doctor_list = (By.CSS_SELECTOR, '.mat-autocomplete-panel.mat-primary.ng-star-inserted.mat-autocomplete-visible')

    #Локатор первого элемента выпадающего списка поля "Врач"
LT_doctor = (By.CSS_SELECTOR, '.mat-option.mat-focus-indicator.mat-tooltip-trigger.ng-star-inserted.mat-active > span')

    #Локатор крестика очистки поля "Врач"
BT_clear_doctor = (By.CSS_SELECTOR, '.mat-form-field-suffix.ng-tns-c11-17.ng-star-inserted > div > button')

    #Локатор обязательности поля "Врач" (подсвеченность красным)
OB_doctor = (By.CSS_SELECTOR, '.mat-form-field-ripple.ng-tns-c11-17')

    #Локатор поля "Дата начала"
FD_startDate = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-34 > input')

    #Локатор кнопки числа даты начала в календаре (Выбор числа в календаре, указав value = 12 например)
CL_startDate = (By.CSS_SELECTOR, '.mat-calendar-body-cell-content.mat-focus-indicator')

    #Локатор кнопки открытия календаря поля "Дата начала"
BT_startDate = (By.CSS_SELECTOR, '.mat-datepicker-toggle.ng-tns-c11-34.ng-star-inserted > button')

    #Локатор поля "Детализация"
FD_details = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-23 > input')

    #Локатор крестика очистки поля "Детализация"
BT_details = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-23 > button')

    #Локатор обязательности поля "Детализация" (подсвеченность красным)
OB_details = (By.CSS_SELECTOR, '.mat-form-field-ripple.ng-tns-c11-23')

    #Локатор поля "Ед. измерения"
FD_unit = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-22 > input')

    #Локатор обязательности поля "Ед. измерения" (подсвеченность красным)
OB_unit = (By.CSS_SELECTOR, '.mat-form-field-ripple.ng-tns-c11-22')

    #Локатор поля "Количество дней"
FD_countDay = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-12 > input')

    #Локатор поля "Количество на курс"
FD_perCourse = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-13 > input')

    #Локатор обязательности поля "Количество на курс" (подсвеченность красным)
OB_perCourse = (By.CSS_SELECTOR, '.mat-form-field-underline.ng-tns-c11-13.ng-star-inserted > span')

    #Локатор поля "Обоснование назначения"
FD_rationalDose = (By.CSS_SELECTOR, '#mat-input-8')

    #Локатор поля "Раз в день"
FD_onceADay = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-11 > input')

    #Локатор поля "Разовая доза"
FD_singleDose = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-10 > input')

    #Локатор поля "Способ приема"
FD_receptionMethod = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-24 > input')

    #Выпадающий список "Способов приема"
LT_receptionMethod = (By.CSS_SELECTOR, '.cdk-overlay-connected-position-bounding-box')

    #Локатор крестика очистки поля "Способ приема"
BT_receptionMethod = (By.CSS_SELECTOR, '.mat-form-field-suffix.ng-tns-c11-24.ng-star-inserted > div > button')

    #Локатор поля "Лекарственная форма"
FD_dosageform = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-21 > input')

    #Локатор поля "Дозировка"
FD_dose = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-16 > input')

    #Локатор поля "Путь введения"
FD_way = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-25 > input')

    #Локатор обязательности поля "Путь введения" (подсвеченность красным)
OB_way = (By.CSS_SELECTOR, '.mat-form-field-ripple.ng-tns-c11-25')

    #Локатор выпадающего списка поля "Путь введения"
LT_Way = (By.CSS_SELECTOR, '.mat-autocomplete-panel.mat-primary.ng-star-inserted.mat-autocomplete-visible')

    #Локатор крестика очистки поля "Путь введения"
BT_clear_way = (By.CSS_SELECTOR, '.ng-tns-c11-25 > button')

    #Локатор поля "МНН"
FD_mnn = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-19 > input')

    #Локатор поля "Торговое"
FD_trn = (By.CSS_SELECTOR, '.mat-form-field-infix.ng-tns-c11-20 > input')

    #Локатор кнопки "След" в гриде для переключения на другую страницу со списком назначений
BT_next = (By.XPATH, '//*[@id="appointment"]/app-appointment/div/div[2]/div/div/app-st-table/div/div/div[2]/div[5]/button')

    #Локатор поля "Дата назначения"
FD_date_purpose = (By.XPATH, '//*[@id="mat-input-20"]')

    #Локатор кнопки календаря поля "Дата назначения"
BT_date_purpose = (By.XPATH, '//*[@id="appointmentAdding"]/appointment-add/div[1]/div/div/mat-card/form/div[1]/div[1]/date-time/div/div[1]/st-date/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button')

    #Локатор обязательности поля "Дата назначения"
OB_date_purpose = (By.CSS_SELECTOR, '.mat-form-field-ripple.ng-tns-c11-29')



#=====================================Локаторы блока/формы "Рецепты" в ТАП==============================================


    #Локатор кнопки "Добавить"
BT_add_recipe = (By.CSS_SELECTOR, '#appointmentRecipe > appointment-recipe > div.row.mb-0 > div > div > app-st-table > div > div:nth-child(5)')

    #Локатор формы рецепта
FM_recipe = (By.ID, 'appointmentRecipeForm')

    #Локатор статуса рецепта в гриде
ST_recipe_grid = (By.XPATH, '//*[@id="appointmentRecipe"]/appointment-recipe/div[2]/div/div/app-st-table/div/table/tbody/tr/td[7]')

    #Локатор поля "Льгота"
FD_privilege = (By.XPATH, '//*[@id="mat-input-26"]')

    #Локатор первого элемента выпадающего списка поля "Льгота"
LT = (By.CSS_SELECTOR, '.mat-option-text')

    #Локатор чек-бокса "На дом"
CH_home = (By.ID, 'mat-mdc-checkbox-5')

    #Локатор кнопки "Сохранить"
BT_save_recipe = (By.CSS_SELECTOR, '#appointmentRecipeForm > div > div > div > mat-card > form > div.flex-justify-space-between > div:nth-child(2) > button:nth-child(2)')

    #Локатор кнопки "Подписать и отправить"
BT_caption_recipe = (By.CSS_SELECTOR, '#appointmentRecipeForm > div > div > div > mat-card > form > div.flex-justify-space-between > div:nth-child(2) > button:nth-child(3)')

    #Локатор номера рецепта в гриде блока "Рецепты"
CL_num_recipe = (By.CSS_SELECTOR, '#appointmentRecipe > appointment-recipe > div.row.mb-0 > div > div > app-st-table > div > table > tbody > tr > td.mat-mdc-cell.mdc-data-table__cell.cdk-cell.cdk-column-numRecipe.mat-column-numRecipe.appointment__row.appointment__row--edit.ng-star-inserted')

    #Локатор Радиокнопки "Коммерческий"
CH_comm = (By.XPATH, '//*[@id="mat-radio-15-input"]')

    #Локатор радиокнопки "Льготный"
CH_privilege = (By.XPATH, '//*[@id="mat-radio-13-input"]')

    #Локатор Чек-бокса "Бланк"
CH_blank = (By.CSS_SELECTOR, '#appointmentRecipeForm > div > div > div > mat-card > form > div:nth-child(2) > div.col.s1.mat-input-wrapper')

    #Локатор Поля "Серия"
FD_series = (By.ID, 'mat-input-24')

    #Локатор Поля "Номер"
FD_number = (By.ID, 'mat-input-25')

    #Локатор поля ввода "Адрес доставки"
FD_adress = (By.XPATH, '//*[@id="mat-chip-list-1"]/div/input')

    #Локатор крестика очистки поля "Адрес доствки"
BT_clear_adress = (By.XPATH, '//*[@id="appointmentRecipeForm"]/div/div/div/mat-card/form/div[5]/div/st-address/div/div[1]/mat-form-field/div/div[1]/div[2]/span/button')

    #Локатор элементов внутри поля "Адрес доставки"
FD_adress_text = (By.CSS_SELECTOR, '.mat-chip-list-wrapper > mat-chip')

    #Локатор текста ошибки поля "Адрес доставки" когда не заполнено
WD_adress = (By.XPATH, '//*[@id="appointmentRecipeForm"]/div/div/div/mat-card/form/div[5]/div/mat-error')

    #Локатор поля "Телефон"
FD_phone = (By.XPATH, '//*[@id="appointmentRecipeForm"]/div/div/div/mat-card/form/div[4]/div[2]/mat-form-field/div/div[1]/div/input')

    #Локатор поля "Дата выписки"
FD_date = (By.XPATH, '//*[@id="appointmentRecipeForm"]/div/div/div/mat-card/form/div[6]/div[2]/date-time/div/div/st-date/mat-form-field/div/div[1]/div[1]/input')

    #Локатор кнопки календаря поля "Дата выписки"
BT_date = (By.CSS_SELECTOR, '.mat-form-field-suffix.ng-tns-c11-47.ng-star-inserted')

    #Локатор обязательности поля "Дата выписки"
OB_date = (By.CSS_SELECTOR, '.mat-form-field-ripple.ng-tns-c11-47')

    #Локатоп поля "Врач"
FD_doctor_recipe = (By.XPATH, '//*[@id="mat-input-33"]')

    #Локатор обязательности поля "Врач"
OB_doctor_recipe = (By.XPATH, '//*[@id="appointmentRecipeForm"]/div/div/div/mat-card/form/div[7]/div[1]/st-autocomplete/mat-form-field/div/div[2]/span')

    #Локатор крестика очистки поля "Врач"
BT_clear_doctor_recipe = (By.CSS_SELECTOR, '.mat-form-field-suffix.ng-tns-c11-45.ng-star-inserted > div > button')

    #Локатор поля "Источник финансирования"
FD_source_of_financing = (By.XPATH, '//*[@id="mat-input-27"]')

    #Локатор поля "Процент оплаты"
FD_percentage_of_payment = (By.XPATH, '//*[@id="mat-input-28"]')

    #Локатор поля "Тип формы"
FD_type_form = (By.XPATH, '//*[@id="mat-input-29"]')

    #Локатор поля "Срок действия"
FD_period_of_validity = (By.XPATH, '//*[@id="mat-input-30"]')

    #Локатор радиокнопки "Электронный"
CH_electronic_recipe = (By.XPATH, '//*[@id="mat-radio-18-input"]')

    #Локатор радиокнопки "Бумажный"
CH_paper_recipe = (By.XPATH, '//*[@id="mat-radio-17-input"]')

    #Локатор кнопки "Отменить" в гриде рецептов
BT_cancel_recipe = (By.XPATH, '//*[@id="appointmentRecipe"]/appointment-recipe/div[2]/div/div/app-st-table/div/table/tbody/tr/td[12]')

    #Локатор текста в гриде рецептов
CL_crid_recipe_text = (By.CSS_SELECTOR, '.no-data-to-display.substrate-block.divide-border-bottom.ng-star-inserted')