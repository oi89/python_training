*** Settings ***
Library    AddressBook.py
Library    Collections
Suite Setup    Init Fixtures
Suite Teardown    Destroy Fixtures

*** Test Cases ***
Add New Contact
    ${old_list} =    get contact list
    ${contact} =    new contact    firstname1  lastname1
    create contact    ${contact}
    ${new_list} =    get contact list
    append to list    ${old_list}    ${contact}
    contacts list should be equal    ${new_list}    ${old_list}

Edit Contact
    ${old_list} =    get non empty contact list
    ${contact_to_edit} =    get random contact from list    ${old_list}
    ${new_contact} =    new contact    firstname-edit    lastname-edit
    edit contact    ${contact_to_edit}    ${new_contact}
    ${new_list} =    get contact list
    ${old_list} =    change old contacts list    ${old_list}    ${contact_to_edit}    ${new_contact}
    contacts list should be equal    ${new_list}    ${old_list}

Delete Contact
    ${old_list} =    get non empty contact list
    ${contact} =    get random contact from list    ${old_list}
    delete contact    ${contact}
    ${new_list} =    get contact list
    remove values from list    ${old_list}    ${contact}
    contacts list should be equal    ${new_list}    ${old_list}