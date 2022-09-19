from selenium.webdriver.common.by import By


class YandexSearchLocators:
    INPUT_FIELD = (By.CSS_SELECTOR, "input.input__control")
    SUGGEST_ELEMENT = (By.CSS_SELECTOR, ".mini-suggest__popup")
    LIST_OF_RESULTS = (By.CSS_SELECTOR, "ul.serp-list")
    FIRST_LINK = (By.CSS_SELECTOR, "[data-cid='0'] a.Link")


class YandexImagesLocators:
    INPUT_FIELD = (By.CSS_SELECTOR, "input.input__control")
    LINK_TO_IMAGES = (By.CSS_SELECTOR, ".service_name_images .link")
    FIRST_CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList-Preview:nth-child(1)")
    FIRST_IMAGE = (By.CSS_SELECTOR, ".serp-item__link:nth-child(1)")
    CURRENT_IMAGE = (By.CSS_SELECTOR, ".MMImage-Origin")
    BUTTON_NEXT = (By.CSS_SELECTOR, ".CircleButton_type_next")
    BUTTON_PREV = (By.CSS_SELECTOR, ".CircleButton_type_prev")
