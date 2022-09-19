from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from .locators import YandexImagesLocators


class YandexImagesPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.first_image_url = None
        self.current_image_url = None
        self.category_name = None

    def should_be_image_link(self):
        assert self.is_element_present(*YandexImagesLocators.LINK_TO_IMAGES), \
            "Сслыка на страницу картинки отсутстует"

    def click_to_images_link(self):
        images_link = WebDriverWait(self.browser, 1).until(
            EC.presence_of_element_located(YandexImagesLocators.LINK_TO_IMAGES)
        )
        images_link.click()

    def open_first_category_images(self):
        first_category = self.browser.find_element(*YandexImagesLocators.FIRST_CATEGORY)
        self.category_name = self.browser.find_element(*YandexImagesLocators.FIRST_CATEGORY).text
        first_category.click()

    def should_be_category_in_input_value(self):
        input_search = self.browser.find_element(*YandexImagesLocators.INPUT_FIELD)
        assert input_search.get_attribute("value") == self.category_name, "Неверное название категории"

    def open_first_image(self):
        first_image = WebDriverWait(self.browser, 3).until(
            EC.presence_of_element_located(YandexImagesLocators.FIRST_IMAGE)
        )
        first_image.click()

    def is_opened_image(self):
        image = WebDriverWait(self.browser, 3).until(
            EC.presence_of_element_located(YandexImagesLocators.CURRENT_IMAGE)
        )
        self.first_image_url = image.get_attribute("src")
        assert self.is_element_present(*YandexImagesLocators.CURRENT_IMAGE), "Ошибка при открытии картинки"

    def click_to_next_image(self):
        button_next = self.browser.find_element(*YandexImagesLocators.BUTTON_NEXT)
        button_next.click()
        image = self.browser.find_element(*YandexImagesLocators.CURRENT_IMAGE)
        self.current_image_url = image.get_attribute("src")

    def is_the_picture_changed(self):
        assert self.first_image_url != self.current_image_url, "Картинка не сменилась"

    def click_to_prev_image(self):
        button_prev = self.browser.find_element(*YandexImagesLocators.BUTTON_PREV)
        button_prev.click()

    def is_the_previous_picture(self):
        image = WebDriverWait(self.browser, 3).until(
            EC.presence_of_element_located(YandexImagesLocators.CURRENT_IMAGE)
        )
        self.current_image_url = image.get_attribute("src")
        assert self.first_image_url == self.current_image_url, "Первая картинка не совпадает с исходной"
