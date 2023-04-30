from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Practice with locators.
# Create locators + search strategy for these page elements of Amazon Sign in page:
# Amazon logo:

driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Email field

driver.find_element(By.ID, "ap_email")

# Continue button

driver.find_element(By.ID, "continue")

# Need help link

driver.find_element(By.XPATH, "//a[@data-csa-c-func-deps='aui-da-a-expander-toggle']")

# Forgot your password link

driver.find_element(By.ID, "auth-fpp-link-bottom")

# Other issues with Sign-In link

driver.find_element(By.ID, "ap-other-signin-issues-link")

# Create your Amazon account button

driver.find_element(By.ID, "createAccountSubmit")

# *Conditions of use link

driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# *Privacy Notice link

driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
