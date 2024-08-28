from pages.base_page import Page


class ReellyTelegramNewsPage(Page):

    def verify_tnp_url(self):
        self.verify_partial_url('t.me')
