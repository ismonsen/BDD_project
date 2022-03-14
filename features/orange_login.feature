Feature: OrangeHRM Login
  Scenario: Login to OrangeHRM with valid parameters
    Given I launch Chrome
    When Enter orangehrm homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then Verify dashboard loaded