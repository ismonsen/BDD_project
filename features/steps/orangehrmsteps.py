from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@given(u'launch Chrome')
def launch_chrome(context):
    s = Service('chromedriver.exe')
    context.driver = webdriver.Chrome(service=s)


@when(u'open orangehrm homepage')
def open_page(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com')


@then(u'verify that logo presents on page')
def verify_logo(context):
    status = context.driver.find_element(By.XPATH, '//*[@id="divLogo"]/img').is_displayed()
    assert status is True


@then(u'close browser')
def close_browser(context):
    context.driver.close()
