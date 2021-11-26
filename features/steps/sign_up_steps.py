from behave import *
import parse
import newsletter_steps
from selenium.webdriver.support.select import Select

@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text

register_type(NullableString = parse_nullable_string)

@given(u'the email is a random email')
def step_impl(context):
    context.driver.find_element_by_id("email_create").send_keys(newsletter_steps.random_email())

@given(u'Create an account button is clicked')
def step_impl(context):
    context.driver.find_element_by_id("SubmitCreate").click()


@given(u'title "{title:NullableString}" checkbox is checked')
def step_impl(context, title):
    context.driver.implicitly_wait(10)
    if title == "Mr.":
        context.driver.find_element_by_id("id_gender1").click()
    elif title == "Mrs.":
        context.driver.find_element_by_id("id_gender2").click()
    else:
        assert True

@given(u'customer first name is filled with "{customerFirstName:NullableString}"')
def step_impl(context, customerFirstName):
    context.driver.find_element_by_id("customer_firstname").send_keys(customerFirstName)

@given(u'customer last name is filled with "{customerLastName}"')
def step_impl(context,customerLastName):
    context.driver.find_element_by_id('customer_lastname').send_keys(customerLastName)


@given(u'Password is filled with "{password:NullableString}"')
def step_impl(context, password):
    context.driver.find_element_by_id('passwd').send_keys(password)


@given(u'signup for newsletter checkbox is checked')
def step_impl(context):
   context.driver.find_element_by_id("newsletter").click()


@given(u'recieve offers checkbox is checked')
def step_impl(context):
    context.driver.find_element_by_id("uniform-optin").click()


@given(u'first name is filled with "{firstname:NullableString}"')
def step_impl(context, firstname):
    context.driver.find_element_by_id('firstname').send_keys(firstname)


@given(u'last name is filled with "{lastname}"')
def step_impl(context, lastname):
    context.driver.find_element_by_id('lastname').send_keys(lastname)


@given(u'company name is filled with "{company}"')
def step_impl(context, company):
    context.driver.find_element_by_id('company').send_keys(company)


@given(u'address is filled with "{address}"')   
def step_impl(context, address):
    context.driver.find_element_by_id('address1').send_keys(address)


@given(u'city is filled with "{city}"')
def step_impl(context, city):
    context.driver.find_element_by_id('city').send_keys(city)


@given(u'state is filled with "{state}"')
def step_impl(context, state):
    select = Select(context.driver.find_element_by_id("id_state"))
    select.select_by_visible_text(state)


@given(u'the zip code is "{postcode}"')
def step_impl(context,postcode):
    context.driver.find_element_by_id('postcode').send_keys(postcode)


@given(u'the country is "{country}"')
def step_impl(context, country):
    select = Select(context.driver.find_element_by_id("id_country"))
    select.select_by_visible_text(country)


@given(u'the additional information is filled with "{additionalInfo:NullableString}"')
def step_impl(context, additionalInfo):
    context.driver.find_element_by_id("other").send_keys(additionalInfo)


@given(u'the mobile phone is "{phone:NullableString}"')
def step_impl(context, phone):
    context.driver.find_element_by_id("phone_mobile").send_keys(phone)


@given(u'the address alias is filled with "{alias}"')
def step_impl(context, alias):
    context.driver.find_element_by_id("alias").send_keys(alias)


@when(u'the register button is clicked')
def step_impl(context):
    context.driver.find_element_by_id("submitAccount").click()

@then('the registered fail "{failMsg}" message appear')
def step_impl(context, failMsg):
    msg = context.driver.find_element_by_xpath('//*[@id="center_column"]/div/ol/li').get_attribute('innerHTML')
    print("-------> msg: " + msg)
    print("-------> failMsg: " + failMsg)
    assert failMsg == msg
    context.driver.close()


@given(u'the sign up email is "{email}"')
def step_impl(context, email):
    context.driver.find_element_by_id("email_create").send_keys(email)


@when(u'Create an account button is clicked')
def step_impl(context):
    context.driver.find_element_by_id("SubmitCreate").click()


@then(u'a using registered email error message appear')
def step_impl(context):
    context.driver.implicitly_wait(10)
    fail_msg = context.driver.find_element_by_xpath('//*[@id="create_account_error"]/ol/li').get_attribute('innerHTML')
    msg = 'An account using this email address has already been registered. Please enter a valid password or request a new one.'
    print("------------> fail_msg: " + fail_msg)
    print("------------>      msg: " + msg)
    assert fail_msg.strip() == msg.strip()
    context.driver.close()
