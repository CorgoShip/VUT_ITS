Feature: User account test

   This Feature aims to test operations concerning user's account

   Scenario: Register user
   Given User is at registration page
   When User fills all required fields
   Then User is registered

   Scenario: Log in
   Given User is not logged in
   When User fills credentials
   Then User is logged in

   Scenario: Log out
   Given User is logged in1
   When User clicks My Account -> Logout
   Then User is logged out
