from model.contact import Contact


def test_edit_first_contact_firstname(app):
    contact = Contact(firstname='firstname1-edit')
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='contact for edit'))

    app.contact.edit_first(contact)


def test_edit_first_contact_birthday(app):
    contact = Contact(bday='6', bmonth='February', byear='1981')
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='contact for edit'))

    app.contact.edit_first(contact)
