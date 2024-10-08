from behave import given, when, then

@then('Verify the Secondary page opens')
def verify_secondary_page_url(context):
    context.app.reelly_secondary_page.verify_secondary_page_url()


@then('Go to the final page using the pagination button')
def go_to_last_secondary_page(context):
    context.app.reelly_secondary_page.go_to_last_page()


@then('Go back to the first page using the pagination button')
def go_to_first_secondary_page(context):
    context.app.reelly_secondary_page.go_to_first_page()