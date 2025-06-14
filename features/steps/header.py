from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.XPATH, '//*[@data-test="@web/CartLink"]')
SIGN_IN_BTN = (By.ID, 'account-sign-in')
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@aria-label='search']")


@when('the user clicks on the cart icon at the top of the page')
def click_on_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(15)


@when('the user clicks the "Sign in" button')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN_BTN).click()
    sleep(10)


@when('the user searches for {product_name}')
def search_product(context, product_name):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product_name)
    sleep(10)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(5)
