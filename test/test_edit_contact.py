import random
import allure

from model.contact import Contact


def test_edit_random_contact_firstname(app, db, check_ui):
    new_contact = Contact(firstname='firstname1-edit')

    with allure.step("Given non-empty contact list"):
        if len(db.get_contacts_list()) == 0:
            app.contact.create(Contact(firstname='contact for edit'))

        old_contacts = db.get_contacts_list()

    with allure.step("Given random contact from the list"):
        contact_to_edit = random.choice(old_contacts)

    with allure.step(f"When modify the selected contact {contact_to_edit} with new contact values {new_contact}"):
        app.contact.edit_contact_by_id(contact_to_edit.id, new_contact)

    with allure.step("Then new contacts list is equal to old contacts list with modified contact"):
        assert app.contact.count() == len(old_contacts)

        # change contact_to_edit to new_contact in old_contacts list for compare
        index = old_contacts.index(contact_to_edit)
        old_contacts[index].firstname = new_contact.firstname

        new_contacts = db.get_contacts_list()

        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)

        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == \
                   sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)


def test_edit_random_contact_lastname(app, db, check_ui):
    new_contact = Contact(lastname='lastname1-edit')

    with allure.step("Given non-empty contact list"):
        if len(db.get_contacts_list()) == 0:
            app.contact.create(Contact(lastname='contact for edit'))

        old_contacts = db.get_contacts_list()

    with allure.step("Given random contact from the list"):
        contact_to_edit = random.choice(old_contacts)

    with allure.step(f"When modify the selected contact {contact_to_edit} with new contact values {new_contact}"):
        app.contact.edit_contact_by_id(contact_to_edit.id, new_contact)

    with allure.step("Then new contacts list is equal to old contacts list with modified contact"):
        assert app.contact.count() == len(old_contacts)

        # change contact_to_edit to new_contact in old_contacts list for compare
        index = old_contacts.index(contact_to_edit)
        old_contacts[index].lastname = new_contact.lastname

        new_contacts = db.get_contacts_list()

        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)

        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == \
                   sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
