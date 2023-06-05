import random
import allure

from model.group import Group


def test_delete_some_random_group(app, db, check_ui):
    with allure.step("Given non-empty group list"):
        if len(db.get_groups_list()) == 0:
            app.group.create(Group(name='group for delete'))

        old_groups = db.get_groups_list()

    with allure.step("Given random group from the list"):
        group = random.choice(old_groups)

    with allure.step(f"When delete the group {group}"):
        app.group.delete_group_by_id(group.id)

    with allure.step("Then new groups list is equal to old groups list without deleted group"):
        assert app.group.count() == len(old_groups) - 1

        new_groups = db.get_groups_list()
        # remove element of the original list and compare lists
        old_groups.remove(group)

        assert new_groups == old_groups

        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
