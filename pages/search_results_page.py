from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.CSS_SELECTOR,
                                          "span.h-text-bs.h-display-flex.h-flex-align-center.h-text-grayDark.h-margin-l-x2")

    def verify_search_results(self):
        actual_text = self.find_element(*self.SEARCH_RESULTS_TXT).text
        assert 'tea' in actual_text, f"Error, expected 'tea' not in actual {actual_text}"