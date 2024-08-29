from pages.base_page import Page
from selenium.webdriver.common.by import By


class ReellySettingsPage(Page):
    SUPPORT_BTN = (By.XPATH,'//div[@class = "setting-text"] [text() = "Support"]')
    NEWS_BTN = (By.XPATH,'//div[@class = "setting-text"] [text() = "News"]')

    def option_support(self):
        self.click(*self.SUPPORT_BTN)

    def option_news(self):
        self.click(*self.NEWS_BTN)




