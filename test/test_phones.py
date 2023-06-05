import re
import allure

from model.contact import Contact


def test_contacts_on_home_page(app, db):
    with allure.step("Given a contacts list from home page"):
        contacts_on_home_page = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)

    def clear_spaces(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                       address=contact.address,
                       email=contact.email.strip(), email2=contact.email2.strip(), email3=contact.email3.strip(),
                       mobile=contact.mobile, work=contact.work, home=contact.home, phone2=contact.phone2)

    with allure.step("Given a contacts list from database"):
        contacts_from_db = list(map(clear_spaces, db.get_contacts_list()))
        contacts_from_db = sorted(contacts_from_db, key=Contact.id_or_max)

    with allure.step("Then contacts from web page and from database are equal"):
        for i in range(0, len(contacts_on_home_page)):
            assert contacts_on_home_page[i].firstname == contacts_from_db[i].firstname
            assert contacts_on_home_page[i].lastname == contacts_from_db[i].lastname
            assert contacts_on_home_page[i].address == contacts_from_db[i].address
            assert contacts_on_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[i])
            assert contacts_on_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[i])


def test_phones_on_view_page(app, db):
    contact = Contact(firstname='contact with phones', home="001", mobile="002", work="003", phone2="004")

    with allure.step(f"Given a contact with phone numbers {contact}"):
        app.contact.create(contact)
        index = app.contact.get_contacts_list().index(contact)

    with allure.step("Given a contacts list from view page"):
        contact_from_view_page = app.contact.get_contact_from_view_page(index)

    with allure.step("Given a contacts list from edit page"):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    with allure.step("Then contacts from view page and from edit page are equal"):
        assert contact_from_view_page.home == contact_from_edit_page.home
        assert contact_from_view_page.mobile == contact_from_edit_page.mobile
        assert contact_from_view_page.work == contact_from_edit_page.work
        assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(str):
    # change "00" to "+"
    if str.startswith("00"):
        str = str.replace("00", "+", 1)
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
