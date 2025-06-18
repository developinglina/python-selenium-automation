from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@then('Verify correct search result display for {product_name}')
def verify_search_result(context, product_name):
    context.app.search_results_page.verify_search_results()


@when('the user clicks add to cart')
def add_to_cart(context):
    context.app.search_results_page.add_to_cart()
