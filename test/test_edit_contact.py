import random

from model.contact import Contact


def test_edit_random_contact_firstname(app, db, check_ui):
    new_contact = Contact(firstname='firstname1-edit')

    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname='contact for edit'))

    old_contacts = db.get_contacts_list()
    contact_to_edit = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact_to_edit.id, new_contact)

    assert app.contact.count() == len(old_contacts)

    # change contact_to_edit to new_contact in old_contacts list for compare
    for contact in old_contacts:
        if contact == contact_to_edit:
            contact.firstname = new_contact.firstname

    new_contacts = db.get_contacts_list()

    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)

    if check_ui:
        sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)


def test_edit_random_contact_lastname(app, db, check_ui):
    new_contact = Contact(lastname='lastname1-edit')

    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(lastname='contact for edit'))

    old_contacts = db.get_contacts_list()
    contact_to_edit = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact_to_edit.id, new_contact)

    assert app.contact.count() == len(old_contacts)

    # change contact_to_edit to new_contact in old_contacts list for compare
    for contact in old_contacts:
        if contact == contact_to_edit:
            contact.lastname = new_contact.lastname

    new_contacts = db.get_contacts_list()

    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)

    if check_ui:
        sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
