Feature: AutomationPractice search test

    Background:
        Given the home page is opened

    Scenario: 
        Given the search bar is filled with "shirt"
        When the search button is clicked
        Then the page with searched item "shirt" appear

    Scenario Outline: 
        Given the search bar is filled with "<item>"
        When the search button is clicked
        Then a "<msg>" search message is displayed

        Examples:
            | item | msg                                        |
            | abc  | No results were found for your search "abc"|
            |      | Please enter a search keyword              |

    