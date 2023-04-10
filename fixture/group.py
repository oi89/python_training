from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_menu(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_menu()

        # click new group button
        wd.find_element(By.NAME, "new").click()
        # fill new group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit form
        wd.find_element(By.NAME, "submit").click()

        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_menu()
        # select first group's checkbox
        wd.find_element(By.XPATH, "(//input[@name='selected[]'])[1]").click()
        # press delete button
        wd.find_element(By.XPATH, "//input[@name='delete']").click()
        self.return_to_groups_page()
