from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Sign In form is opened')
def verify_sign_in_form(context):
    context.app.sign_in_page.verify_sign_in_form()
