from model.contact import Contact


def test_edit_first_contact(app):
    contact = Contact(
        firstname='firstname1-edit',
        middlename='middlename1-edit',
        lastname='lastname1-edit',
        nickname='nickname1-edit',
        title='title1-edit',
        company='company1-edit',
        address='address1-edit',
        home='0011',
        mobile='0021',
        work='0031',
        fax='0041',
        email='a1@a.ru',
        email2='b1@b.net',
        email3='c1@c.com',
        homepage='a1.ru',
        bday='6',
        bmonth='February',
        byear='1981',
        aday='3',
        amonth='march',
        ayear='2001',
        address2='address2-edit',
        phone2='phone2-edit',
        notes='notes1-edit'
    )
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(contact)
    app.session.logout()
