from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ProductPage(Page):
    NEW_ARRIVALS_BTN = By.XPATH, "//a[contains(@href, '/New-Arrivals/')]"
    NEW_ARRIVALS_OPT = By.XPATH, "//*[@class='mm-category-list']//*[text()='Women']"

    def open_amazon_product(self, product):
        self.open_url('https://www.amazon.com/gp/product/' + product)

    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS_BTN)

        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_can_see_deals(self):
        self.find_element(*self.NEW_ARRIVALS_OPT)