from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResults(Page):
    SEARCH_RESULT_TEXT = By.XPATH, "//span[@class='a-color-state a-text-bold']"
    HCP_DEP = By.CSS_SELECTOR, "[data-category='hpc']"

    def verify_search_results(self, expected_result):
        actual_result = self.driver.find_element(*self.SEARCH_RESULT_TEXT).text
        assert expected_result == actual_result, \
            f'Error! Expected {expected_result} but got actual {actual_result}'

    def verify_dept(self):
        self.wait_for_element_appear(*self.HCP_DEP)
