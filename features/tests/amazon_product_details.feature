# Created by vera at 5/27/23
Feature: Product page with multiple elements

  Scenario: User can select colors
    Given Open amazon product B07BJKRR25 page
    Then Verify user can click through colors


  Scenario: User can see New Arrivals deals
    Given Open amazon product B074TBCSC8 page
    When Hover over New Arrivals
    Then Verify user can click through colors