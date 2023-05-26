# Created by shelb at 5/26/2023
Feature: Validate that register
  # Enter feature description here

  @smoke
  Scenario: Make a new user
    Given I go to our app
    When I click on register
    And I fill out the Register Form
    And I submit the Register Form
    Then I validate the account is created