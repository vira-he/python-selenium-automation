from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SIGNIN_HEADER = By.XPATH, "//h1[@class = 'a-spacing-small']"
    EMAIL = (By.ID, "ap_email")

    def verify_signin_opens(self):
        self.driver.wait.untill(EC.url_contins('https://www.amazon.com/ap/signin'))
        self.verify_element_text("Sign in", *self.SIGNIN_HEADER)
        self.find_element(*self.EMAIL)
