from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignIn(Page):

    USERNAME_FIELD = (By.ID, "username")

    def verify_sign_in_form(self):
        input_field = self.find_element(*self.USERNAME_FIELD)
        assert input_field.is_displayed()
        print("sign in form is displayed")
