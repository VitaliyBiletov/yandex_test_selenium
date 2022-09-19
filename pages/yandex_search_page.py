from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import YandexSearchLocators


class YandexSearchPage(BasePage):
    """Класс описывает методы работы со поисковой страницей (yandex.ry/search)"""

    url = "https://yandex.ru/search/"

    def __init__(self, browser):
        """Конструктор класса"""
        super().__init__(browser, self.url)

    def should_be_input_field(self):
        """Проверяет наличие поля поиска"""
        assert self.is_element_present(*YandexSearchLocators.INPUT_FIELD)

    def entering_text_in_the_input_field(self):
        """Получает элемент поля поиска и вводит туда текст"""
        search_input = self.browser.find_element(*YandexSearchLocators.INPUT_FIELD)
        search_input.send_keys("Тензор")

    def should_be_suggest(self):
        """Проверяет наличие таблицы с подсказками"""
        assert self.is_element_present(*YandexSearchLocators.SUGGEST_ELEMENT), "Таблица с подсказками отсутствует"

    def click_to_enter(self):
        """
        Получает элемент поля поиска
        Нажимает Enter
        """
        search_input = self.browser.find_element(*YandexSearchLocators.INPUT_FIELD)
        search_input.send_keys(Keys.ENTER)

    def should_be_results(self):
        """Проверяет наличие результатов поиска"""
        assert self.is_element_present(*YandexSearchLocators.LIST_OF_RESULTS), \
            "Отстутсвует таблица с результатами поиска"

    def the_first_link_directs_to_tensor_ru(self):
        """Проверяет наличие первой ссылки и кликает по ней"""
        first_link = WebDriverWait(self.browser, 1).until(
            EC.presence_of_element_located(YandexSearchLocators.FIRST_LINK)
        )
        first_link.click()
