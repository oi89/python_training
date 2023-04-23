from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='contact for delete'))

    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first()

    assert app.contact.count() == len(old_contacts) - 1

    new_contacts = app.contact.get_contacts_list()
    # удаляем первый элемент изначального списка и сравниваем списки
    old_contacts[0:1] = []
    assert new_contacts == old_contacts
