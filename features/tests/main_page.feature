Feature: Tests for Main Page Functionality

  Scenario: User can open the Secondary deals page and go through the pagination
    Given Open the signin page
    And Log in to the page
    And Click on Secondary option at the left side menu
    Then Verify the Secondary page opens
    And Go to the final page using the pagination button
    And Go back to the first page using the pagination button

