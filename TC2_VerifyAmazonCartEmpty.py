from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-cart').click()

expected_result = "Your Amazon Cart is empty."
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-mini a-spacing-top-base']").text

assert expected_result == actual_result, f'Error! Expected {expected_result} but got actual {actual_result}'

print ("Test case passed")

sleep(10)