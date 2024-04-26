import pyautogui
import pytest
from autotest.tests.config.function import *
from autotest.tests.config.pathConfTest import *

#Установка в браузере расширения криптопро которая будет действовать в рамках всей сессии (Пока не выполнится последний тест)
@pytest.fixture(scope='session')
def criptoPro():

    browser.get(url_croptoPro)
    browser.implicitly_wait(20)
    f = ContractsPage(browser)
    f.click_element(BT_add_criptoPlugin)
    time.sleep(4)
    pyautogui.press('LEFT')
    time.sleep(1)
    pyautogui.press('ENTER')
    time.sleep(2)


