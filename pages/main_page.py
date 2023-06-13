from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):
    POPUP_SIGNIN_BTN = By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button"

    def open_main_page(self):
        self.open_url("https://www.amazon.com/")

    def click_signin_popup(self):
        self.click(*self.POPUP_SIGNIN_BTN)
