from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



CART_ICON = (By.XPATH, '//*[@data-test="@web/CartLink"]')
EMPTY_CART_MESSAGE = (By.XPATH, '//h1[text()="Your cart is empty"]')

@given('Target homepage is opened')
def open_google(context):
    context.driver.get('https://www.target.com/')
    sleep(10)
@when('the user clicks on the cart icon at the top of the page')
def click_on_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(10)

@then('the user should see a message that says "Your cart is empty"')
def validate_empty_cart_message(context):
    element_text = context.driver.find_element(By.XPATH, '//h1[text()="Your cart is empty"]').text
    sleep(5)
    assert element_text.text == "Your cart is empty"

print('test case passed')

