import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@when(u'slide to 100k pageviews')
def step_impl(context):
    context.page.fill(locator.slider,'50')
    views = context.page.locator(locator.page_views).text_content()
    assert views == "100K PageViews"

@then(u'the price should be $16.00 / month')
def step_impl(context):
    price = context.page.locator(locator.dollar_price_permonth).text_content()
    assert price == "$16.00"

@then(u'the price should be $12.00 / year in 100k')
def step_impl(context):
    price = context.page.locator(locator.dollar_price_permonth).text_content()
    assert price == "$12.00"