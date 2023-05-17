import random

from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, db):
    contacts_db = db.get_contacts_list()
    groups_db = db.get_groups_list()

    if len(contacts_db) == 0:
        app.contact.create(Contact(firstname='contact for group'))
        contacts_db = db.get_contacts_list()

    if len(groups_db) == 0:
        app.group.create(Group(name='group for add contacts'))
        groups_db = db.get_groups_list()

    contact = random.choice(contacts_db)
    group = random.choice(groups_db)

    app.contact.add_contact_to_group(contact, group)

    contacts_in_group = app.contact.get_contacts_list()
    app.contact.click_logo_link()

    assert (contact in contacts_in_group)
