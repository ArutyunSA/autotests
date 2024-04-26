#=================Здесь указаны цвета отображения шагов и результатов теста в консоли=============================
import time
import pytest
import testit
from colorama import init, Fore, Back, Style
# Инициализация colorama
init()

def case_name(message):
    print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")

def step(message):
    print(f"{Style.BRIGHT}{message}{Style.RESET_ALL}")

def true_step(message):
    print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
    pass
def false_step(message):
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")





