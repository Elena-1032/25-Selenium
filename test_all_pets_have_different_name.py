#4. МОИ ПИТОМЦЫ  имеют разные имена

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_have_different_names(go_to_my_pets):
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    name_my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr') # элементы с данными именами о питомцах
    pytest.driver.implicitly_wait(10) # неявные ожидания:

    list_name_my_pets = []     # Проверка:
    for i in range(len(name_my_pets)):
        list_name_my_pets.append(name_my_pets[i].text)
    set_pet_data = set(list_name_my_pets)  # преобразовываем список в множество
    assert len(list_name_my_pets) == len(set_pet_data)  # сравниваем , если нет повтора то равны


# Запускаем python -m pytest -v --driver Chrome --driver-path
# /python/24_new/chromedriver.exe python/24_new/test_all_pets_have_different_name.py
