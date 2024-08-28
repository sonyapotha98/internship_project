from behave import given, when, then


@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.reelly_settings_page.get_current_window()


@when('Click on support option')
def click_support(context):
    context.app.reelly_settings_page.option_support()


@then('Click on news option')
def click_news(context):
    context.app.reelly_settings_page.option_news()


@then('Verify telegram news page opened')
def verify_telegram_news_page_opened(context):
    context.app.reelly_telegram_news_page.verify_tnp_url()
