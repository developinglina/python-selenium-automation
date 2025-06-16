from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Target homepage is opened')
def open_target(context):
    context.app.main_page.open_main_page()
