from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep





@when('"sign in" from the right-side navigation menu is clicked')
def click_sign_in_side_nav(context):
    context.app.header.click_sign_in_side_nav()