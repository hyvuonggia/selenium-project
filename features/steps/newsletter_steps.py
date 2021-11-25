from behave import *
import parse
import random
import string

@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text

register_type(NullableString = parse_nullable_string)

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def random_email():
    return random_char(5)+"@mail.com"

@given(u'the newsletter email is filled with random email address')
def step_impl(context):
    context.driver.find_element_by_id('newsletter-input').send_keys(random_email())

@given(u'the newsletter email is filled with "{email:NullableString}"')
def step_impl(context, email):
    context.driver.find_element_by_id('newsletter-input').send_keys(email)

@when('the submit button is clicked')
def step_impl(context):
    context.driver.find_element_by_name('submitNewsletter').click()


@then(u'a newsletter "{msg}" message appear')
def step_impl(context, msg):
    response = context.driver.find_element_by_xpath('//*[@id="columns"]/p').text
    assert response == msg
    context.driver.close()