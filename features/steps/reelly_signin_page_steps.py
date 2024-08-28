from behave import given, when, then


@given('Open the signin page')
def open_reelly(context):
    context.app.reelly_signin_page.open()


@given('Log in to the page')
def log_in_to_reelly(context):
    context.app.reelly_signin_page.login()
