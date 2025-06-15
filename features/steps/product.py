from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

@given('Open target product A-93533635 page')
def open_target(context):
    context.driver.get(
        "https://www.target.com/p/women-s-high-rise-utility-barrel-jeans-universal-thread/-/A-93533635?preselect=93390852#lnk=sametab"
    )
    sleep(8)

@then('Verify user can click through color options')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Olive Green', 'Medium Wash', 'Pink']
    actual_colors = []


    product_images = context.driver.find_elements(
        By.CSS_SELECTOR,
        'div.styles_img__h4ySy'
    )

    print("Found images:", len(product_images))

    for p in product_images:
        p.click()
        sleep(2)

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    # Remove duplicates from actual_colors before asserting
    unique_actual_colors = []
    for color in actual_colors:
        if color not in unique_actual_colors:
            unique_actual_colors.append(color)

    print("Final unique colors selected:", unique_actual_colors)

    assert expected_colors == unique_actual_colors, f'Expected {expected_colors} did not match actual {unique_actual_colors}'

    print('test case passed')
