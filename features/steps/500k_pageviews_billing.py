import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@when(u'slide to 500k pageviews')
def step_impl(context):
    context.page.fill(locator.slider,'75')

@then(u'the price should be $24.00 / month')
def step_impl(context):
    price = context.page.locator(locator.dollar_price_permonth).text_content()
    assert price == "$24.00"

@then(u'the price should be $18.00 / year')
def step_impl(context):
    price = context.page.locator(locator.dollar_price_permonth).text_content()
    assert price == "$18.00"