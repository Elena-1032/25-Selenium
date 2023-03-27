#___1. Присутствуют все питомцы на странице
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_are_present(go_to_my_pets):
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")# 1*Сохраняем в переменную statistic элементы статистики

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')# 2*Сохраняем элементы карточек питомцев


   number = statistic[0].text.split('\n') # количество питомцев из данных статистики 1*
   number = number[1].split(' ')
   number = int(number[1])
   number_of_pets = len(pets)# Получаем количество карточек питомцев 2*
   pytest.driver.implicitly_wait(10)# неявные ожидания:
   assert number == number_of_pets # количество питомцев из статистики 1* совпадает с количеством карточек питомцев 2*

# Запускаем: python -m pytest -v --driver Chrome --driver-path
# /Python/chromedriver.exe test_all_pets_are_present.py