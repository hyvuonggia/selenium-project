Feature: AutomationPractice Sign in Test

    Background:
        Given the home page is opened
        And the Sign in link is clicked

    Scenario: Sign in successfully
        Given the email is "hyvuo@mail.com"
        And the password is "qwerty123"
        When the Sign in button is clicked
        Then the title "My account - My Store" appear

    Scenario Outline: Sign in failed
        Given the email is "<email>"
        And the password is "<password>"
        When the Sign in button is clicked
        Then a "<msg>" message appear

        Examples:
            | email       | password | msg                        |
            |             | abc      | An email address required. |
            |             |          | An email address required. |
            | abc@qwe.com |          | Password is required.      |
            | abc@qwe.com | abc      | Invalid password.          |