from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import time
from selenium.common.exceptions import TimeoutException


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=15)
        self.elements = None
        self.element = None

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        self.driver.find_element(*locator)

    def find_elements(self, *locator):
        self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self,text,*locator):
        self.driver.find_element(*locator).send_keys(text)

    def find_text(self,*locator):
        # print(self.driver.find_element(*locator).text)
        return self.driver.find_element(*locator).text


    def get_current_window(self):
        window = self.driver.current_window_handle
        print('Current window:', window)
        return window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        windows = self.driver.window_handles
        sleep(5)
        print(f'All windows {windows}')
        if len(windows) > 1:
            self.driver.switch_to.window(windows[1])
            print(f'Switched to window => {windows[1]}')

        else:
            raise Exception("No new window to switch to!")

    # def switch_to_new_window(self, timeout=15):
    #     windows_before = self.driver.window_handles
    #     start_time = time.time()
    #
    #     while time.time() - start_time < timeout:
    #         windows_after = self.driver.window_handles
    #         if len(windows_after) > len(windows_before):
    #             self.driver.switch_to.window(windows_after[-1])  # Switch to the newest window
    #             return
    #         time.sleep(1)  # Wait for 1 second before checking again
    #
    #     raise TimeoutException("No new window appeared within the timeout period.")


    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)
        print(f'Switched to window => {window_id}')

    def close(self):
        self.driver.close()

    def wait_until_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by locator {locator} not clickable'
        )

    def wait_until_elements_visible(self, *locator):
        self.elements = self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_until_element_visible(self, *locator):
        self.element = self.wait.until(EC.presence_of_element_located(locator))


    def wait_and_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by locator {locator} not clickable'
        ).click()

    # def move_to_element_and_click(self, *locator):
    #     element = self.wait.until(EC.visibility_of_element_located(locator))
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(element).pause(2).click()
    #     actions.perform()

    def wait_for_element_appear(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by locator {locator} did not appear'
        )

    def wait_for_element_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by locator {locator} shown, but should not appear'
        )

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, f'Expected {expected_text} did not match actual {actual_text}'

    def verify_partial_text(self, expected_partial_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_partial_text in actual_text, f'Expected {expected_partial_text} not in actual {actual_text}'

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected {expected_url} but got {actual_url}'

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, f'Expected {expected_partial_url} not in {actual_url}'