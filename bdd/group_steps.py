import random
from pytest_bdd import given, when, then, parsers

from model.group import Group


@given("a group list", target_fixture="groups_list")
def get_groups_list(db):
    return db.get_groups_list()


@given(parsers.parse('a group with {name}, {header}, {footer}'), target_fixture="new_group")
def get_new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when("add the group")
def add_new_group(app, new_group):
    app.group.create(new_group)


@then("new groups list is equal to old groups list with added group")
def check_added_group(db, groups_list, new_group):
    old_groups = groups_list
    new_groups = db.get_groups_list()
    old_groups.append(new_group)

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


@given("non-empty group list", target_fixture="non_empty_groups_list")
def get_non_empty_groups_list(db, app):
    if len(db.get_groups_list()) == 0:
        app.group.create(Group(name="group for delete"))

    return db.get_groups_list()


@given("random group from the list", target_fixture="random_group")
def get_random_group(non_empty_groups_list):
    return random.choice(non_empty_groups_list)


@when("delete the group")
def delete_group(random_group, app):
    app.group.delete_group_by_id(random_group.id)


@then("new groups list is equal to old groups list without deleted group")
def check_deleted_group(non_empty_groups_list, random_group, db):
    old_groups = non_empty_groups_list
    new_groups = db.get_groups_list()
    old_groups.remove(random_group)

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
