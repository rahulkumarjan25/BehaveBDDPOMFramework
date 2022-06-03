import allure
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

from Utilities import configReader


def before_scenario(context, driver):
    if configReader.readConfig("basic info", "browser") == "chrome":
        context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    if configReader.readConfig("basic info", "browser") == "firefox":
        context.driver = webdriver.firefox(executable_path=GeckoDriverManager().install())
    if configReader.readConfig("basic info", "browser") == "IE":
        context.driver = webdriver.firefox(executable_path=IEDriverManager().install())


def after_scenario(context, step):
    context.driver.close()


def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
