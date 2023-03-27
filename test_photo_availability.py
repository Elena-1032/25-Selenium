# 2/ Хотя бы у половины питомцев есть фото/

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_photo_availability(go_to_my_pets):
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")# 1* Сохраняем элементы статистики
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')# Сохраняем элементы img
   number = statistic[0].text.split('\n')# количество питомцев из данных статистики 1*
   number = number[1].split(' ')
   number = int(number[1])
   half = number // 2 # Половина количества питомцев
   # Неявные ожидания ________________________________:
   pytest.driver.implicitly_wait(10)
   number_а_photos = 0 # Проверка, питомцы с фото
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         number_а_photos += 1 #счетчик питомцев с фото
   assert number_а_photos >= half # Провверка на половину питомцев с фото
   print(f'количество фото: {number_а_photos}, что более половины {half} от числа питомцев ')


# Запускаем python -m pytest -v --driver Chrome --driver-path
# /python/chromedriver.exe python/test_photo_availability.py