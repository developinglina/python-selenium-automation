from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify correct search result display for {product_name}')
def verify_search_result(context, product_name):
    element = context.driver.find_element(By.CSS_SELECTOR, "span.h-text-bs.h-display-flex.h-flex-align-center.h-text-grayDark.h-margin-l-x2")
    actual_text = element.text
    assert product_name in actual_text
