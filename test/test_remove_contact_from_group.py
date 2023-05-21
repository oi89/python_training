import random

from model.contact import Contact
from model.group import Group


def test_remove_contact_from_group(app, db):
    contacts_db = db.get_contacts_list()
    groups_db = db.get_groups_list()
    contact = None
    group = None

    if len(contacts_db) == 0:
        app.contact.create(Contact(firstname='contact for group'))
        contacts_db = db.get_contacts_list()

    if len(groups_db) == 0:
        app.group.create(Group(name='group for add contacts'))
        groups_db = db.get_groups_list()

    # try to find group with contacts
    for gr in groups_db:
        if len(db.orm.get_contacts_in_group(gr)) > 0:
            group = gr
            break

    if group is None:
        group = random.choice(groups_db)
        contact = random.choice(contacts_db)
        app.contact.add_contact_to_group(contact, group)
    else:
        contact = random.choice(db.orm.get_contacts_in_group(group))

    app.contact.remove_contact_from_group(contact, group)
    app.contact.click_logo_link()

    contacts_in_group_new = db.orm.get_contacts_in_group(group=group)

    assert contact not in contacts_in_group_new
