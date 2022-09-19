from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def go_to_url(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        url = WebDriverWait(self.browser, 1).until(
            EC.presence_of_element_located((how, what))
        )
        return bool(url)

    def checking_the_transition_to_the_page(self, target_url):
        window_after = self.browser.window_handles[1]
        self.browser.switch_to.window(window_after)
        url = WebDriverWait(self.browser, 5).until(
            EC.url_contains(target_url)
        )
        assert url, f"Не выполнен переход по адресу: {target_url}"
