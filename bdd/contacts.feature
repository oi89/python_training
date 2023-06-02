Scenario Outline: Add new contact
  Given a contacts list
  Given a contact with <firstname> and <lastname>
  When add the contact
  Then new contacts list is equal to old contacts list with added contact

  Examples:
  | firstname  | lastname  |
  | Tom | White |


Scenario: Delete random contact
  Given non-empty contact list
  Given random contact from the list
  When delete the contact
  Then new contacts list is equal to old contacts list without deleted contact


Scenario Outline: Edit random contact
  Given non-empty contact list
  Given random contact from the list
  Given new contact with <firstname> and <lastname>
  When modify the selected contact with new contact values
  Then new contacts list is equal to old contacts list with modified contact

  Examples:
  | firstname  | lastname  |
  | John | Black |