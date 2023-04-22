from model.contact import Contact


def test_edit_first_contact_firstname(app):
    contact = Contact(firstname='firstname1-edit')

    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='contact for edit'))

    old_contacts = app.contact.get_contacts_list()
    contact.id = old_contacts[0].id
    app.contact.edit_first(contact)
    new_contacts = app.contact.get_contacts_list()

    assert len(new_contacts) == len(old_contacts)

    old_contacts[0] = contact

    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)


def test_edit_first_contact_birthday(app):
    contact = Contact(bday='6', bmonth='February', byear='1981')

    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='contact for edit'))

    old_contacts = app.contact.get_contacts_list()
    app.contact.edit_first(contact)
    new_contacts = app.contact.get_contacts_list()

    assert len(new_contacts) == len(old_contacts)
