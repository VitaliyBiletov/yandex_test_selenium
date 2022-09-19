from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import YandexSearchLocators


class YandexSearchPage(BasePage):
    url = "https://yandex.ru/search/"

    def __init__(self, browser):
        super().__init__(browser, self.url)

    def should_be_input_field(self):
        assert self.is_element_present(*YandexSearchLocators.INPUT_FIELD)

    def entering_text_in_the_input_field(self):
        search_input = self.browser.find_element(*YandexSearchLocators.INPUT_FIELD)
        search_input.send_keys("Тензор")

    def should_be_suggest(self):
        assert self.is_element_present(*YandexSearchLocators.SUGGEST_ELEMENT), "Suggest is not present"

    def click_to_enter(self):
        search_input = self.browser.find_element(*YandexSearchLocators.INPUT_FIELD)
        search_input.send_keys(Keys.ENTER)

    def should_be_results(self):
        assert self.is_element_present(*YandexSearchLocators.LIST_OF_RESULTS), \
            "Отстутсвует таблица с результатами поиска"

    def the_first_link_directs_to_tensor_ru(self):
        first_link = WebDriverWait(self.browser, 1).until(
            EC.presence_of_element_located(YandexSearchLocators.FIRST_LINK)
        )
        first_link.click()
