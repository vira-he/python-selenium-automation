# Created by vera at 5/16/23
Feature: Amazon Sign in page

  Scenario: Unregistered user is transferred to Sign in page
    Given Open amazon main page
    When Click Orders
    Then Verify Sign in page opened



  Scenario: Signin page can be opened from Signin popup
    Given Open amazon main page
    When Click on button from Signin popup
    Then Verify Sign in page opened
