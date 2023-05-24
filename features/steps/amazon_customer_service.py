from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

HDR_TEXT = By.CSS_SELECTOR, ".header-subtext.subtext-container"
PAGE_CONTAINER = By.CSS_SELECTOR, ".issue-card-container"
SEARCH_FIELD = By.ID, "hubHelpSearchInput"
HELP_TOPICS = By.CSS_SELECTOR, ".help-topics-list-wrapper"


@given("Open Customer service page")
def open_cs_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html?nodeId=508510&ref_=nav_cs_customerservice')


@then("Search for Header text")
def search_header(context):
    assert context.driver.find_element(*HDR_TEXT).is_displayed(), "Header text is not shown"


@then("Search for Options menu")
def search_options(context):
    assert context.driver.find_element(*PAGE_CONTAINER).is_displayed(), "Options menu is not shown"


@then("Search for Search field")
def search_field(context):
    assert context.driver.find_element(*SEARCH_FIELD).is_displayed(), "Search field is not shown"


@then("Search for All help topics")
def search_help(context):
    assert context.driver.find_element(*HELP_TOPICS).is_displayed(), "All help topics block is not shown"
