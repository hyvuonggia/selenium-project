Feature: AutomationPractice Contact us Page Test

    Background:
        Given the home page is opened
        And the Contact us button is clicked

    Scenario: Successfully contact with AutomationPractice
        Given the subject heading is "Customer service"
        And the email address is filled with "abc@mail.com"
        And order reference is filled with "abc123456"
        And the attach file is "\\image.png" 
        And the message is filled with "This is a message"
        When the send button is clicked
        Then a "Your message has been successfully sent to our team." message is shown

    # Scenario Outline: Successfully contact with AutomationPractice
    #     Given the subject heading is "<subject>"
    #     And the email address is filled with "<email>"
    #     And order reference is filled with "<order>"
    #     And the attach file is "<attachment>"
    #     And the message is filled with "<message>"
    #     When the send button is clicked
    #     Then a "<msg>" message is shown

    #     Examples:
    #         | subject   | email        | order | attachment | message | msg                                                   |
    #         | Webmaster | qwe@mail.com | qwe   | \img.jpg   | Hello   | Your message has been successfullly sent to our team. |
    #         | Webmaster | qwe@mail.com |       | \img.jpg   | Hello   | Your message has been successfullly sent to our team. |
    #         | Webmaster | qwe@mail.com |       |            | Hello   | Your message has been successfullly sent to our team. |

    # Scenario Outline: Fail to contact with AutomationPractice
    #     Given the subject heading is "<subject>"
    #     And the email address is filled with "<email>"
    #     And order reference is filled with "<order>"
    #     And the attach file is "<attachment>"
    #     And the message is filled with "<message>"
    #     When the send button is clicked
    #     Then a "<msg>" message is shown
    #     Example:
    #         | subject   | email        | order | attachment | message | msg                                             |
    #         |           | qwe@mail.com | qwe   | \img.jpg   | Hello   | Please select a subject from the list provided. |
    #         | Webmaster |              |       | \img.jpg   | Hello   | Invalid email address.                          |
    #         | Webmaster | qwe@mail.com |       |            |         | The message cannot be blank.                    |
