from pages.base_page import Page
from selenium.webdriver.common.by import By


class ReellySigninPage(Page):
    EMAIL_FEILD = (By.CSS_SELECTOR,'#email-2')
    PWD_FIELD = (By.CSS_SELECTOR,'#field')
    CONTINUE_BTN = (By.CSS_SELECTOR,'[class *= "login-button"]')

    def open(self):
        self.open_url('https://soft.reelly.io/sign-in')

    def login(self):
        self.input_text('******',*self.EMAIL_FEILD)
        self.input_text('******',*self.PWD_FIELD)
        self.click(*self.CONTINUE_BTN)

