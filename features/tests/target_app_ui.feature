Feature: Target app

Scenario: User can open and close Terms and Conditions from sign in page
        Given Open sign in page
        And Store original window
        When Click on Target terms and conditions link
        And Switch to the newly opened window
       Then Verify Terms and Conditions page is opened
        Then Close current page
        Then Return to original window


