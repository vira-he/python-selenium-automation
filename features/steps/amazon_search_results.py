from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_RESULT_TEXT = By.XPATH, "//span[@class='a-color-state a-text-bold']"
OPEN_SEARCH_RESULT = By.XPATH, "//div[@data-asin = 'B08Y85SYG4']"
ADD_TO_CART_BTN = By.ID, "add-to-cart-button"


@then("Verify search results for {expected_result}")
def verify_search_results(context, expected_result):
    # expected_result = '"table"'
    # actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    # assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'
    context.app.search_results.verify_search_results(expected_result)


@when("Add product to cart")
def add_to_cart(context):
    context.driver.find_element(*OPEN_SEARCH_RESULT).click()
    sleep(5)
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(5)
    # cart opens automatically after product added


@then("Verify correct department shown")
def verify_dept(context):
    context.app.search_results.verify_dept()
