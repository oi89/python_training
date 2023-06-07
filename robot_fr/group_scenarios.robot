*** Settings ***
Library    AddressBook.py
Library    Collections
Suite Setup    Init Fixtures
Suite Teardown    Destroy Fixtures

*** Test Cases ***
Add New Group
    ${old_list} =    Get Group List
    ${group} =    New Group    name1  header1  footer1
    Create Group  ${group}
    ${new_list} =    Get Group List
    Append To List    ${old_list}    ${group}
    Groups List Should Be Equal    ${new_list}    ${old_list}

Delete Group
    ${old_list} =    Get Group List
    ${len} =    get length    ${old_list}
    ${index} =    evaluate    random.randrange(${len})    modules=random
    ${group} =    Get From List  ${old_list}    ${index}
    Delete Group  ${group}
    ${new_list} =    Get Group List
    remove values from list    ${old_list}    ${group}
    Groups List Should Be Equal    ${new_list}    ${old_list}