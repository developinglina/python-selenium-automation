Feature: Cart functionality

  Scenario: Display message when cart is empty
    Given Target homepage is opened
    When the user clicks on the cart icon at the top of the page
    Then the user should see a message that says "Your cart is empty"
