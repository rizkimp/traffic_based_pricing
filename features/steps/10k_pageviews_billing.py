import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@given(u'visit bitcoin price calculator')
def step_impl(context):
    context.page.goto(locator.dev_url)
    time.sleep(1)

@when(u'slide to 10k pageviews')
def step_impl(context):
    context.page.fill(locator.slider,'0')

@then(u'the price should be $8.00 / month')
def step_impl(context):
    price = context.page.locator(locator.dollar_price_permonth).text_content()
    assert price == "$8.00"

@when(u'switch to yearly billing')
def step_impl(context):
    context.page.locator(locator.button_billing).click()

@then(u'the price should be $6.00 / year')
def step_impl(context):
    price = context.page.locator(locator.dollar_price_permonth).text_content()
    assert price == "$6.00"