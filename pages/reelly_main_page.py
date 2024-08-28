from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ReellyMainPage(Page):
    SETTINGS_TXT = (By.XPATH,'//div[text() = "Settings"]')

    def option_settings(self):
        sleep(2)
        self.click(*self.SETTINGS_TXT)

