Feature: Login Functionality

Scenario: Logged out user can navigate to the Sign In form
    Given Target homepage is opened
    When the user clicks the "Sign in" button
    When "sign in" from the right-side navigation menu is clicked
    Then Sign In form is opened
