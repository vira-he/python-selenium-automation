from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


SEARCH_FIELD = By.ID, "twotabsearchtextbox"
SUBMIT_BTN = By.ID, "nav-search-submit-button"
ORDERS_BTN = By.ID, "nav-orders"
CART_BTN = By.ID, "nav-cart"
BS_BTN = By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]"
FOOTER_LINKS = By.CSS_SELECTOR, ".navFooterMoreOnAmazon a"
POPUP_SIGNIN_BTN = By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button"


@given("Open amazon main page")
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when("Search for {search_word}")
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SUBMIT_BTN).click()


@when("Click Orders")
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()

@when("Open cart")
def open_cart(context):
    context.driver.find_element(*CART_BTN).click()


@when("Click Best Sellers")
def click_best_sellers(context):
    context.driver.find_element(*BS_BTN).click()


@when("Click on button from Signin popup")
def click_signin_popup_btn(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Signin not clickable'
    ).click()


@when("Verify sign in is clickable")
def verify_sign_in_clickable(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Signin not clickable'
    )


@when("Wait for {sec} sec")
def wait_sec(context, sec):
    sleep(int(sec))


@then("Verify there are 36 links")
def verify_link_number(context):
    links_count = len(context.driver.find_elements(*FOOTER_LINKS))
    assert links_count == 36, f'Expected 36 links, but got {links_count}'


@then("Verify sign in disappears")
def verify_sign_in_popup_disappears(context):
    context.driver.wait.until(
        EC.invisibility_of_element_located(POPUP_SIGNIN_BTN),
        message="Signin btn did not disappear"
    )


