Feature: Wish List test

   This Feature will test function of Wish List

   Scenario: Add to Wish List
   Given User is logged in
   And customer is viewing a product
   When User clicks Add product to Wish List
   Then Wish List contains the product

   Scenario: Remove from Wish List
   Given User is logged in
   And Wish List contains at least one product
   And Is at Wish List website
   When User cliks on Remove button on a product
   Then Wish List is empty

