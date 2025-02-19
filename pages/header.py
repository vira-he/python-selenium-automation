from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    SEARCH_FIELD = By.ID, "twotabsearchtextbox"
    SUBMIT_BTN = By.ID, "nav-search-submit-button"
    ORDERS_BTN = By.ID, "nav-orders"
    CART_BTN = By.ID, "nav-cart"
    BS_BTN = By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]"
    POPUP_SIGNIN_BTN = By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button"
    LANG_OPTIONS = By.ID, "icp-nav-flyout"
    SPANISH_LANG = By.CSS_SELECTOR, "a[href='#switch-lang=es_US']"
    DEPT_SELECT = By.ID, "searchDropdownBox"

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SUBMIT_BTN)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def click_best_sellers(self):
        self.click(*self.BS_BTN)

    def click_signin_popup(self):
        self.click(*self.POPUP_SIGNIN_BTN)

    def hover_lang(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)

        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def verify_spanish_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def open_cart(self):
        self.click(*self.CART_BTN)

    def select_dept(self):
        dept_select = self.find_element(*self.DEPT_SELECT)
        select = Select(dept_select)
        select.select_by_value("search-alias=hpc")
