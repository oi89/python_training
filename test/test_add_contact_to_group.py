import random
import allure

from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, db):
    contact = None
    group = None

    with allure.step("Given a contacts list"):
        contacts_db = db.get_contacts_list()

    with allure.step("Given non-empty groups list"):
        groups_db = db.get_groups_list()
        if len(groups_db) == 0:
            app.group.create(Group(name='group for add contacts'))
            groups_db = db.get_groups_list()

    with allure.step("Given a contact which is not used in groups"):
        contacts_not_used = []
        db.delete_outdated_contacts_in_group()
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

    with allure.step(f"When add the contact {contact} to group {group}"):
        app.contact.add_contact_to_group(contact, group)
        app.contact.click_logo_link()

    with allure.step("Then contact is in group"):
        contacts_in_group_new = db.orm.get_contacts_in_group(group=group)

        assert contact in contacts_in_group_new
