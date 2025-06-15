from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# Locate the button using data-test attribute
ADD_CART_BTN = (By.ID, 'addToCartButtonOrTextIdFor13010225')


@then('Verify correct search result display for {product_name}')
def verify_search_result(context, product_name):
    element = context.driver.find_element(By.CSS_SELECTOR,
                                          "span.h-text-bs.h-display-flex.h-flex-align-center.h-text-grayDark.h-margin-l-x2")
    actual_text = element.text
    assert product_name in actual_text


@when('the user clicks add to cart')
def add_to_cart(context):


    add_to_cart_button = context.driver.find_element(By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]')
    sleep(15)
    add_to_cart_button.click()

    # Wait for side nav to open, then click the "Order Pickup" button
    sleep(15)
    side_nav_add_to_cart_button = context.driver.find_element(By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
    sleep(5)
    side_nav_add_to_cart_button.click()

    # Wait for cart page to be ready, then click "View Cart"
    sleep(15)
    view_cart_button = context.driver.find_element(By.CSS_SELECTOR, 'a[href="/cart"]')
    sleep(5)
    view_cart_button.click()