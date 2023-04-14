from selenium import webdriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            # try to get current url; if done - fixture is valid
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
