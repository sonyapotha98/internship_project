from pages.base_page import Page
from pages.reelly_main_page import ReellyMainPage
from pages.reelly_settings_page import ReellySettingsPage
from pages.reelly_signin_page import ReellySigninPage
from pages.reelly_telegram_news_page import ReellyTelegramNewsPage
from pages.reelly_whatsapp_support_page import ReellyWhatsappSupportPage
from pages.reelly_secondary_page import ReellySecondaryPage

class Application:
    def __init__(self,driver):

        self.base_page = Page(driver)

        self.reelly_main_page = ReellyMainPage(driver)
        self.reelly_settings_page = ReellySettingsPage(driver)
        self.reelly_signin_page = ReellySigninPage(driver)
        self.reelly_telegram_news_page = ReellyTelegramNewsPage(driver)
        self.reelly_whatsapp_support_page = ReellyWhatsappSupportPage(driver)
        self.reelly_secondary_page = ReellySecondaryPage(driver)
