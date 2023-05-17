from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CONFIRMATION_TEXT = By.XPATH, "//span[@class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']"
CART_TEXT = By.XPATH, "//h1[@class='a-spacing-mini a-spacing-top-base']"


@then("Verify the product is added to cart")
def verify_search_results(context):
    expected_result = 'Added to Cart'
    actual_result = context.driver.find_element(*CONFIRMATION_TEXT).text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'


@then("Verify cart is empty")
def verify_cart_empty(context):
    expected_result = "Your Amazon Cart is empty."
    actual_result = context.driver.find_element(*CART_TEXT).text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'

