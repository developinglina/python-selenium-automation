from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_ITEMS = (By.CSS_SELECTOR, 'span.sc-46253dd2-2.ijhCkR')


@then('the user should see a message that says "Your cart is empty"')
def validate_empty_cart_message(context):
    context.app.cart_page.validate_empty_cart_message()


@then('verify cart')
def verify_cart(context):
    # Find all elements matching the selector
    cart_items_elements = context.driver.find_elements(*CART_ITEMS)

    # Check if list is not empty (element found)
    if len(cart_items_elements) > 0:
        # Get the first element's text and print it
        print("Cart items found: ", cart_items_elements[0].text)
    else:
        print("Cart items not found.")
