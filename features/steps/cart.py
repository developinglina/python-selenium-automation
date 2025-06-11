from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

EMPTY_CART_MESSAGE = (By.XPATH, '//h1[text()="Your cart is empty"]')


@then('the user should see a message that says "Your cart is empty"')
def validate_empty_cart_message(context):
    element_text = context.driver.find_element(By.XPATH, '//h1[text()="Your cart is empty"]').text
    sleep(5)
    assert element_text.text == "Your cart is empty"


print('test case passed')
