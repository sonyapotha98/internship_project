from app.application import Application
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def browser_init(context,scenario_name):
    """
    :param context: Behave context
    """
    ### CHROME ####
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)


    # ### FIREFOX ####
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)


    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )
    #
    # ### Mobile Emulation ###
    # mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # # driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=chrome_options.to_capabilities())
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)


    # ### BROWSERSTACK ###
    # bs_user = 'sonyapotha_IDjqPV'
    # bs_key = '8WixNvQ43Xx7y3oyJYp3'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # # options.add_argument("--disable-notifications")  # Disable notifications
    # # options.add_argument("--disable-popup-blocking")  # Disable pop-up blocking
    # bstack_options = {
    #     'deviceName': 'iPhone 12 Pro',
    #     'osVersion': '17',
    #     'browserName': 'chrome',
    #     'sessionName': scenario_name
    # }
    #
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    # context.driver.set_window_size(390, 844)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
