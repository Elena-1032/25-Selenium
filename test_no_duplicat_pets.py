# 5. В списке нет повторяющихся питомцев. (Сложное задание).

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_no_duplicate_pets(go_to_my_pets):
    # Явные ожидания__________________:
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    data_my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')# Сохраняем данные о питомцах
    # Неявные ожидания___________________:
    pytest.driver.implicitly_wait(10)

    list_data_my_pets = [] # Проверка_____________________:
    for i in range(len(data_my_pets)):
        list_data = data_my_pets[i].text.split("\n")
        list_data_my_pets.append(list_data[0])  # элемент с данными питомца в списке
    set_data_my_pets = set(list_data_my_pets)  # список в множество
    assert len(list_data_my_pets) == len(set_data_my_pets)  # сравнивнение

# Запускаем python -m pytest -v --driver Chrome --driver-path
# /python/24_new/chromedriver.exe python/24_new/test_no_duplicat_pets.py
