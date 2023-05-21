import random

from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, db):
    contacts_db = db.get_contacts_list()
    groups_db = db.get_groups_list()
    contact = None
    group = None

    if len(groups_db) == 0:
        app.group.create(Group(name='group for add contacts'))
        groups_db = db.get_groups_list()

    contacts_not_used = []
    for gr in groups_db:
        contacts_in_group = db.orm.get_contacts_in_group(group=gr)
        contacts_not_used = list(filter(lambda c: c not in contacts_in_group, contacts_db))
        if len(contacts_not_used) > 0:
            contact = random.choice(contacts_not_used)
            group = gr
            break

    if len(contacts_db) == 0 or len(contacts_not_used) == 0:
        app.contact.create(Contact(firstname='contact for group'))
        group = random.choice(groups_db)
        contact = random.choice(db.orm.get_contacts_not_in_group(group=group))

    app.contact.add_contact_to_group(contact, group)
    app.contact.click_logo_link()

    contacts_in_group_new = db.orm.get_contacts_in_group(group=group)

    assert contact in contacts_in_group_new
