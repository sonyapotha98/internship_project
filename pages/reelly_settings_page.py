from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ReellySettingsPage(Page):
    # SUPPORT_BTN = (By.XPATH,'//div[@class = "setting-text"] [text() = "Support"]')
    SUPPORT_BTN = (By.CSS_SELECTOR, 'a[href*="https://api.whatsapp.com/"]')
    NEWS_BTN = (By.XPATH,'//div[@class = "setting-text"] [text() = "News"]')

    def option_support(self):
        # sleep(2)
        # self.driver.execute_script("window.scrollBy(0, 300);")
        # # sleep(5)
        self.click(*self.SUPPORT_BTN)
        sleep(5)

    def option_news(self):
        # sleep(2)
        # self.driver.execute_script("window.scrollBy(0, 300);")
        # sleep(5)
        self.click(*self.NEWS_BTN)
        sleep(5)




