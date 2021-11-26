Feature: AutomationPractice sign up test

    Background:
        Given the home page is opened
        And the Sign in link is clicked

    Scenario: 
        Given the email is a random email
        And Create an account button is clicked
        And title "Mr." checkbox is checked
        And customer first name is filled with "Joe"
        And customer last name is filled with "Biden"
        And Password is filled with "qwerty123"
        And signup for newsletter checkbox is checked
        And recieve offers checkbox is checked
        And first name is filled with "Joe"
        And last name is filled with "Biden"
        And company name is filled with "White House"
        And address is filled with "1600 Pennsylvania Avenue NW"
        And city is filled with "Washington D.C"
        And state is filled with "Washington"
        And the zip code is "20500"
        And the country is "United States"
        And the additional information is filled with "I am the president of the USA"
        And the mobile phone is "+123456789"
        And the address alias is filled with "whitehouse"
        When the register button is clicked
        Then the title "My account - My Store" appear

        