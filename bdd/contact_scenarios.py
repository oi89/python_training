from pytest_bdd import scenario

from .contact_steps import *


@scenario("contacts.feature", "Add new contact")
def test_add_new_contact():
    pass


@scenario("contacts.feature", "Delete random contact")
def test_delete_random_contact():
    pass


@scenario("contacts.feature", "Edit random contact")
def test_edit_random_contact():
    pass
