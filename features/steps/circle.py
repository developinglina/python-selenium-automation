from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Target circle is open')
def open_google(context):
    context.driver.get('https://www.target.com/circle')
    sleep(10)


@then("verify number of benefit cells")
def verify_num_of_cells(context):
    elements = context.driver.find_elements(By.CLASS_NAME, 'storycard--text')
    sleep(12)

    # Print how many elements were found
    print("Number elements found:", len(elements))

