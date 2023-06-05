import allure

from model.contact import Contact


# parameter json_contacts means that we will get test data from file data.contacts.json
def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts

    with allure.step("Given a contacts list"):
        old_contacts = db.get_contacts_list()

    with allure.step(f"When add the contact {contact}"):
        app.contact.create(contact)

    with allure.step("Then new contacts list is equal to old contacts list with added contact"):
        new_contacts = db.get_contacts_list()
        old_contacts.append(contact)

        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)

        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
