import json
import os.path
import random

from fixture.application import Application
from fixture.db import DbFixture
from model.group import Group
from model.contact import Contact


class AddressBook:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, browser="chrome", config="target.json"):
        self.browser = browser
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(file) as config_file:
            self.target = json.load(config_file)

    def init_fixtures(self):
        web_config = self.target["web"]
        self.fixture = Application(browser=self.browser, base_url=web_config['baseUrl'])
        self.fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])

        db_config = self.target["db"]
        self.db_fixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"],
                                    password=db_config["password"])

    def destroy_fixtures(self):
        self.fixture.destroy()
        self.db_fixture.destroy()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def get_group_list(self):
        return self.db_fixture.get_groups_list()

    def create_group(self, group):
        self.fixture.group.create(group)

    def groups_list_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def get_non_empty_group_list(self):
        groups = self.get_group_list()
        if len(groups) == 0:
            group = self.new_group(name="new group")
            self.create_group(group)
            return self.get_group_list()
        else:
            return groups

    def get_contact_list(self):
        return self.db_fixture.get_contacts_list()

    def new_contact(self, firstname, lastname):
        return Contact(firstname=firstname, lastname=lastname)

    def create_contact(self, contact):
        self.fixture.contact.create(contact)

    def contacts_list_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Contact.id_or_max) == sorted(list2, key=Contact.id_or_max)

    def get_non_empty_contact_list(self):
        contacts = self.get_contact_list()
        if len(contacts) == 0:
            contact = self.new_contact(firstname="new contact")
            self.create_contact(contact)
            return self.get_contact_list()
        else:
            return contacts

    def get_random_contact_from_list(self, contacts):
        return random.choice(contacts)

    def edit_contact(self, contact_to_edit, new_contact):
        self.fixture.contact.edit_contact_by_id(contact_to_edit.id, new_contact)

    def change_old_contacts_list(self, old_contacts, contact_to_edit, new_contact):
        index = old_contacts.index(contact_to_edit)
        old_contacts[index].firstname = new_contact.firstname
        old_contacts[index].lastname = new_contact.lastname
        return old_contacts

    def delete_contact(self, contact):
        self.fixture.contact.delete_contact_by_id(contact.id)
