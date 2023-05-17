from model.contact import Contact


# parameter json_contacts means that we will get test data from file data.contacts.json
def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts

    old_contacts = db.get_contacts_list()
    app.contact.create(contact)

    new_contacts = db.get_contacts_list()
    old_contacts.append(contact)

    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
