from selenium.webdriver.common.by import By

from model.group import Group


class GroupHelper:

    # кеширование списка групп
    groups_cache = None

    def __init__(self, app):
        self.app = app

    def open_groups_menu(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, element_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, element_name).click()
            wd.find_element(By.NAME, element_name).clear()
            wd.find_element(By.NAME, element_name).send_keys(text)

    def create(self, group):
        wd = self.app.wd
        self.open_groups_menu()
        # click new group button
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit form
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.groups_cache = None

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def delete_first(self):
        wd = self.app.wd
        self.open_groups_menu()
        self.select_first_group()
        # press delete button
        wd.find_element(By.XPATH, "//input[@name='delete']").click()
        self.return_to_groups_page()
        self.groups_cache = None

    def edit_first(self, group):
        wd = self.app.wd
        self.open_groups_menu()
        self.select_first_group()
        # press edit button
        wd.find_element(By.XPATH, "//input[@name='edit']").click()
        self.fill_group_form(group)
        # press update button
        wd.find_element(By.XPATH, "//input[@name='update']").click()
        self.return_to_groups_page()
        self.groups_cache = None

    def select_first_group(self):
        wd = self.app.wd
        # select first group's checkbox
        wd.find_element(By.XPATH, "(//input[@name='selected[]'])[1]").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_menu()
        return len(wd.find_elements(By.XPATH, "//input[@name='selected[]']"))

    def get_groups_list(self):
        if self.groups_cache is None:
            wd = self.app.wd
            self.open_groups_menu()

            self.groups_cache = []
            for element in wd.find_elements(By.XPATH, "//span[@class='group']"):
                name = element.text
                # ищем вложенный элемент input по имени, получаем id из атрибута value
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.groups_cache.append(Group(name=name, id=id))

        return self.groups_cache
