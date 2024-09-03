from behave import given, when, then
from time import sleep


@given('Click on settings option')
def click_settings(context):
    context.app.reelly_main_page.option_settings()

