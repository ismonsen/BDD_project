Feature: OrangeHRM Basic

  Background: common steps
    Given I launch browser
    When I open application
    And Enter valid username and password
    And Click on login

  Scenario: Login to OrangeHRM
    Then User dashboard is displayed

  Scenario: Search user
    When navigate to search page
    Then search page should be display

  Scenario: Advanced search user
    When navigate to advanced search page
    Then advanced search page should be display