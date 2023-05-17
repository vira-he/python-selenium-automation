# Created by vera at 5/16/23
Feature: Amazon cart tests

  Scenario: User can access cart
    Given Open amazon main page
    When Open cart
    Then Verify cart is empty

  Scenario: User can add product to cart
    Given Open amazon main page
    When Search for stickers
    When Add product to cart
    Then Verify the product is added to cart