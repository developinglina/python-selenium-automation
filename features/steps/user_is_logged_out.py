from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGN_IN_BTN = (By.ID, 'account-sign-in')
SIDE_NAV_SIGN_IN_BTN = (By.XPATH, '//*[@data-test="accountNav-signIn"]')
SIGN_IN_HEADER = (By.XPATH, '//h1[contains(text(), "Sign in or create account")]')


@given('a user opens Target homepage')
def open_google(context):
    context.driver.get('https://www.target.com/')
    sleep(10)


@when('the user clicks the "Sign in" button')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN_BTN).click()
    sleep(10)


@when('"sign in" from the right-side navigation menu is clicked')
def click_sign_in_side_nav(context):
    context.driver.find_element(*SIDE_NAV_SIGN_IN_BTN).click()
    sleep(10)
@then('Sign In form is opened')
def verify_sign_in_form(context):
    element_text = context.driver.find_element(By.XPATH, '//h1[contains(text(), "Sign in or create account")]').text
    sleep(5)
    assert element_text.text == "Sign in or create account"


print("test case passed!")
