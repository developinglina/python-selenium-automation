from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SearchResultsPage(Page):
    VIEW_CART_BTN = (By.CSS_SELECTOR, 'a[href="/cart"]')
    SIDE_NAV_ADD_TO_CART = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
    ADD_CART_BTN = (By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]')
    SEARCH_RESULTS_TXT = (By.CSS_SELECTOR,
                          "span.h-text-bs.h-display-flex.h-flex-align-center.h-text-grayDark.h-margin-l-x2")

    def verify_search_results(self):
        actual_text = self.find_element(*self.SEARCH_RESULTS_TXT).text
        assert 'tea' in actual_text, f"Error, expected 'tea' not in actual {actual_text}"

    def add_to_cart(self):
        self.click(*self.ADD_CART_BTN)
        sleep(10)
        self.click(*self.SIDE_NAV_ADD_TO_CART)
        # Wait for cart page to be ready, then click "View Cart"
        sleep(10)
        self.click(*self.VIEW_CART_BTN)
