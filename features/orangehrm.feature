Feature: OrangeHRM Logo
  Scenario: Logo presence on OrangeHRM home page
    Given launch Chrome
    When open orangehrm homepage
    Then verify that logo presents on page
    And close browser