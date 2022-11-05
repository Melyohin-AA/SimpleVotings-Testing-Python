import features.parsers
from features.steps.browser import Browser
from features.steps.registration import Registration


def before_all(context):
    Browser.open(context)


def after_all(context):
    context.driver.quit()


def before_scenario(context, scenario):
    Browser.reset(context)


def after_scenario(context, scenario):
    Registration.try_delete(context)
