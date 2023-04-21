from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='contact for delete'))

    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contacts_list()

    assert len(new_contacts) == len(old_contacts) - 1

    # удаляем первый элемент изначального списка и сравниваем списки
    old_contacts[0:1] = []
    assert new_contacts == old_contacts
