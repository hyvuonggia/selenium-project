from behave import *
import parse

@parse.with_pattern(r'.*')
def parse_nullable_string(text):
    return text

register_type(NullableString = parse_nullable_string)

@given(u'the search bar is filled with "{item:NullableString}"')
def step_impl(context, item):
    context.driver.find_element_by_id('search_query_top').send_keys(item)


@when(u'the search button is clicked')
def step_impl(context):
    context.driver.find_element_by_name('submit_search').click()


@then(u'the page with searched item "{searched_item}" appear')
def step_impl(context, searched_item):
    assert context.driver.title == 'Search - My Store'
    item = context.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span').text
    print("------------> item: " + item)
    print("------------> searched_item: " + searched_item)
    assert item == '"' + searched_item.upper() + '"'
    context.driver.close()
    
@then(u'a "{msg}" search message is displayed')
def step_impl(context, msg):
    fail_res = context.driver.find_element_by_xpath('//*[@id="center_column"]/p').text
    print("------------> fail_res: " + fail_res)
    print("------------> msg: " + msg)
    assert fail_res == msg
    context.driver.close()