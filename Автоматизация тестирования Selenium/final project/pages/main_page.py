import time
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_browse_store(self):
        assert self.is_element_present(*MainPageLocators.BROWSE_STORE), "Browse store link is not presented"

    def all_products(self):
        assert self.is_element_present(*MainPageLocators.ALL_BOOKS), "All books list is not presented"
        text = self.browser.find_element(*MainPageLocators.ALL_BOOKS).get_attribute("innerHTML")
        all_prod = self.browser.find_element(*MainPageLocators.ALL_BOOKS)
        all_prod.click()
        page_title = self.browser.find_element(*MainPageLocators.HEADER_ALLBOOKS)
        title = page_title.get_attribute("innerHTML")
        time.sleep(5)
        assert text in title, "ALL PRODUCTS title is not presented"