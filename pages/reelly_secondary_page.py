from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class ReellySecondaryPage(Page):
    GRID = (By.XPATH, '//div[@wized="listingCardMLS"]')
    CURRENT_PAGE = (By.CSS_SELECTOR,'[wized="currentPageProperties"]')
    TOTAL_PAGE = (By.CSS_SELECTOR,'[wized="totalPageProperties"]')
    NEXT_BTN = (By.CSS_SELECTOR,'[wized="nextPageMLS"]')
    PREVIOUS_BTN = (By.CSS_SELECTOR,'[wized="previousPageMLS"]')

    def verify_secondary_page_url(self):
        self.verify_partial_url('secondary-listings')

    def go_to_last_page(self):
        i = 1
        self.wait_until_elements_visible(*self.GRID)
        sleep(2)
        current_page = self.find_text(*self.CURRENT_PAGE)
        print(f"Current page: {current_page}")
        total_page = self.find_text(*self.TOTAL_PAGE)
        print(f"total_page: {total_page}")

        while i <= int(total_page):
            self.wait_until_elements_visible(*self.GRID)
            sleep(2) #had to use sleep for fully loading the page
            self.wait_for_element_appear(*self.CURRENT_PAGE)
            self.click(*self.NEXT_BTN)
            i += 1
        current_page = self.find_text(*self.CURRENT_PAGE)
        if int(current_page) == 98:
            print(f"Reached Final page : {current_page}")
        else:
            raise Exception(f"Next Button Break at page {current_page} ")

        sleep(5)

    def go_to_first_page(self):
        self.wait_until_elements_visible(*self.GRID)
        sleep(2)
        total_page = self.find_text(*self.TOTAL_PAGE)
        i = int(total_page)

        current_page = self.find_text(*self.CURRENT_PAGE)
        print(f"Initial Current page: {current_page}")
        total_page = self.find_text(*self.TOTAL_PAGE)
        print(f"total_page: {total_page}")

        while i >= 1:
            self.wait_until_elements_visible(*self.GRID)
            sleep(2) #had to use sleep for fully loading the page
            self.wait_for_element_appear(*self.CURRENT_PAGE)
            self.click(*self.PREVIOUS_BTN)
            i -= 1
        current_page = self.find_text(*self.CURRENT_PAGE)
        if int(current_page) == 1:
            print(f"Final Current page : {current_page}")
        else:
            raise Exception(f"Next Button Break at page {current_page} ")







