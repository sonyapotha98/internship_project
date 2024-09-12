from behave import given, when, then
from time import sleep


@when('Switch to the new tab')
def switch_window(context):
    context.app.reelly_settings_page.switch_to_new_window()
    sleep(2)


@then('Verify whatsapp support page opened')
def verify_whatsapp_support_page_opened(context):
    context.app.reelly_whatsapp_support_page.verify_wsp_url()
    sleep(6)


@then('Close and Go back to original window')
def close_and_return(context):
    context.app.reelly_whatsapp_support_page.close()
    context.app.reelly_whatsapp_support_page.switch_to_window_by_id(context.original_window)





