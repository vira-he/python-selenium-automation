# Created by vera at 5/6/23
Feature: Amazon search tests

  Scenario: User can search on Amazon
    Given Open amazon main page
    When Search for table
    Then Verify search results for "table"
