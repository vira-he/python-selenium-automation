# Created by vera at 5/23/23
Feature: Amazon find elements

  Scenario: Verify the user sees 5 links on the best sellers page
    Given Open amazon main page
    When Click Best Sellers
    Then Verify links displayed
