# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
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
        self.login(username="admin", password="secret")
        self.add_new_contact(contact)
        self.logout()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def click_add_new_menu(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def add_new_contact(self, contact):
        wd = self.wd

        # click "add new"
        self.click_add_new_menu()

        # fill new contact form
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(contact.home)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(contact.work)
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        wd.find_element(By.NAME, "bday").click()
        wd.find_element(By.XPATH, "//option[@value='%s']" % contact.bday).click()
        wd.find_element(By.NAME, "bmonth").click()
        wd.find_element(By.XPATH, "//option[@value='%s']" % contact.bmonth).click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        wd.find_element(By.NAME, "aday").click()
        wd.find_element(By.XPATH, "//select[@name='aday']/option[@value='%s']" % contact.aday).click()
        wd.find_element(By.NAME, "amonth").click()
        wd.find_element(By.XPATH, "//select[@name='amonth']/option[@value='%s']" % contact.amonth).click()
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys(contact.address2)
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys(contact.notes)

        # submit
        wd.find_element(By.XPATH, "//input[@name='submit'][2]").click()

        # return to a home page
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
