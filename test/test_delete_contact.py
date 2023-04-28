from random import randrange

from model.contact import Contact


def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='contact for delete'))

    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)

    assert app.contact.count() == len(old_contacts) - 1

    new_contacts = app.contact.get_contacts_list()
    # remove first element of the original list and compare lists
    old_contacts[index:index+1] = []
    assert new_contacts == old_contacts
