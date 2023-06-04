# Created by vera at 6/3/23
Feature: Tests for 404 feature

  Scenario: User is able to navigate to amazon blog
    Given Open amazon product B07B113JKRR2511111 page
    And Store original window
    When Click on dog image
    And Switch to new window
    Then Verify blog is opened
    And Close blog
    And Return to original window