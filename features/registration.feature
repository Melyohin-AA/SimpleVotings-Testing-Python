@registration
Feature: User registration

  @en
  Scenario: User opens registration page
    Given index page is opened
    When I navigate to registration page
    Then I verify registration page is loaded

  @en
  Scenario: User registers successfully
    Given registration page is opened
    When I try register as unique PW1="pass", PW2="pass", name="USER"
    Then I verify registration is succeeded

  @en
  Scenario: User registration is rejected because login is occupied
    Given registration page is opened
    When I try register as login="user1", PW1="pass", PW2="psas", name="USER"
    Then I verify registration is rejected

  @en
  Scenario: User registration is rejected because entered passwords are different
    Given registration page is opened
    When I try register as unique PW1="pass", PW2="psas", name="USER"
    Then I verify registration is rejected

  @en
  Scenario: User cannot register with empty login
    Given registration page is opened
    When I try register as login="", PW1="pass", PW2="psas", name="USER"
    Then I verify registration is rejected

  @en
  Scenario: User cannot register with empty password
    Given registration page is opened
    When I try register as unique PW1="", PW2="", name="USER"
    Then I verify registration is rejected

  @en
  Scenario: User cannot register with empty name
    Given registration page is opened
    When I try register as unique PW1="pass", PW2="pass", name=""
    Then I verify registration is rejected
