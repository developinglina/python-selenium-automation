from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class TargetAppPage(Page):
    TERMS_LINK = (By.LINK_TEXT, "Target terms and conditions")
    TERMS_HEADER = (By.CSS_SELECTOR, 'h1[data-test="page-title"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # 10 seconds wait time

    def open_sign_in_page(self):
        self.driver.get(
            'https://www.target.com/orders?lnk=acct_nav_my_account')

    def click_on_terms_link(self):
        self.click(*self.TERMS_LINK)

    def verify_terms_page(self):
        header = self.driver.find_element(*self.TERMS_HEADER)
        print("Header text:", header.text)
        return header.is_displayed()

    def get_current_window_id(self):
        window = self.driver.current_window_handle
        print(f'Original window: {window}')
        return window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print(f'Switching to a new window: {all_windows[1]}')
        self.driver.switch_to.window(all_windows[1])

    def close_window(self):
        self.driver.close()

    def switch_to_window_by_id(self, window_id):
        print(f'Switching to window: {window_id}')
        self.driver.switch_to.window(window_id)
