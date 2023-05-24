# Created by vera at 5/23/23
Feature: Customer service page UI tests

  Scenario: Verify the user can see UI elements on Customer service page
    Given Open Customer service page
    Then Search for Header text
    Then Search for Options menu
    Then Search for Search field
    Then Search for All help topics