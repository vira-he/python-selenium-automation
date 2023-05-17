from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SIGNIN_HEADER = By.XPATH, "//h1[@class = 'a-spacing-small']"


@then("Verify Sign in page opened")
def verify_signin_page(context):
    expected_result = "Sign in"
    actual_result = context.driver.find_element(*SIGNIN_HEADER).text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'
