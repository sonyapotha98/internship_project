from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class ReellyMainPage(Page):
    # SETTINGS_TXT = (By.XPATH,'//div[text() = "Settings"]')
    SETTINGS_TXT = (By.CSS_SELECTOR, ".menu-button-block[href='/settings']")
    
    def option_settings(self):
        self.click(*self.SETTINGS_TXT)

