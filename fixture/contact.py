import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from model.contact import Contact


class ContactHelper:
    contacts_cache = None

    def __init__(self, app):
        self.app = app

    def click_home_menu(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements(By.NAME, "searchstring")) > 0):
            wd.find_element(By.LINK_TEXT, "home").click()

    def click_add_new_menu(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def change_field_value(self, element_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, element_name).click()
            wd.find_element(By.NAME, element_name).clear()
            wd.find_element(By.NAME, element_name).send_keys(text)

    def select_field_value(self, element_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element(By.NAME, element_name).click()
            wd.find_element(By.XPATH, f"//select[@name='{element_name}']/option[@value='{value}']").click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.select_field_value("bday", contact.bday)
        self.select_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.select_field_value("aday", contact.aday)
        self.select_field_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd

        self.click_add_new_menu()
        self.fill_contact_form(contact)
        # submit
        wd.find_element(By.XPATH, "//input[@name='submit'][2]").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd

        self.click_home_menu()
        self.select_contact_by_index(index)
        # press delete button
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # press OK in alert window
        time.sleep(1)
        wd.switch_to.alert.accept()
        time.sleep(1)
        self.click_home_menu()

        self.contacts_cache = None

    def delete_contact_by_id(self, contact_id):
        wd = self.app.wd

        self.click_home_menu()
        self.select_contact_by_id(contact_id)
        # press delete button
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # press OK in alert window
        time.sleep(1)
        wd.switch_to.alert.accept()
        time.sleep(1)
        self.click_home_menu()

        self.contacts_cache = None

    def delete_first(self):
        self.delete_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.click_home_menu()
        self.select_contact_by_index(index)
        self.click_edit_button_by_index(index)
        self.fill_contact_form(contact)
        # press update button
        wd.find_element(By.XPATH, "//input[@value='Update']").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def edit_contact_by_id(self, contact_id, contact):
        wd = self.app.wd
        self.click_home_menu()
        self.select_contact_by_id(contact_id)
        self.click_edit_button_by_id(contact_id)
        self.fill_contact_form(contact)
        # press update button
        wd.find_element(By.XPATH, "//input[@value='Update']").click()
        self.return_to_home_page()
        self.contacts_cache = None

    def edit_first(self, contact):
        self.edit_contact_by_index(0, contact)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        # select contact's checkbox by index
        wd.find_elements(By.XPATH, "//input[@name='selected[]']")[index].click()

    def select_contact_by_id(self, contact_id):
        wd = self.app.wd
        # select contact's checkbox by contact id
        wd.find_element(By.XPATH, f"//input[@id='{contact_id}']").click()

    def select_first_contact(self):
        wd = self.app.wd
        # select first contact's checkbox
        wd.find_element(By.XPATH, "(//input[@name='selected[]'])[1]").click()

    def click_view_button_by_index(self, index):
        wd = self.app.wd
        # press view button in row by index
        wd.find_element(By.XPATH, f"//tr[@name='entry'][{index + 1}]/td[7]/a").click()

    def click_edit_button_by_index(self, index):
        wd = self.app.wd
        # press edit button in row by index
        wd.find_element(By.XPATH, f"//tr[@name='entry'][{index + 1}]/td[8]/a").click()

    def click_edit_button_by_id(self, contact_id):
        wd = self.app.wd
        # press edit button in row by index
        wd.find_element(By.XPATH, f"//input[@id='{contact_id}']/ancestor::tr/td[8]/a").click()
        # row.find_element(By.XPATH, "/td[8]/a").click()

    def count(self):
        wd = self.app.wd
        self.click_home_menu()
        return len(wd.find_elements(By.XPATH, "//input[@name='selected[]']"))

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.click_home_menu()

            self.contacts_cache = []
            for element in wd.find_elements(By.XPATH, "//tr[@name='entry']"):
                firstname = element.find_elements(By.TAG_NAME, "td")[2].text
                lastname = element.find_elements(By.TAG_NAME, "td")[1].text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                address = element.find_elements(By.TAG_NAME, "td")[3].text
                all_emails = element.find_elements(By.TAG_NAME, "td")[4].text
                all_phones = element.find_elements(By.TAG_NAME, "td")[5].text

                self.contacts_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                   address=address, all_emails_from_home_page = all_emails,
                                                   all_phones_from_home_page=all_phones))

        return self.contacts_cache

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.click_home_menu()
        self.click_edit_button_by_index(index)

        id = wd.find_element(By.NAME, "id").get_attribute("value")
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        address = wd.find_element(By.NAME, "address").text
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        home_phone = wd.find_element(By.NAME, "home").get_attribute("value")
        mobile_phone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        work_phone = wd.find_element(By.NAME, "work").get_attribute("value")
        secondary_phone = wd.find_element(By.NAME, "phone2").get_attribute("value")

        return Contact(id=id, firstname=firstname, lastname=lastname,
                       address=address,
                       email=email, email2=email2, email3=email3,
                       home=home_phone, mobile=mobile_phone,
                       work=work_phone, phone2=secondary_phone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.click_home_menu()
        self.click_view_button_by_index(index)

        text = wd.find_element(By.ID, "content").text
        # search by regexp
        # .* - any symbol repeated any times,
        # (.*) - group; when we call group(1) it returns content of this group - phone number
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)

        return Contact(home=home_phone, mobile=mobile_phone, work=work_phone, phone2=secondary_phone)
