Feature: Tests for Settings Page Functionality

  Scenario: User can find the 12 options in settings page
    Given Open the signin page
    And Log in to the page
    And Click on settings option
    Then Verify the right page opens
    And Verify there are 12 options for the settings
    And Verify “connect the company” button is available