# Created by vera at 5/23/23
Feature: Tests for main page UI

  Scenario: User sees all footer links
    Given Open amazon main page
    Then Verify there are 36 links


  Scenario:
    Given Open amazon main page
    When Click on button from Signin popup
    Then Verify Sign in page opened