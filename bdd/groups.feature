Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header>, <footer>
  When add the group
  Then new groups list is equal to old groups list with added group

  Examples:
  | name  | header  | footer  |
  | name1 | header1 | footer1 |
  | name2 | header2 | footer2 |


 Scenario: Delete random group
  Given non-empty group list
  Given random group from the list
  When delete the group
  Then new groups list is equal to old groups list without deleted group