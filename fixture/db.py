import pymysql.cursors

from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.orm = ORMFixture(host=host, name=name, user=user, password=password)
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_groups_list(self):
        groups = []
        cursor = self.connection.cursor()

        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (group_id, name, header, footer) = row
                groups.append(Group(id=str(group_id), name=name, header=header, footer=footer))
        finally:
            cursor.close()

        return groups

    def get_contacts_list(self):
        contacts = []
        cursor = self.connection.cursor()

        try:
            query = """SELECT id, firstname, lastname, address, email, email2, email3, mobile, work, home, phone2 
            FROM addressbook 
            WHERE deprecated = '0000-00-00 00:00:00'"""
            cursor.execute(query)
            for row in cursor:
                (contact_id, firstname, lastname, address, email, email2, email3, mobile, work, home, phone2) = row
                contacts.append(Contact(id=str(contact_id), firstname=firstname, lastname=lastname,
                                        address=address, email=email, email2=email2, email3=email3,
                                        mobile=mobile, work=work, home=home, phone2=phone2))
        finally:
            cursor.close()

        return contacts

    def destroy(self):
        self.connection.close()
