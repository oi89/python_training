import random
import allure

from model.group import Group


def test_edit_random_group_name(app, db, check_ui):
    new_group = Group(name='group1-edit')

    with allure.step("Given non-empty group list"):
        if len(db.get_groups_list()) == 0:
            app.group.create(Group(name='group for edit'))

        old_groups = db.get_groups_list()

    with allure.step("Given random group from the list"):
        group_to_edit = random.choice(old_groups)

    with allure.step(f"When edit the group {group_to_edit}"):
        app.group.edit_group_by_id(group_to_edit.id, new_group)

    with allure.step("Then new groups list is equal to old groups list with modified group"):
        assert app.group.count() == len(old_groups)

        # change group_to_edit to new_group in old_groups list for compare
        index = old_groups.index(group_to_edit)
        old_groups[index].name = new_group.name
        new_groups = db.get_groups_list()

        assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)


def test_edit_random_group_header(app, db, check_ui):
    new_group = Group(header='text1-edit')

    with allure.step("Given non-empty group list"):
        if len(db.get_groups_list()) == 0:
            app.group.create(Group(header='group for edit'))

        old_groups = db.get_groups_list()

    with allure.step("Given random group from the list"):
        group_to_edit = random.choice(old_groups)

    with allure.step(f"When edit the group {group_to_edit}"):
        app.group.edit_group_by_id(group_to_edit.id, new_group)

    with allure.step("Then new groups list is equal to old groups list with modified group"):
        assert app.group.count() == len(old_groups)

        # change group_to_edit to new_group in old_groups list for compare
        index = old_groups.index(group_to_edit)
        old_groups[index].header = new_group.header
        new_groups = db.get_groups_list()

        assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)


def test_edit_random_group_footer(app, db, check_ui):
    new_group = Group(footer='text2-edit')

    with allure.step("Given non-empty group list"):
        if len(db.get_groups_list()) == 0:
            app.group.create(Group(footer='group for edit'))

        old_groups = db.get_groups_list()

    with allure.step("Given random group from the list"):
        group_to_edit = random.choice(old_groups)

    with allure.step(f"When edit the group {group_to_edit}"):
        app.group.edit_group_by_id(group_to_edit.id, new_group)

    with allure.step("Then new groups list is equal to old groups list with modified group"):
        assert app.group.count() == len(old_groups)

        # change group_to_edit to new_group in old_groups list for compare
        index = old_groups.index(group_to_edit)
        old_groups[index].footer = new_group.footer
        new_groups = db.get_groups_list()

        assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
