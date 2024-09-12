from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class ReellyMainPage(Page):
    # SETTINGS_TXT = (By.XPATH,'//div[text() = "Settings"]')
    SETTINGS_TXT = (By.CSS_SELECTOR, ".menu-button-block[href='/settings']")
    MAIN_MENU_BTN = (By.CSS_SELECTOR,'[class *= "assistant-button"][href *= "main-menu"]')
    USER_PROFILE_BTN = (By.CSS_SELECTOR,'[class *= "menu-photo"][href *= "setting"]')
    def option_settings(self):
        self.click(*self.SETTINGS_TXT)
    def main_menu(self):
        self.click(*self.MAIN_MENU_BTN)
        sleep(5)

    def user_profile(self):
        self.click(*self.USER_PROFILE_BTN)
        sleep(5)

