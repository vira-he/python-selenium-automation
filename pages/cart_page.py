from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    CART_TEXT = By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty"
    CONFIRMATION_TEXT = By.XPATH, "//span[@class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']"

    def verify_search_results(self):
        actual_result = self.driver.find_element(*self.CONFIRMATION_TEXT).text
        assert actual_result == 'Added to Cart', \
            f'Error! Expected "Added to Cart" but got actual {actual_result}'

    def verify_cart_empty(self):
        actual_result = self.driver.find_element(*self.CART_TEXT).text
        assert actual_result == "Your Amazon Cart is empty", \
            f'Error, expected "Your Amazon Cart is empty.", but got {actual_result}'
