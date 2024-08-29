from pages.base_page import Page
from selenium.webdriver.common.by import By


class ReellyMainPage(Page):
    SETTINGS_TXT = (By.XPATH,'//div[text() = "Settings"]')

    def option_settings(self):
        self.wait_and_click(*self.SETTINGS_TXT)

