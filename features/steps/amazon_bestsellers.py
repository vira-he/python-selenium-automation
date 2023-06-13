from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


ELEMENTS_LI = By.CSS_SELECTOR, "._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a"
TOP_LINKS = By.CSS_SELECTOR, "."


@then("Verify links displayed")
def verify_links_displayed(context):
    links_count = len(context.driver.find_elements(*ELEMENTS_LI))
    assert links_count == 5, f'Expected 5 links, but got {links_count}'


# create loop to verify user clicks thorugh links and verifies they are correct pagaes
@then("User can click through top links and verify correct link opens")
def click_through_top_links(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for i in range(len(top_links)):
        link_to_click = context.driver.find_elements(*TOP_LINKS)[i]
        link_text = link_to_click.text
        link_to_click.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text == header_text, f"Expected {link_text}, actual {header_text}"


