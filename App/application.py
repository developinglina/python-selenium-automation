from pages.base_page import Page
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import Cart
from pages.sign_in_page import SignIn
from pages.target_app_page import TargetAppPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = Cart(driver)
        self.sign_in_page = SignIn(driver)
        self.target_app_page = TargetAppPage(driver)


