from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

USERNAME_FIELD = (By.ID, "username")


@then('Sign In form is opened')
def verify_sign_in_form(context):
    input_field = context.driver.find_element(*USERNAME_FIELD)
    assert input_field.is_displayed()
    print("sign in form is displayed")
