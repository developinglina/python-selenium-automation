from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Target homepage is opened')
def open_google(context):
    context.driver.get('https://www.target.com/')
    sleep(10)

