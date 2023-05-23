from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


ELEMENTS_LI = By.CSS_SELECTOR, "._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a"

@then("Verify links displayed")
def verify_links_displayed(context):
    links_count = len(context.driver.find_elements(*ELEMENTS_LI))
    assert links_count == 5, f'Expected 5 links, but got {links_count}'