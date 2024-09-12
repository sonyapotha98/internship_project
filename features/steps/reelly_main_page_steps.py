from behave import given, when, then
from time import sleep

@given('Click on settings option')
def click_settings(context):
    context.app.reelly_main_page.option_settings()

@given('Click on Main menu')
def click_main(context):
    context.app.reelly_main_page.main_menu()

@given('Click on User profile')
def click_user_profile(context):
    context.app.reelly_main_page.user_profile()



