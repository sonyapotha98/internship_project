from pages.base_page import Page


class ReellyWhatsappSupportPage(Page):

    def verify_wsp_url(self):
        self.verify_partial_url('api.whatsapp.com')