Feature: Test for support and news functionality

 Scenario: User can access Whatsapp and Telegram communities
    Given Open the signin page
    And Log in to the page
    And Click on Main menu
    And Click on User profile
#    And Click on settings option
    And Store Original window
    When Click on support option
    And Switch to the new tab
    Then Verify whatsapp support page opened
    And Close and Go back to original window
    Then Click on news option
    And Verify telegram news page opened
