# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact
from fixture.application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    contact = Contact(
        firstname='firstname1',
        middlename='middlename1',
        lastname='lastname1',
        nickname='nickname1',
        title='title1',
        company='company1',
        address='address1',
        home='001',
        mobile='002',
        work='003',
        fax='004',
        email='a@a.ru',
        email2='b@b.net',
        email3='c@c.com',
        homepage='a.ru',
        bday='5',
        bmonth='January',
        byear='1980',
        aday='2',
        amonth='February',
        ayear='2000',
        address2='address2',
        phone2='phone2',
        notes='notes1'
    )
    app.login(username="admin", password="secret")
    app.add_new_contact(contact)
    app.logout()
