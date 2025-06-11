from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify correct search result display for {product_name}')
def verify_search_result(context, product_name):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']")
    assert product_name in actual_text, f"Error, expected {product_name} not in {actual_text}"
