from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def click_home_menu(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/addressbook/") and len(wd.find_elements(By.NAME, "searchstring")) > 0):
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

    def delete_first(self):
        wd = self.app.wd
        self.click_home_menu()
        self.select_first_contact()
        # press delete button
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # press OK in alert window
        wd.switch_to.alert.accept()
        self.click_home_menu()
        # обновляем страницу, чтобы удаленные данные не присутствовали
        wd.refresh()


    def edit_first(self, contact):
        wd = self.app.wd
        self.click_home_menu()
        self.select_first_contact()
        # press edit button in first row
        wd.find_element(By.XPATH, "(//tr[@name='entry'])[1]//img[@title='Edit']").click()
        self.fill_contact_form(contact)
        # press update button
        wd.find_element(By.XPATH, "//input[@value='Update']").click()
        self.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        # select first contact's checkbox
        wd.find_element(By.XPATH, "(//input[@name='selected[]'])[1]").click()

    def count(self):
        wd = self.app.wd
        self.click_home_menu()
        return len(wd.find_elements(By.XPATH, "//input[@name='selected[]']"))

    def get_contacts_list(self):
        wd = self.app.wd
        self.click_home_menu()

        contacts = []
        for element in wd.find_elements(By.XPATH, "//tr[@name='entry']"):
            firstname = element.find_elements(By.TAG_NAME, "td")[2].text
            lastname = element.find_elements(By.TAG_NAME, "td")[1].text
            id = element.find_element(By.NAME, "selected[]").get_attribute("value")
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))

        return contacts
