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


  Scenario: Amazon user sees sign in button
    Given Open amazon main page
    When Verify sign in is clickable
    Then Verify sign in disappears