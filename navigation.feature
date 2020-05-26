Feature: Navigation test

   This Feature aims to test website navigation and stuff concernig webstite appearence

   Scenario Outline: Search
   Given User is at eshop website
   When User writes <product> to Search bar
   And Clicks search
   Then Webpage with result for <product> is displayed

   Examples:
   | product |
   | MacBook |
   | MacBook Air |
   | Sony VAIO |

   Scenario Outline: Change currency
   Given User is at eshop website
   When Currency is set to <different>
   Then All prices are in <different>

   Examples:
   | different |
   | EUR |
   | GBP |
   | USD |

   Scenario Outline: Product sort
   Given Users is viewing <category>
   When Users clicks set Sort by to <sort>
   Then <category> is sorted by <sort>

   Examples:
   | category | sort |
   | Monitors | Name (A - Z) |
   | Cameras  | Name (Z - A) |

   Scenario Outline: Nav bar
   Given User is at eshop website
   When User chooses <category>
   Then <category> is shown

   Examples:
   | category |
   | Monitors |
   | Cameras  |
   | Tablets  |
