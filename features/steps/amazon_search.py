from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open amazon main page")
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when ("Search for table")
def search_amazon (context):
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("table")
    context.driver.find_element(By.ID, "nav-search-submit-button").click()


@then("Verify search results")
def verify_search_results (context):
    expected_result = '"table"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'


