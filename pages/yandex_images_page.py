import time
from loguru import logger
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from .locators import YandexImagesLocators


class YandexImagesPage(BasePage):
    """Класс описывает методы работы со страницей картинок (yandex.ry/images)"""
    def __init__(self, browser, url):
        """
        Конструктор класса
        first_image_url - атрибут для хранения url первой картинки
        current_image_url - атрибут для хранения url текущей открытой картинки
        category_name - атрибут для хранения названия категории
        """
        super().__init__(browser, url)
        self.first_image_url = None
        self.current_image_url = None
        self.category_name = None

    def should_be_image_link(self):
        """Проверяет наличие ссылки на страницу с картинками"""
        assert self.is_element_present(*YandexImagesLocators.LINK_TO_IMAGES), \
            logger.error("Сслыка 'картинки' отсутстует")

    def click_to_images_link(self):
        """Получает элемент ссылки и кликает по нему"""
        images_link = WebDriverWait(self.browser, 1).until(
            EC.presence_of_element_located(YandexImagesLocators.LINK_TO_IMAGES)
        )
        images_link.click()

    def open_first_category_images(self):
        """
        Получает первый элемент среди категорий картинок
        Получает имя категории и заисывает его в атрибут category_name
        Кликает по первой категории
        """
        first_category = self.browser.find_element(*YandexImagesLocators.FIRST_CATEGORY)
        self.category_name = self.browser.find_element(*YandexImagesLocators.FIRST_CATEGORY).text
        first_category.click()

    def should_be_category_in_input_value(self):
        """
        Проверяет наличие названия категории в поисковой строке
        Проверяет что именно та категоря которую мы выбрали отображается в поисковой строке
        """
        input_search = self.browser.find_element(*YandexImagesLocators.INPUT_FIELD)
        assert input_search.get_attribute("value") == self.category_name, \
            logger.error("Неверное название категории")

    def open_first_image(self):
        """Получает первую картинку и кликает по ней"""
        try:
            first_image = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located(YandexImagesLocators.FIRST_IMAGE)
            )
            first_image.click()
        except TimeoutException:
            logger.error("Первая картинка отсутствует")

    def is_opened_image(self):
        """
        Проверяет открытие картинки
        Запоминает url прервой картинки в атрибуте first_image_url
        """
        time.sleep(1)
        image = WebDriverWait(self.browser, 3).until(
            EC.presence_of_element_located(YandexImagesLocators.CURRENT_IMAGE)
        )
        self.first_image_url = image.get_attribute("src")
        assert self.is_element_present(*YandexImagesLocators.CURRENT_IMAGE), \
            logger.error("Ошибка при открытии картинки")

    def click_to_next_image(self):
        """
        Получает элемент для переход к следующей картинке
        Кликает по нему
        Запоминает url картинки в атрибуте current_image_url
        """
        button_next = self.browser.find_element(*YandexImagesLocators.BUTTON_NEXT)
        button_next.click()
        image = self.browser.find_element(*YandexImagesLocators.CURRENT_IMAGE)
        self.current_image_url = image.get_attribute("src")

    def is_the_picture_changed(self):
        """Проверяет что картинка сменилась"""
        assert self.first_image_url != self.current_image_url, \
            logger.error("Картинка не сменилась")

    def click_to_prev_image(self):
        """
        Получает элемент для переход к предыдущей картинке
        Кликает по нему
        """
        button_prev = self.browser.find_element(*YandexImagesLocators.BUTTON_PREV)
        button_prev.click()

    def is_the_previous_picture(self):
        """
        Проверяет открытие картинки
        Запоминает url картинки в атрибуте current_image_url
        Сравнивает url полученный при клике на первую картинку и url полученный при возврате на первую кратинку
        """
        image = WebDriverWait(self.browser, 3).until(
            EC.presence_of_element_located(YandexImagesLocators.CURRENT_IMAGE)
        )
        self.current_image_url = image.get_attribute("src")

        assert self.first_image_url == self.current_image_url, \
            logger.error("Первая картинка не совпадает с исходной")
