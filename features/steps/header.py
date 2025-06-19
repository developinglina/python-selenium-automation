from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.XPATH, '//*[@data-test="@web/CartLink"]')

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@aria-label='search']")



@when('the user clicks on the cart icon at the top of the page')
def click_on_cart_icon(context):
    context.app.header.click_on_cart_icon()


@when('the user clicks the "Sign in" button')
def click_sign_in(context):
    context.app.header.click_sign_in()


@when('the user searches for {product_name}')
def search_product(context, product_name):
    context.app.header.search_product(product_name)

