from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


COLOR_OPTIONS = By.CSS_SELECTOR, ".imgSwatch"


@given("Open amazon product {product} page")
def open_amazon_product(context, product):
    context.driver.get('https://www.amazon.com/gp/product/' + product)


@then("Verify user can click through colors")
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Blue, Over Dye', 'Bright White']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors [:3]:
        color.click()
        current_color = context.driver.find_element(By.CSS_SELECTOR,".selection").text
        actual_colors += [current_color]

    assert expected_colors == actual_colors, \
        f'Expected colors {expected_colors} did not match {actual_colors}'