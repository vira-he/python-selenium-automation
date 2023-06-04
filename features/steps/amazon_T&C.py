from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


PRIVACY_LINK = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")
HEADER_TEXT = (By.ID, "GUID-8966E75F-9B92-4A2B-BFD5-967D57513A40__GUID-2C1DF364-8FA3-4387-BCDB-2A63B7C51B64")


@given("Open Amazon T&C page")
def open_tc_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when("Store original windows")
def store_original_window(context):
    context.original_window = context.driver.current_window_handle


@when("Click on Amazon Privacy Notice link")
def click_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_LINK).click()


@when("Switch to the newly opened window")
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])


@then("Verify Amazon Privacy Notice page is opened")
def verify_privacy_notice_opened(context):
    actual_result = context.driver.find_element(*HEADER_TEXT).text
    expected_result = "Amazon.com Privacy Notice"
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'


@then ("User can close new window and switch back to original")
def return_to_original_window(context):
    context.driver.switch_to.window(context.original_window)