from pony.orm import *
from datetime import datetime
from pymysql.converters import decoders

from model.group import Group
from model.contact import Contact


class ORMFixture:
    # object to bind to Database
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups",
                       lazy=True)

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts",
                     lazy=True)

    def __init__(self, host, name, user, password):
        # bind to database; conv=decoders - use converters from pymysql
        self.db.bind("mysql", host=host, database=name, user=user, password=password)
        # map database tables to ORM classes
        self.db.generate_mapping()
        # show SQL query in console
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert_groups(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)

        return list(map(convert_groups, groups))

    @db_session
    def get_groups_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert_contacts(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)

        return list(map(convert_contacts, contacts))

    @db_session
    def get_contacts_list(self):
        # select contacts where deprecated field is like '0000-00-00 00:00:00'
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        # get all contacts in this group from 'contacts' field
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        # get all contacts where specified group not in groups from 'groups' field
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact
                                                     if c.deprecated is None and orm_group not in c.groups))
