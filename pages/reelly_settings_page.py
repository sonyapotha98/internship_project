from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ReellySettingsPage(Page):
    # SUPPORT_BTN = (By.XPATH,'//div[@class = "setting-text"] [text() = "Support"]')
    SUPPORT_BTN = (By.CSS_SELECTOR, 'a[href*="https://api.whatsapp.com/"]')
    NEWS_BTN = (By.XPATH,'//div[@class = "setting-text"] [text() = "News"]')
    SETTINGS_PAGE_OPTIONS = (By.CSS_SELECTOR,'a.page-setting-block.w-inline-block')
    CONNECT_THE_CMPY_BTN = (By.CSS_SELECTOR,'div.settings-profile-block a.button-link-menu[href *= "book"]')


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

    def verify_settings_page_url(self):
        self.verify_partial_url('settings')

    def verify_12_settings_options(self):

        self.wait_until_elements_visible(*self.SETTINGS_PAGE_OPTIONS)
        assert len(self.elements) == 12, f"Expected 12 settings options, got {len(self.elements)}"
        # for value, element in enumerate(self.elements):
        #     print(f'{value+1}.{element.text}')

    def verify_ctc_available(self):
        self.wait_until_element_visible(*self.CONNECT_THE_CMPY_BTN)
        # print(f'{self.element.text} is available')






