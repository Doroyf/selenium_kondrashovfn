from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class BasePage(object):
    """Класс для базовой страницы"""
    def __init__(self):
        # переходим на страницу
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/")

class FunctionsForWork(BasePage):
    """Класс для работы с элементами страницы"""
    def element_click(self, element_xpath):
        element = WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(By.XPATH, element_xpath)).click()

    def element_text(self, element_xpath, element_name):
        try:
            element = WebDriverWait(self.driver, 10).until(
                lambda driver: self.driver.find_element(By.XPATH, element_xpath))
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, element_xpath))).text
            assert element == element_name, f'ERROR Проверка элемента ! {element_name} ! не пройдена, выдан следующий результат: {element}'
        except NoSuchElementException:
            return False
        return True

    def check_element_find(self, element_xpath, element):
        try:
            element = WebDriverWait(self.driver, 10).until(
                lambda driver: self.driver.find_element(By.XPATH, element_xpath))
        except NoSuchElementException:
            print(f'ERROR Элемент !{element}! не найден')
            return False
        return True

    def element_text_special(self, element_xpath1, element_xpath2, element_name):
        try:
            element1 = WebDriverWait(self.driver, 10).until(
                lambda driver: self.driver.find_element(By.XPATH, element_xpath1))
            element1 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, element_xpath1))).text
            element2 = WebDriverWait(self.driver, 10).until(
                lambda driver: self.driver.find_element(By.XPATH, element_xpath2))
            element2 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, element_xpath2))).text
            element_name1 = element1 + element2
            assert element_name1 == element_name, f'ERROR Проверка элемента ! {element_name} ! не пройдена, выдан следующий результат: {element_name1}'
        except NoSuchElementException:
            return False
        return True

    def close_driver(self):
        self.driver.close()