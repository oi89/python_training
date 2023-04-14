from model.contact import Contact


def test_edit_first_contact_firstname(app):
    contact = Contact(firstname='firstname1-edit')
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(contact)
    app.session.logout()


def test_edit_first_contact_birthday(app):
    contact = Contact(bday='6', bmonth='February', byear='1981')
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(contact)
    app.session.logout()
