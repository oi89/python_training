# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    # connect letters, numbers and space
    # to get more spaces in result string, multiply " " to 10 times
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numbers(maxlen):
    return ''.join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

test_data = [
    Contact(
        firstname=random_string('', 7),
        middlename=random_string('', 7),
        lastname=random_string('', 10),
        nickname=random_string('', 7),
        title=random_string('title', 7),
        company=random_string('company', 10),
        address=random_string('address', 15),
        home=random_numbers(7),
        mobile=random_numbers(10),
        work=random_numbers(10),
        fax=random_numbers(10),
        email=random_string('email', 5),
        email2=random_string('email2', 5),
        email3=random_string('email2', 5),
        homepage=random_string('', 10),
        bday=random.randrange(32),
        bmonth=months[random.randrange(12)],
        byear=random_numbers(5),
        aday=random.randrange(32),
        amonth=months[random.randrange(12)],
        ayear=random_numbers(5),
        address2=random_string('address2', 15),
        phone2=random_numbers(10),
        notes=random_string('notes', 20)
    )
    for i in range(2)
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)

    assert app.contact.count() == len(old_contacts) + 1

    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)

    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
