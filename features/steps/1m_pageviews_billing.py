import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@when(u'slide to 1m pageviews')
def step_impl(context):
    context.page.fill(locator.slider,'100')
    views = context.page.locator(locator.page_views).text_content()
    assert views == "1M PageViews"

@then(u'the price should be $36.00 / month')
def step_impl(context):
    price = context.page.locator(locator.dollar_price_permonth).text_content()
    assert price == "$36.00"

@then(u'the price should be $27.00 / year')
def step_impl(context):
    price = context.page.locator(locator.dollar_price_permonth).text_content()
    assert price == "$27.00"