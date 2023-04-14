from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()

        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:  # is logged in by another user
                self.logout()
        self.login(username, password)

    def is_logged_in(self):
        wd = self.app.wd
        # check if there are logout links on the page
        return len(wd.find_elements(By.XPATH, "//form[@name='logout']//a")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        # check if there are correct username in the top of the page
        return wd.find_element(By.XPATH, "//form[@name='logout']/b").text == "(" + username + ")"

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//form[@name='logout']//a").click()
        # wait for appearance of login form
        wd.find_element(By.NAME, "user")

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()
