from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@given('I launch Chrome')
def start_chrome(context):
    s = Service('chromedriver.exe')
    context.driver = webdriver.Chrome(service=s)


@when('Enter orangehrm homepage')
def home(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com')


@when('Enter username "{username}" and password "{password}"')
def login(context, username, password):
    context.driver.find_element(By.ID, 'txtUsername').send_keys(username)
    context.driver.find_element(By.ID, 'txtPassword').send_keys(password)


@when('Click on login button')
def click(context):
    context.driver.find_element(By.ID, 'btnLogin').click()


@then('Verify dashboard loaded')
def dashboard(context):
    head = context.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/h1').text
    assert head == 'Dashboard'
    context.driver.close()
