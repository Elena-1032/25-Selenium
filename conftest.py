import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('.\tests\chromedriver.exe')
   pytest.driver.get('http://petfriends.skillfactory.ru/login') # Страница авторизации
   yield
   pytest.driver.quit()

@pytest.fixture()
def go_to_my_pets():
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email"))) # ввести email
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass"))) # Ввести пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click() # кнопка ВОЙТИ
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='button']")))
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="button"]').click() # Кнопка МЕНЮ
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы"))) # Меню "Мои питомцы"
   pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы").click()