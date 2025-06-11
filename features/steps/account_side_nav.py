from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SIDE_NAV_SIGN_IN_BTN = (By.XPATH, '//*[@data-test="accountNav-signIn"]')


@when('"sign in" from the right-side navigation menu is clicked')
def click_sign_in_side_nav(context):
    context.driver.find_element(*SIDE_NAV_SIGN_IN_BTN).click()
    sleep(10)