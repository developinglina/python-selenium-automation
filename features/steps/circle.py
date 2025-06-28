from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

TARGET_CIRCLE_URL = 'https://www.target.com/circle'
BENEFIT_CELLS = (By.CLASS_NAME, 'storycard--text')


@given('Target circle is open')
def open_google(context):
    context.driver.get(TARGET_CIRCLE_URL)
    context.wait.until(EC.presence_of_element_located(BENEFIT_CELLS))


@then("verify number of benefit cells")
def verify_num_of_cells(context):
    elements = context.driver.find_elements(*BENEFIT_CELLS )
    context.wait.until(EC.presence_of_all_elements_located(BENEFIT_CELLS))

    actual = len(elements)
    print("Number of elements found:", actual)
    assert actual >= 10, f"Expected at least 10 benefit cells, but found {actual}"

