from behave import *

use_step_matcher("parse")

# locators

register_button = "//a[normalize-space()='Register']"


@step('I click on Register')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.execute_steps(f"given I click the link with text=Register")


@step('I fill out the Register Form')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.execute_steps(f"given I type Random First Name in the field with id=customer.firstName \n\
        and I type Random Last Name in the field with id=customer.lastName \n\
                          and I type 123 Test Road in the field with id=customer.address.street \n\
                          and I type Random City in the field with id=customer.address.city \n\
                          and I type Random State in the field with id=customer.address.state \n\
                          and I type Random Zip Code in the field with id=customer.address.zipCode \n\
                          and I type Random Phone Number in the field with id=customer.phoneNumber \n\
                          and I type Random SSN in the field with id=customer.ssn \n\
                          and I type Random Username in the field with id=customer.username \n\
                          and I type Random Password in the field with id=customer.password \n\
                          and I type Previous Password in the field with id=repeatedPassword")


@step("I submit the Register Form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.execute_steps(f"given I click the input with value=Register")


@then("I validate the account is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    message = f"Your account was created successfully. You are now logged in."
    context.execute_steps(
        f"given I check {message} is present in the page"
    )