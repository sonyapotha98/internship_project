from behave import given, when, then



@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.reelly_settings_page.get_current_window()


@when('Click on support option')
def click_support(context):
    context.app.reelly_settings_page.option_support()

@then('Verify the settings page opens')
def verify_settings_page_open(context):
    context.app.reelly_settings_page.verify_settings_page_url()

@then('Verify there are 12 options for the settings')
def verify_settings_page_12options(context):
    context.app.reelly_settings_page.verify_12_settings_options()

@then('Verify “connect the company” button is available')
def verify_connect_the_company_btn_available(context):
    context.app.reelly_settings_page.verify_ctc_available()



@then('Click on news option')
def click_news(context):
    context.app.reelly_settings_page.option_news()


@then('Verify telegram news page opened')
def verify_telegram_news_page_opened(context):
    context.app.reelly_telegram_news_page.verify_tnp_url()


@given('Click on Secondary option at the left side menu')
def click_secondary_option(context):
    context.app.reelly_main_page.option_secondary()