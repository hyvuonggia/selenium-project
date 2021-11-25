from behave import *
import parse

@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text

register_type(NullableString = parse_nullable_string)


@given(u'the Sign in link is clicked')
def step_impl(context):
    context.driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()


@given(u'the email is "{email:NullableString}"')
def step_impl(context, email):
    context.driver.find_element_by_id('email').send_keys(email)


@given(u'the password is "{password:NullableString}"')
def step_impl(context, password):
    context.driver.find_element_by_id('passwd').send_keys(password)


@when(u'the Sign in button is clicked')
def step_impl(context):
    context.driver.find_element_by_id('SubmitLogin').click()


@then(u'the title "My account - My Store" appear')
def step_impl(context):
    assert context.driver.title == 'My account - My Store'
    context.driver.close()

@then(u'a "{msg}" message appear')
def step_impl(context, msg):
    error_message = context.driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/ol/li').text
    print("--> error_message" + error_message)
    print("--> msg" + msg)
    assert error_message == msg
    context.driver.close()