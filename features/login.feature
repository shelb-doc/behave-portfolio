# Created by shelb at 5/23/2023
Feature: Validate login

  @smoke
  Scenario: Validate site is up.
    Given I go to our app
    And I fill out the login Form
    And I submit the login Form
    Then I validate the Login is successful