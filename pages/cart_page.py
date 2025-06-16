from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

class Cart(Page):

    def validate_empty_cart_message(context):
        actual_text = context.driver.find_element(*EMPTY_CART_MESSAGE).text
        expected_text = "Your cart is empty"
        assert actual_text == expected_text