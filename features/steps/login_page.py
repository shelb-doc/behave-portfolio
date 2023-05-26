from behave import *

use_step_matcher("parse")


@step('I fill out the login Form')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    username = context.config.userdata["username"]
    password = context.config.userdata["password"]
    context.execute_steps(f"given I type {username} in the field with name=username \n\
        and I type {password} in the field with name=password")


@step("I submit the login Form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.execute_steps(f"given I click the input with value=Log In")


@then("I validate the Login is successful")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    message = f"Account Services"
    context.execute_steps(
        f"given I check {message} is present in the page"
    )