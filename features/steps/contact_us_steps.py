import os
from behave import *
import parse
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text

register_type(NullableString = parse_nullable_string)

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

@given('the home page is opened')
def step_impl(context):
    driver.implicitly_wait(10)
    driver.get("http://automationpractice.com")
    driver.maximize_window()

@given('the Contact us button is clicked')
def step_impl(context):
    driver.find_element_by_id("contact-link").click()
    # assert driver.title == "Contact us - My Store"


@given('the subject heading is "{subject:NullableString}"')
def step_impl(context, subject):
    select = Select(driver.find_element_by_id("id_contact"))
    select.select_by_visible_text(subject)
    

@given('the email address is filled with "{email:NullableString}"')
def step_impl(context, email):
    driver.find_element_by_id("email").send_keys(email)


@given('order reference is filled with "{order:NullableString}"')
def step_impl(context, order):
    driver.find_element_by_id("id_order").send_keys(order)


@given('the attach file is "{attachment:NullableString}"')
def step_impl(context, attachment):
    if attachment.strip() != "":
        driver.find_element_by_id("fileUpload").send_keys(os.getcwd() + "\\features\\steps" + attachment)
    else :
        assert True

@given('the message is filled with "{message:NullableString}"')
def step_impl(context, message):
    driver.find_element_by_id("message").send_keys(message)


@when('the send button is clicked')
def step_impl(context):
    driver.find_element_by_id("submitMessage").click()


@then('a "{msg}" message is shown')
def step_impl(context, msg):
    try:
        succ_res = driver.find_element_by_xpath('//*[@id="center_column"]/p').text
        print("--> succ_res: " + succ_res)
        print("--> msg: " + msg)
        assert succ_res == msg
    except:
        fail_res = driver.find_element_by_xpath('//*[@id="center_column"]/div/ol/li').text
        print('fail_res: ' + fail_res)
        print("--> msg: " + msg)
        assert fail_res == msg
    # finally:
    #     driver.close()