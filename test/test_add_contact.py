from model.contact import Contact


# parameter json_contacts means that we will get test data from file data.contacts.json
def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)

    assert app.contact.count() == len(old_contacts) + 1

    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)

    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
