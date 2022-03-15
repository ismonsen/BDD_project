Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch Chrome
    When Enter orangehrm homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then Verify dashboard loaded

  Scenario Outline: Login to OrangeHRM with valid parameters
    Given I launch Chrome
    When Enter orangehrm homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then Verify dashboard loaded
    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |
