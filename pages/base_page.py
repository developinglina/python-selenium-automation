class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, '...'


def get_current_window_id(self):
    window = self.driver.current_window_handle
    print(f'Original window: {window}')
    return window


def switch_to_window_by_id(self, window_id):
    print(f'Switching to window: {window_id}')
    self.driver.switch_to.window(window_id)


def close_window(self):
    self.driver.close()
