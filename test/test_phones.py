import re
from random import randrange


def test_phones_on_home_page(app):
    contacts_on_home_page = app.contact.get_contacts_list()
    index = randrange(len(contacts_on_home_page))
    contact_from_home_page = contacts_on_home_page[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(str):
    # remove symbols: "(", ")", " ", "-" from phones on edit page
    return re.sub("[() -]", "", str)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda phone: phone != '',  # remove empty elements if phone is not set
                            map(lambda phone: clear(phone),  # remove extra symbols from the phone
                                filter(lambda phone: phone is not None,  # clear method won't work for None elements
                                       [contact.home, contact.mobile, contact.work, contact.phone2]
                                       )
                                )
                            )
                     )


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda email: email != '', [contact.email, contact.email2, contact.email3]))
