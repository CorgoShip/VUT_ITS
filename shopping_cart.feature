Feature: Shopping Cart test

   This Feature will test functionality of Shopping Cart

   Scenario Outline: Add to cart
   Given User is viewing a <product>
   When User Clicks on Add to Cart
   Then Cart contains <product>

   Examples:
   | product |
   | MacBook |
   | MacBook Air |
   | Sony VAIO |

   Scenario: Remove from cart
   Given Cart contains at least one product
   And User is viewing cart
   When User clicks on Remove button on a product
   Then Cart is empty

   Scenario: Change quantity of product in cart
   Given Cart contains at least one product
   And User is viewing cart
   When User changes Quantity of product to another number
   Then Quantity of product is the new number

