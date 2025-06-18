from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):

    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@aria-label='search']")
    CART_ICON = (By.XPATH, '//*[@data-test="@web/CartLink"]')

    def search_product(self, product_name):
        self.input_text(product_name, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_on_cart_icon(self):
        self.driver.find_element(*self.CART_ICON).click()
        sleep(5)

