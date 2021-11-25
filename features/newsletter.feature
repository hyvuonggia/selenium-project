Feature: AutomationPractice newsletter test

    Background:
        Given the home page is opened

    Scenario: Successfully register for newsletter
        Given the newsletter email is filled with random email address
        When the submit button is clicked
        Then a newsletter "Newsletter : You have successfully subscribed to this newsletter." message appear

    Scenario Outline: Fail to register for newsletter
        Given the newsletter email is filled with "<email>"
        When the submit button is clicked
        Then a newsletter "<msg>" message appear
        Examples:
            | email        | msg                                                    |
            | abc@mail.com | Newsletter : This email address is already registered. |
            |              | Newsletter : Invalid email address.                    |
            | abc          | Newsletter : Invalid email address.                    |