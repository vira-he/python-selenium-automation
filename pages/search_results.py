from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResults(Page):
    SEARCH_RESULT_TEXT = By.XPATH, "//span[@class='a-color-state a-text-bold']"

    def verify_search_results(self):
        expected_result = '"table"'
        actual_result = self.driver.find_element(*self.SEARCH_RESULT_TEXT).text
        assert expected_result == actual_result, \
            f'Error! Expected {expected_result} but got actual {actual_result}'
