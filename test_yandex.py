from pages.yandex_search_page import YandexSearchPage
from pages.yandex_images_page import YandexImagesPage


class TestYandex:
    def test_of_the_transition_to_the_tensor_page(self, browser):
        page = YandexSearchPage(browser)
        page.go_to_url()
        page.should_be_input_field()
        page.entering_text_in_the_input_field()
        page.should_be_suggest()
        page.click_to_enter()
        page.should_be_results()
        page.the_first_link_directs_to_tensor_ru()
        page.checking_the_transition_to_the_page("tensor.ru")

    def test_images(self, browser):
        page = YandexSearchPage(browser)
        page.go_to_url()
        page_images = YandexImagesPage(browser, browser.current_url)
        page_images.should_be_image_link()
        page_images.click_to_images_link()
        page_images.checking_the_transition_to_the_page("https://yandex.ru/images/")
        page_images.open_first_category_images()
        page_images.should_be_category_in_input_value()
        page_images.open_first_image()
        page_images.is_opened_image()
        page_images.click_to_next_image()
        page_images.is_the_picture_changed()
        page_images.click_to_prev_image()
        page_images.is_the_previous_picture()
