from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


SIGNIN_HEADER = By.XPATH, "//h1[@class = 'a-spacing-small']"


@then("Verify Sign in page opened")
def verify_signin_opens(context):
    context.app.signin_page.verify_signin_opens()
    # # Verify URL
    # context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
    # # Verify header
    # expected_result = "Sign in"
    # actual_result = context.driver.find_element(*SIGNIN_HEADER).text
    # assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'
