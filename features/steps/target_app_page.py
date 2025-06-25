from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.target_app_page.open_sign_in_page()


@given('Store original window')
def store_window(context):
    context.original_window = context.app.target_app_page.get_current_window_id()


@when('Click on Target terms and conditions link')
def click_on_terms_link(context):
    sleep(10)
    context.app.target_app_page.click_on_terms_link()


@when('Switch to the newly opened window')
def switch_tabs(context):
    context.app.target_app_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_terms_page(context):
    context.app.target_app_page.verify_terms_page()


@then('Close current page')
def close_page(context):
    context.app.target_app_page.close_window()


@then('Return to original window')
def switch_to_original_window(context):
    context.app.target_app_page.switch_to_window_by_id(context.original_window)
