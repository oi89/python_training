import random
from pytest_bdd import given, when, then, parsers

from model.contact import Contact


@given("a contacts list", target_fixture="contacts_list")
def get_contacts_list(db):
    return db.get_contacts_list()


@given(parsers.parse("a contact with {firstname} and {lastname}"), target_fixture="new_contact")
def get_new_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when("add the contact")
def add_contact(new_contact, app):
    app.contact.create(new_contact)


@then("new contacts list is equal to old contacts list with added contact")
def check_added_contact(contacts_list, new_contact, db):
    old_contacts = contacts_list
    new_contacts = db.get_contacts_list()
    old_contacts.append(new_contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)


@given("non-empty contact list", target_fixture="non_empty_contacts_list")
def get_non_empty_contacts_list(db, app):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname='contact for delete'))

    return db.get_contacts_list()


@given("random contact from the list", target_fixture="random_contact")
def get_random_contact(non_empty_contacts_list):
    return random.choice(non_empty_contacts_list)


@when("delete the contact")
def delete_contact(random_contact, app):
    app.contact.delete_contact_by_id(random_contact.id)


@then("new contacts list is equal to old contacts list without deleted contact")
def check_deleted_contact(non_empty_contacts_list, random_contact, db):
    old_contacts = non_empty_contacts_list
    new_contacts = db.get_contacts_list()
    old_contacts.remove(random_contact)

    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)


@given(parsers.parse("new contact with {firstname} and {lastname}"), target_fixture="updated_contact")
def get_updated_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when("modify the selected contact with new contact values")
def modify_contact(random_contact, updated_contact, app):
    app.contact.edit_contact_by_id(random_contact.id, updated_contact)


@then("new contacts list is equal to old contacts list with modified contact")
def check_modified_contact(non_empty_contacts_list, random_contact, updated_contact, db):
    old_contacts = non_empty_contacts_list
    new_contacts = db.get_contacts_list()

    # change contact_to_edit to new_contact in old_contacts list for compare
    for contact in old_contacts:
        if contact == random_contact:
            contact.firstname = updated_contact.firstname
            contact.lastname = updated_contact.lastname

    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
