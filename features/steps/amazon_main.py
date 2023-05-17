from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_FIELD = By.ID, "twotabsearchtextbox"
SUBMIT_BTN = By.ID, "nav-search-submit-button"
ORDERS_BTN = By.ID, 'nav-orders'
CART_BTN = By.ID, 'nav-cart'


@given("Open amazon main page")
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(15)


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