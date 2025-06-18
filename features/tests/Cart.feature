Feature: Cart functionality

    Scenario Outline: User can search for product
      Given Target homepage is opened
      When the user searches for <product_name>
      Then Verify correct search result display for <expected_result>

      Examples:
      | product_name | expected_result|
      | tea          | tea


      Scenario Outline: User can add an item to cart
        Given Target homepage is opened
        When the user searches for <product_name>
        When the user clicks add to cart
     #   Then verify cart

        Examples:
      | product_name | expected_result|
      | tea          | tea



  Scenario: Display message when cart is empty
    Given Target homepage is opened
    When the user clicks on the cart icon at the top of the page
    Then the user should see a message that says "Your cart is empty"







