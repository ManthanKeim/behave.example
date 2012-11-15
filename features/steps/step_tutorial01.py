# -*- coding: UTF-8 -*-
"""
Based on ``behave tutorial``
"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then

@given('we have behave installed')
def step(context):
    pass

@when('we implement a test')
def step(context):
    assert True is not False

@then('behave will test it for us!')
def step(context):
    assert context.failed is False
