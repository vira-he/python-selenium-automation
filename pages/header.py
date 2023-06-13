from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Header(Page):
    SEARCH_FIELD = By.ID, "twotabsearchtextbox"
    SUBMIT_BTN = By.ID, "nav-search-submit-button"
    ORDERS_BTN = By.ID, "nav-orders"
    LANG_OPTIONS =
    SPANISH_LANG =

    def search_for_product(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SUBMIT_BTN)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def hover_lang(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)

        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def verify_spanish_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)