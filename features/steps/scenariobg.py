"""
Для сценариев с одинаковыми шагами в одной *.feature создается отдельный блок Background
"""
from behave import *


@given(u'I launch browser')
def step_impl(context):
    assert True, 'Test passed'


@when(u'I open application')
def step_impl(context):
    assert True, 'Test passed'


@when(u'Enter valid username and password')
def step_impl(context):
    assert True, 'Test passed'


@when(u'Click on login')
def step_impl(context):
    assert True, 'Test passed'


@then(u'User dashboard is displayed')
def step_impl(context):
    assert True, 'Test passed'


@when(u'navigate to search page')
def step_impl(context):
    assert True, 'Test passed'


@then(u'search page should be display')
def step_impl(context):
    assert True, 'Test passed'


@when(u'navigate to advanced search page')
def step_impl(context):
    assert True, 'Test passed'


@then(u'advanced search page should be display')
def step_impl(context):
    assert True, 'Test passed'