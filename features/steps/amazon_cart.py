from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CONFIRMATION_TEXT = By.XPATH, "//span[@class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']"
CART_TEXT = By.XPATH, "//h1[@class='a-spacing-mini a-spacing-top-base']"


@then("Verify the product is added to cart")
def verify_search_results(context):
    context.app.cart_page.verify_search_results()


@then("Verify cart is empty")
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()
