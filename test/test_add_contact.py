# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact
from data.add_contact import constants as test_data


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)

    assert app.contact.count() == len(old_contacts) + 1

    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)

    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
