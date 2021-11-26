from behave import *
import parse

@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text

register_type(NullableString = parse_nullable_string)

@given(u'the email is a random email')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the email is a random email')


@given(u'Create an account button is clicked')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Create an account button is clicked')


@given(u'title "Mr." checkbox is checked')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given title "Mr." checkbox is checked')


@given(u'customer first name is filled with "Joe"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given customer first name is filled with "Joe"')


@given(u'customer last name is filled with "Biden"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given customer last name is filled with "Biden"')


@given(u'Password is filled with "qwerty123"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Password is filled with "qwerty123"')


@given(u'signup for newsletter checkbox is checked')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given signup for newsletter checkbox is checked')


@given(u'recieve offers checkbox is checked')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given recieve offers checkbox is checked')


@given(u'first name is filled with "Joe"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given first name is filled with "Joe"')


@given(u'last name is filled with "Biden"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given last name is filled with "Biden"')


@given(u'company name is filled with "White House"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given company name is filled with "White House"')


@given(u'address is filled with "1600 Pennsylvania Avenue NW"')   
def step_impl(context):
    raise NotImplementedError(u'STEP: Given address is filled with "1600 Pennsylvania Avenue NW"')


@given(u'city is filled with "Washington D.C"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given city is filled with "Washington D.C"')


@given(u'state is filled with "Washington"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given state is filled with "Washington"')


@given(u'the zip code is "20500"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the zip code is "20500"')


@given(u'the country is "United States"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the country is "United States"')


@given(u'the additional information is filled with "I am the president of the USA"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the additional information is filled with "I am the president of the USA"')


@given(u'the mobile phone is "+123456789"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the mobile phone is "+123456789"')


@given(u'the address alias is filled with "whitehouse"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the address alias is filled with "whitehouse"')


@when(u'the register button is clicked')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the register button is clicked')