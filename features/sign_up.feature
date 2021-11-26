Feature: AutomationPractice sign up test

    Background:
        Given the home page is opened
        And the Sign in link is clicked

    # Scenario: Create account successfully
    #     Given the email is a random email
    #     And Create an account button is clicked
    #     And title "Mr." checkbox is checked
    #     And customer first name is filled with "Joe"
    #     And customer last name is filled with "Biden"
    #     And Password is filled with "qwerty123"
    #     And signup for newsletter checkbox is checked
    #     And recieve offers checkbox is checked
    #     And first name is filled with "Joe"
    #     And last name is filled with "Biden"
    #     And company name is filled with "White House"
    #     And address is filled with "1600 Pennsylvania Avenue NW"
    #     And city is filled with "Washington D.C"
    #     And state is filled with "Washington"
    #     And the zip code is "20500"
    #     And the country is "United States"
    #     And the additional information is filled with "I am the president of the USA"
    #     And the mobile phone is "+123456789"
    #     And the address alias is filled with "whitehouse"
    #     When the register button is clicked
    #     Then the title "My account - My Store" appear

        Scenario: Using registered email
            Given the sign up email is "abc@mail.com"
            When Create an account button is clicked
            Then a using registered email error message appear

        # Scenario Outline: Fail to create account
        #     Given the email is a random email
        #     And Create an account button is clicked
        #     And title "<title>" checkbox is checked
        #     And customer first name is filled with "<firstname>"
        #     And customer last name is filled with "<lastname>"
        #     And Password is filled with "<password>"
        #     And signup for newsletter checkbox is checked
        #     And recieve offers checkbox is checked
        #     And first name is filled with "<firstname>"
        #     And last name is filled with "<lastname>"
        #     And company name is filled with "<company>"
        #     And address is filled with "<address>"
        #     And city is filled with "<city>"
        #     And state is filled with "<state>"
        #     And the zip code is "<zipcode>"
        #     And the country is "<country>"
        #     And the additional information is filled with "<additionalInfo>"
        #     And the mobile phone is "<phone>"
        #     And the address alias is filled with "<alias>"
        #     When the register button is clicked
        #     Then the registered fail "<failMsg>" message appear

        #     Examples:
        #         | title  | firstname  | lastname| password | company | address       | city      | state  | zipcode | country       | additionalInfo | phone      | alias      | failMsg                                      |
        #         | Mrs.   |            | Clinton | abc123   | UniDeb  | Egyetem ter 1 |  Debrecen | Nevada | 12345   | United States |                | +987654321 | whitehouse | <b>firstname</b> is required.                |
        #         |        | Hillary    | Clinton |          | UniDeb  | Egyetem ter 1 |  Debrecen | Nevada | 12345   | United States |  abc           | +987654321 | whitehouse | <b>passwd</b> is required.                   |
        #         |        | Hillary    | Clinton | abc123   | UniDeb  | Egyetem ter 1 |  Debrecen | Nevada | 12345   | United States |  abc           |            | whitehouse | You must register at least one phone number. |