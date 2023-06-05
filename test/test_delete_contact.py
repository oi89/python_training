import random
import allure

from model.contact import Contact


def test_delete_random_contact(app, db, check_ui):
    with allure.step("Given non-empty contact list"):
        if len(db.get_contacts_list()) == 0:
            app.contact.create(Contact(firstname='contact for delete'))

        old_contacts = db.get_contacts_list()

    with allure.step("Given random contact from the list"):
        contact = random.choice(old_contacts)

    with allure.step(f"When delete the contact {contact}"):
        app.contact.delete_contact_by_id(contact.id)

    with allure.step("Then new contacts list is equal to old contacts list without deleted contact"):
        assert app.contact.count() == len(old_contacts) - 1

        new_contacts = db.get_contacts_list()
        # remove element of the original list and compare lists
        old_contacts.remove(contact)
        assert new_contacts == old_contacts

        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == \
                   sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
